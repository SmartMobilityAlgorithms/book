# Introduction to Geographic Data Science

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://github.com/SmartMobilityAlgorithms/GettingStarted/graphs/contributors) 
[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://github.com/SmartMobilityAlgorithms/GettingStarted/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/SmartMobilityAlgorithms/GettingStarted/pulls)
[![Gitter](https://badges.gitter.im/SmartMobilityAlgorithms/community.svg)](https://gitter.im/SmartMobilityAlgorithms/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SmartMobilityAlgorithms/GettingStarted/master)


### Contents

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
