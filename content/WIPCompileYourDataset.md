# Compile your dataset
You can compile your own dataset using the [Overpass QL](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) language that runs on [Overpass turbo](http://overpass-turbo.eu/). You can use this query language to mine OpenStreetMaps data, filter it, and get it ready to be used by `osmnx` or any library that parses `.osm` files. Below is a quick review about using [Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API), which is the official API for reading data from OpenStreetMap servers. All the online [routing services and software](https://wiki.openstreetmap.org/wiki/Routing/online_routers) use it. Additionally, we will usually use [Nominatim](https://github.com/osm-search/Nominatim) to do geocoding/geo-decoding; translating addresses to/from (latitude-longitude). 

Also be aware of the fact that most of the time if you are building a dataset over a very big area in the map, the graph parsed from the data by `osmnx` won't be complete, even though there are physically feasible routes that could make the graph complete and connect all the nodes. This deficiency is usually because of the incomplete [relations](https://wiki.openstreetmap.org/wiki/Relation) and data of `osm` -- don't worry about that now.

For these cases, we will be using [OSRM](http://project-osrm.org/) to fill these gaps when needed, with the help of some utilities in `utilities/src/poi.py`. This can be seen in some of the case studies.

### Using `OverPass QL`

Fire up [Overpass turbo](http://overpass-turbo.eu/) and run these scripts and export it as `.osm` files.

* [**All hospitals around UofT**](./scripts/hospitals_toronto.oql)
* [**All Tim Hortons in Canada**](./scripts/tim_hortons_canada.oql)
* [**All fast food or restaurant places in London**](./scripts/restaurant_fastfood_london.oql)


Finding the bounding box around an area of interest is a recurring problem in writing `OverPass QL` queries. To solve for that, we can use [bbox finder](http://bboxfinder.com/). Don't forget to change the coordinate format to latitude/longitude at the right corner after drawing the polygon around the area of interest.

### Using `Overpass turbo`'s Wizard
[Overpass turbo](http://overpass-turbo.eu/)'s Wizard provides an easy way to auto-generate Overpass QL queries. Wizard syntax is similar to that of a search engine. An example of Wizard syntax is `amenity=hospital` that generates an Overpass QL query to find all the hospitals in a certain region of interest. Hospital locations will be visualized on the map and can be downloaded/copied using the "Export" button. The data can be exported as GeoJSON, GPX, KML, raw OSM data, or raw data directly from Overpass API. You can then use `osmnx` to read `.osm` files with [`osmnx.graph_from_xml`](https://osmnx.readthedocs.io/en/stable/osmnx.html?highlight=from%20file#osmnx.graph.graph_from_xml).

Some examples of `Overpass turbo`'s wizard syntax include:
* **`amenity=restaurant in "Toronto, Canada"`** to find all resturants in City of Toronto.
* **`amenity=cafe and name="Tim Hortons"`** to find all Tim Hortons coffee shops.
* **`(amenity=hospital or amenity=school) and (type:way)`** to find hospitals and schools with close ways mapped.
* **`amenity=hospital and name~"General Hospital"`** will find all hospitals with "General Hospital" part of their names. 

#

**Contributing:** Do you have something cool and want to share it with us? If you collected your data by downloading it directly from OpenStreetMaps and did some filtering with `osmfilter`, open a pull request with the details of the data and how you filtered it. If you collected your data with [overpass turbo](http://overpass-turbo.eu/), please attach your `Overpass QL` script with the data so we can replicate your results, and maybe we can learn a thing or two from your script.

---