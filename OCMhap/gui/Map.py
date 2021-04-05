import folium
import webbrowser
import os
import pandas as pd
import branca.colormap as cm
import branca
import numpy as np
import geopandas as gpd
from folium.plugins import TimeSliderChoropleth

table = lambda x: '<table border="1">%s</table>' % x  # table
tr = lambda x: '<tr>%s</tr>' % x  # table: row
th = lambda x: '<th bgcolor="#66B3FF">%s</th>' % x  # table: title
td = lambda x: '<td bgcolor="#C5DCE7">{}</td>'.format(x)  # table: cell

def make_tb(ls_of_ls, fields):
    _tb = ''.join(tr(''.join(td(i) for i in ls)) for ls in ls_of_ls)
    _th = tr(''.join(th(i) for i in fields))  # title
    return table(_th + _tb)

def make_tb_of_area(Year, Data, Dataname, areaNum, yearNum):
    """
    Year: a list contains the year num
    Data: the data you want to show
    Dataname: name of Data
    areaNum: the # of area you want, start from 0
    yearNum: the # of year, not the length of Year, Year may contains duplicates
    """
    lss = []
    for i in range(0+(areaNum*yearNum), yearNum*(areaNum+1)):
        lss.append([Year[i], Data[i]])
    tbl = make_tb(lss, ['Year', Dataname])
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>""" + tbl + """ 
    </body> 
    </html> """
    return html

def read_data(dataPath, statePath):
    data_df = pd.read_csv(dataPath)
    states = gpd.read_file(statePath)
    return [data_df, states]

def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range

def heatmap(dataName, data_df, states):
    states = states.rename(columns={'NAME': 'State'})
    joined_df = data_df.merge(states, on='State')
    joined_df['normal'] = normalization(joined_df[dataName])

    latitude = np.mean(joined_df['LATITUDE'])
    longitude = np.mean(joined_df['LONGITUDE'])
    map = folium.Map(title='OCM_Map', location=[latitude, longitude], zoom_start=8)

    yearNum = 0
    for i in range(len(joined_df['YEAR'])):
        if (joined_df['YEAR'][i] == joined_df['YEAR'][0] and i != 0):
            break
        else:
            yearNum += 1

    La_Long = []
    for index in range(0, len(joined_df['LATITUDE']), yearNum):
        La_Long.append((joined_df['LATITUDE'][index], joined_df['LONGITUDE'][index]))
    for i in range(len(La_Long)):
        html = make_tb_of_area(joined_df['YEAR'], joined_df[dataName], dataName, i, yearNum);
        iframe = branca.element.IFrame(html=html, width=110, height=300);
        pop_up = folium.Popup(iframe, parse_html=True);
        latitude = La_Long[i][0]
        longitude = La_Long[i][1]
        folium.Marker(
            location=[latitude, longitude],
            popup=pop_up
        ).add_to(map)

    """
    Since the data has been normalized, max is 1 min is 0. 
    If you try to use log in the future, you need to find the max and min for your log data
    """
    max_colour = 1
    min_colour = 0
    cmap = cm.linear.YlOrRd_09.scale(min_colour, max_colour)
    joined_df['colour'] = joined_df['normal'].map(cmap)
    state_list = joined_df['State'].unique().tolist()
    state_idx = len(state_list)
    style_dict = {}

    joined_df['DATE'] = pd.to_datetime(joined_df['DATE'])
    joined_df['DATE'] = joined_df['DATE'].values.astype('datetime64[D]')
    joined_df['date_sec'] = pd.to_datetime(joined_df['DATE'].astype('datetime64[D]').values).astype(int) / 10 ** 9
    joined_df['date_sec'] = joined_df['date_sec'].astype(int).astype(str)

    for i in range(state_idx):
        state = state_list[i]
        result = joined_df[joined_df['State'] == state]
        inner_dict = {}
        for _, r in result.iterrows():
            inner_dict[r['date_sec']] = {'color': r['colour'], 'opacity': 0.7}
        style_dict[str(i)] = inner_dict

    state_df = joined_df[['geometry']]
    state_gdf = gpd.GeoDataFrame(state_df)
    state_gdf = state_gdf.drop_duplicates().reset_index()
    _ = TimeSliderChoropleth(
        data=state_gdf.to_json(),
        styledict=style_dict,

    ).add_to(map)

    _ = cmap.add_to(map)
    cmap.caption = "Normalized number of " + dataName + " cases"
    # map.save(outfile='OCM_Map.html')
    return map




def auto_open(map, mapPath):
    html_page = f'{mapPath}'
    print(html_page)
    map.save(outfile=html_page)
    # open in browser.
    webbrowser.open(html_page, new=2)

def create_map(dataPath, statePath, mapPath, dataName):
    [data_df, states] = read_data(dataPath, statePath)
    map = heatmap(dataName, data_df, states)
    auto_open(map, mapPath)



if __name__ == "__main__":
    dataName = "Asthma"
    dataPath = "../resources/data/data.csv"
    statePath = "../resources/data/tl_2020_us_state.shp"
    path = os.path.pardir
    mapName = "OCM_Map.html"
    mapPath = os.path.join(path, mapName)
    create_map(dataPath, statePath, mapPath, dataName)



