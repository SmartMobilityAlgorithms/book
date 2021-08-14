# Datasets

This repo contains information about how to obtain or compile a dataset for the coruse project problem. 

---
## Geospatial Datasets
Geospatial datasets contain map locations of regions or points of interest.

### 1. Compile your dataset
You can compile your own dataset using [Overpass QL](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) language that runs on [Overpass turbo](http://overpass-turbo.eu/). You can use this query langauge to mine OpenStreetMaps data and filter it and get it ready to be used by `osmnx` or any library that parses `.osm` files and then we would go through a quick review over [Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API), which is the official API for reading data from OpenStreetMap servers and [all the online routing services and software use it](https://wiki.openstreetmap.org/wiki/Routing/online_routers) and usually along side with it we would have [Nominatim](https://github.com/osm-search/Nominatim) to do geo\[coding-decoding\]; translating addresses to/from (latitude - longitude). 

Also be aware of the fact that most of the time if you are taking your dataset over a very big area in the map, the graph parsed from the data by `osmnx` wouldn't be complete even though there are physical feasible routes that could make the graph complete and connect all the nodes, but the deficiency usually is because of the incomplete [relaions](https://wiki.openstreetmap.org/wiki/Relation) and data of `osm` -- don't worry about that now.

In that case, we will be using [OSRM](http://project-osrm.org/) to fill these gaps when needed with the help of some utilities in `utilities/src/poi.py`, it will be used on case studies.

### Using `OverPass QL`

Fire up [Overpass turbo](http://overpass-turbo.eu/) and run these scripts and export it as `.osm` files.

* **All hospitals around UofT** [here](./scripts/hospitals_toronto.oql)
* **All Tim Hortons in Canada**  [here](./scripts/tim_hortons_canada.oql)
* **All fast food or restaurant places in London** [here](./scripts/restaurant_fastfood_london.oql)


It is recurrent problem in writing `OverPass QL` to find the bounding box of an area, for that we use [bbox finder](http://bboxfinder.com/) and don't forget to change coordinate format to latitude/longitude at the right corner after drawing polygon around the area of interest.

### Using `Overpass turbo`'s Wizard
[Overpass turbo](http://overpass-turbo.eu/)'s Wizard provides an easy way to auto-generate Overpass QL queries. Wizard syntax is similar to a search engine. An example of Wizard syntax is `amenity=hospital` that generates an Overpass QL query to find all the hospitals in certain region of interest. Hospital locations will be visualized on the map and can downloaded/copied using "Export" button as GeoJSON, GPX, KML, raw OSM data, raw data directly from Overpass API. You can them us `osmnx` to read `.osm` file with [`osmnx.graph_from_xml`](https://osmnx.readthedocs.io/en/stable/osmnx.html?highlight=from%20file#osmnx.graph.graph_from_xml).

The following `Overpass turbo`'s wizard synatx:
* **`amenity=restaurant in "Toronto, Canada"`** to find all resturants in City of Toronto.
* **`amenity=cafe and name="Tim Hortons"`** to find all Tim Hortons coffee shops.
* **`(amenity=hospital or amenity=school) and (type:way)`** to find hospitals and schools with close ways mapped.
* **`amenity=hospital and name~"General Hospital"`** will find all hospitals with "General Hospital" part of their names. 

#

**Contributing:** You have something cool and you want to share it with us? If you got your data by downloading it directly from OpenStreetMaps and did some filtering with `osmfilter`, open a pull request with the details of the data and how you filter it. If you got your data with [overpass turbo](http://overpass-turbo.eu/), please attach your `Overpass QL` script with the data so we can replicate your results and maybe we can learn a thing or two from your script.

---

### 2. Avialable open datasets
* [Geofabrik](https://download.geofabrik.de/index.html)
* [Factory POI](http://www.poi-factory.com/)
* [Global Rural-Urban Mapping Project (GRUMP)](https://sedac.ciesin.columbia.edu/data/set/grump-v1-settlement-points)
* [GeoNames Data](https://www.geonames.org/export/)
* [City of Toronto](https://www.toronto.ca/city-government/data-research-maps/open-data/)
* [ArcGIS Hub](https://www.esri.com/en-us/arcgis/products/arcgis-hub/overview)
* [GeoHub City of Brampton](https://geohub.brampton.ca/pages/data)
* [City of Markham](https://data-markham.opendata.arcgis.com/)
* [New York City](https://opendata.cityofnewyork.us/)
* [BBBike](https://extract.bbbike.org/)
* [Mapzen](https://github.com/tilezen/joerd/tree/master/docs)
* [openterrain list](https://github.com/openterrain/openterrain/wiki/Terrain-Data)
* [terrain party](https://terrain.party/)
* [OpenMapTiles](https://openmaptiles.org/)
* [UofT MDL](https://mdl.library.utoronto.ca/)
* [GADM maps and data](https://gadm.org/index.html)
* [Elevation data](https://www.opentopodata.org/)
* ...

---

### 3. Commerically available datasets
* [Planet.osm](https://planet.openstreetmap.org/)
* [MapTiler](https://www.maptiler.com/)
* [Factual Global Places](https://www.factual.com/data-set/global-places/)
* [TravelTime API](https://docs.traveltime.com/api/overview/introduction)
* [Precisely](https://www.precisely.com/)
* [World Cities Database](www.worldcitiesdatabase.com )
* [SafeGraph](https://www.safegraph.com/)
* [Google Maps Platform](https://cloud.google.com/maps-platform/)
* [Here Maps for Developers](https://developer.here.com/products/here-sdk)
* [Ratio City](https://www.ratio.city/)
* [100 feet](https://www.beans.ai/index)
* [MPAC Residential Property Assessments](https://www.mpac.ca/)
* ...

---

## Traffic Datasets
* [traffic per edge](https://github.com/Project-OSRM/osrm-backend/wiki/Traffic)
* [Toronto Open Data](https://www.toronto.ca/city-government/data-research-maps/open-data/)
* [Open Traffic](https://github.com/opentraffic)
* [Google Routes](https://cloud.google.com/maps-platform/routes)

---
## Parking Tickets Datasets
* [City of Toronto Parking Tickets](https://ckan0.cf.opendata.inter.prod-toronto.ca/tr/dataset/parking-tickets)
* [Toronto Parking Tickets Visualziation](https://github.com/ian-whitestone/toronto-parking-tickets)
* ...

---
## Public Transport Networks Datasets
* [Google Transit APIs](https://developers.google.com/transit)
* ...

---
## Planned events, road work, and other temporary changes to the road network
* [one.network](https://us.one.network/)
* ...

---
## Traffic Crashes Datasets
* [A Countrywide Traffic Accident Dataset (2016 - 2020)](https://www.kaggle.com/sobhanmoosavi/us-accidents)
* ...

---
## Emission Datasets
* [Ontario Air Quality Data Sets](http://www.airqualityontario.com/science/data_sets.php)
* ...

---
## Environment Datasets
* [Canadian Open Geospatial Data](https://canadiangis.com/data.php)
* [Government of Canada Open Data Portal](https://open.canada.ca/data/en/dataset)
* ...

---
## Mobility-aware urban design, active transportation modeling and access analysis for amenities and public transport
* [Urbano](https://www.urbano.io/)
* ...

---
## Accessibility
* [Wheelmap](https://wheelmap.org/)
* ...


---
## Open Source Projects
* [GIScience](https://github.com/GIScience)
* ...


