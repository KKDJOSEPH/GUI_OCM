import io
import os
import setuptools


name = "OCMhap"
description = "OCM Advisory Health Analytics Platform"
version = "0.1.0"
# Should be one of:
# "Development Status :: 3 - Alpha"
# "Development Status :: 4 - Beta"
# "Development Status :: 5 - Production/Stable"
release_status = "Development Status :: 3 - Alpha"
dependencies = [
    "branca",
    "folium",
    "geopandas",
    "tkinter",
    "numpy",
    "pandas",
    "pandastable"
]
extras = {

}
python_version = ">=3.6"
urls = {
    "US County Data": "https://simplemaps.com/data/us-counties"
}


package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = [
    package for package in setuptools.find_packages() if package.startswith("OCMhap")
]

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="",
    author_email="",
    license="MIT",
    url="",
    classifiers=[
        release_status
    ],
    keywords="health analytics, OCM Advisory",
    packages=packages,
    install_requires=dependencies,
    python_requires=python_version,
    extras_require=extras,
    entry_points={
        "console_scripts": [
            "OCMhap=OCMhap.controller:main"
        ]
    },
    project_urls=urls,
    include_package_data=True,
    package_data={
        "test_data": ["resources/data/data.csv"],
        "ocm_icons": ["resources/images/ocm_icon.png", "resources/images/ocm_logo.png"],
        "state_data": [
            "resources/tl_2020_us_state.cpg",
            "resources/tl_2020_us_state.dbf",
            "resources/tl_2020_us_state.prj",
            "resources/tl_2020_us_state.shp",
            "resources/tl_2020_us_state.shp.ea.iso.xml",
            "resources/tl_2020_us_state.shp.iso.xml",
            "resources/tl_2020_us_state.shx"
        ]
    },
)
