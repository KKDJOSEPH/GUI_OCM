import folium
import folium.plugins
import pandas
import branca
import numpy
import geopandas

import os
import pkg_resources
import webbrowser


class AnimatedMapController(object):
    """
    An AnimatedMapController represents a controller used for the creation
    of an animated map.
    """

    county_geo_data = geopandas.read_file(
        pkg_resources.resource_filename(__name__, "../resources/data/cb_2018_us_county_500k.shp"))
    county_data = pandas.read_csv(
        pkg_resources.resource_filename(__name__, "../resources/data/uscounties.csv"), dtype=str)

    def __init__(self, controller, data):
        """
        Initialize an AnimatedMapController.

        :param controller: The analysis controller controlling this object.
        :param data: The data frame from which to generate the animated map.
        """
        self._controller = controller
        self._data = data
        self._column_name = None
        self._file_name = os.path.join(os.pardir, "map.html")

    @property
    def data(self):
        """The data object"""
        return self._data

    @property
    def column_name(self):
        """The column name of the data to plot"""
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Set the column name of the data to plot"""
        if column_name not in self._data.attributes:
            raise ValueError("invalid column name")
        self._column_name = column_name

    def _validate_county_codes(self):
        """
        Validate the county codes in the data.

        :return: true if the county codes represent valid FIPS county
            codes.
        """
        county_codes = set(self.data.data["FIPS_State_Code"] + self.data.data["FIPS_County_Code"])
        known_codes = set(self.county_data["county_fips"].astype(str))
        unknown_codes = county_codes.difference(known_codes)
        if len(unknown_codes) > 0:
            self._controller.message("Invalid FIPS codes: {}".format(unknown_codes))
            return False
        return True

    def _add_table_popup_to_map(self, folium_map, county_data):
        """
        Add a popup to the folium map containing an html table of the
        county data.

        :param folium_map: the map to add the popup to.
        :param county_data: the county data, including Year, the column
            of interest, and lat and lng.
        """
        html_table = county_data[["Year", self.column_name]].to_html()
        branca_frame = branca.element.IFrame(html=html_table, width=200, height=400)
        popup = folium.Popup(branca_frame, parse_html=True)
        folium.Marker(
            location=[list(county_data["lat"])[0], list(county_data["lng"])[0]],
            popup=popup
        ).add_to(folium_map)

    def generate_map(self):
        if "FIPS_State_Code" not in self.data.attributes or \
                "FIPS_County_Code" not in self.data.attributes or \
                "Year" not in self.data.attributes:
            self._controller.message("Data must contain the following columns: "
                                     "FIPS_State_Code, FIPS_County_Code, Year.")
            return

        if not self._validate_county_codes():
            return

        if os.path.isfile(self._file_name):
            os.remove(self._file_name)

        data = self.data.data.copy()
        data["FIPS"] = data["FIPS_State_Code"] + data["FIPS_County_Code"]
        data = pandas.merge(data, self.county_data,
                            left_on="FIPS", right_on="county_fips",
                            how="left")
        data = pandas.merge(data, self.county_geo_data,
                            left_on=["FIPS_State_Code", "FIPS_County_Code"], right_on=["STATEFP", "COUNTYFP"],
                            how="left")

        data[self.column_name] = data[self.column_name].astype(float)

        folium_map = folium.Map(title='OCM_Map',
                                location=[numpy.mean(data["lat"].astype(float)), numpy.mean(data["lng"].astype(float))],
                                zoom_start=8)

        data["time"] = (pandas.to_datetime(data["Year"], format="%Y").astype(int) / 10 ** 9 + 100000).astype(str)

        color_map = branca.colormap.linear.YlOrRd_09.scale(
            data[self.column_name].min(), data[self.column_name].max())
        data["color"] = data[self.column_name].map(color_map)

        counties = numpy.unique(data["FIPS_County_Code"])
        style_dict = dict()
        for i, county in enumerate(counties):
            county_data = data.loc[data["FIPS_County_Code"] == county]
            self._add_table_popup_to_map(folium_map, county_data)
            time_color_map = dict()
            for _, row in county_data.iterrows():
                time_color_map[row["time"]] = {"color": row["color"], "opacity": 0.7}
            style_dict[i] = time_color_map

        folium.plugins.TimeSliderChoropleth(
            data=geopandas.GeoDataFrame(data[["geometry"]]).drop_duplicates().reset_index(drop=True).to_json(),
            styledict=style_dict,

        ).add_to(folium_map)

        color_map.add_to(folium_map)
        color_map.caption = self.column_name

        folium_map.save(outfile=self._file_name)
        folium_map.render()
        webbrowser.open(self._file_name, new=2)
