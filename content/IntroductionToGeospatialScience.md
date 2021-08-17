# Introduction to Geographic Data Science

## Contents

1.  [Spatial data](#spatial-data) 

2.  [Projection](#projection)

3.  [Plotting](#plotting)
    * [Matplotlib](#Matplotlib)
    * [folium](#folium)
    
4.  [Maven Ride Hailing Service](#maven)
    
5. [References](#references)


---

## Spatial Data

A Geographic Information System (GIS) is a computer-based system to aid in the collection, maintenance, storage, analysis, output, and distribution of spatial data and information [1].

Read geospatial data file
```
import geopandas as gpd
# read geospatial data
# Ontario’s health region geographic data: https://data.ontario.ca/dataset/ontario-s-health-region-geographic-data
ontario=gpd.read_file(r'data\ontario_health_regions\Ontario_Health_Regions.shp')
```

---

## Projection

TBD...

---

## Plotting



### 1. Plotting with Matplotlib

TBD...

### 2. Plotting with folium

TBD...

---

## Maven Ride Hailing Service
TBD...

---

## References

[1] Bolstad, Paul. GIS fundamentals: A first text on geographic information systems. Eider (PressMinnesota), 2016.
