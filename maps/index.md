# Walk through of Scraping for Journalists

Presented at #ijf14 by [@annabelchurch](http://twitter.com/annabelchurch)

Slides are here: [Basic Mapping - how do we do it and do we need a map to get there?](https://docs.google.com/presentation/d/1qB4ChCdoXVfPzXKDS33Z1INAugeKDysb6ttqjxb6-_U/edit?usp=sharing)

# 0. Stories to tell

An example [Cholera map](http://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak) from [Edward Tufte's The Visual Display of Quantitative Information](http://www.edwardtufte.com/tufte/books_vdqi)


#1. What should you map? 

We want to Map all the things right?

* Mathew Ericson urges us to resist impulse map geographic data all the time - [When Maps should be maps](http://www.ericson.net/content/2011/10/when-maps-shouldnt-be-maps/). But why?
	* [Gay rights - the Guardian](http://www.theguardian.com/world/interactive/2012/may/08/gay-rights-united-states)
    * [Legalisation of Marijuana - Mother Jones ](http://www.motherjones.com/politics/2014/02/pot-marijuana-legalization-map-states)
	* [House map by NYT](http://elections.nytimes.com/2010/results/house)
	* [Elections data without the map by NYT](http://www.nytimes.com/interactive/2011/09/30/us/politics/keys-to-victory.html?_r=0)
	* [Mapping data collected by a cell phone by ZeitOnline](http://www.zeit.de/datenschutz/malte-spitz-data-retention)
	* [Death by country by the Guardian](http://www.theguardian.com/world/datablog/2014/mar/27/death-penalty-statistics-2013-by-country)
	
* When to map geographic data? When the patterns you want to find are geographic ones.

* The map is a part of the story, not the whole story. 

* Obama vs McCain is geography or education a better answers what question? The campaign targeting was done by demographics	
	* [Map](http://elections.nytimes.com/2010/results/house) vs [Scatter plot](http://www.nytimes.com/interactive/2011/09/30/us/politics/keys-to-victory.html)
        
# 2. Understanding maps

* Geodata (Geographic data)
* Lattitude and Longditude
* We use decimal degrees instead of degrees, minutes, seconds.
* Projections - inaccurately make the world flat
* Shape of the earth - Earth is not a sphere more like an oblate spheroid - squashed bumpy sphere
* Different projections distort the earth in different ways      
* Map geometry: dots and lines on a map. Dots and lines are are lists of lats and longs
    * Ways of representing map features: geometry (countries), properties (data)
        * [Shapefiles](http://en.wikipedia.org/wiki/Shapefile)
           	*   .shp — The geometry for all the features.
            *   .shx — A helper file that stores what order the shapes should be in.
            *   .dbf — stores the properties of each feature in a spreadsheet-like format.
             * Other optional files storing things like a project description and styling (only the above three files are required)
        * [GeoJSON](http://geojson.org/)
        * [KML](https://developers.google.com/kml/)
        * [TopoJSON](https://github.com/mbostock/topojson/wiki)
    
   * Types of map implementations
       * Slippy maps - google maps and leaflet maps
       * Javascript + SVG/Canvas - A fun example is [mapping san franscisco streets](http://sfstreets.noahveltman.com/)
       
    * Types of map by example
       * Choropleth maps - [Waffenland Deutschland by ZeitOnline](http://www.zeit.de/2014/04/waffen-deutschland)   
       * Proportional symbol maps - [Young adults still living with parents by the Guardian](http://www.theguardian.com/news/datablog/2014/mar/24/young-adults-still-living-with-parents-europe-country-breakdown) or [Elections by ZeitOnline](http://www.zeit.de/politik/deutschland/electionland)
        * Dot or point maps - [Mapping America: Every City, Every Block by NYT](http://projects.nytimes.com/census/2010/explorer)
        * Isopleth maps (heap maps) - [Homeless map](http://cartifact.com/webmaps/homeless/)
        * Cartogram - [High distortion of th US countries rescaled in proportion to population](http://upload.wikimedia.org/wikipedia/commons/4/47/Cartlinearlarge.png) or [the Guardians distribution around the world](http://www.viewsoftheworld.net/wp-content/uploads/2013/08/GuardianNews2012_WithoutBritain_Oceans.jpg)


# 3. Making them understandable 
    
* [Some colour theory described here](http://earthobservatory.nasa.gov/blogs/elegantfigures/2013/08/05/subtleties-of-color-part-1-of-6/) and [a tool to help - Colour brewer](http://colorbrewer2.org/)
* Understanding data language: Sequential, categorical data, points, binning, aggregate, interpolation
 * Usabilibility - [Niemen labs](http://www.nngroup.com/articles/)   
    * Interactivity

# 4. Getting data
* by downloading, scraping, extracting or compiling your own
	* [World bank](http://data.worldbank.org/indicator/SP.RUR.TOTL.ZS)
    * [Italian statistics](http://www.istat.it/en/archive/50621)
    
# 5. Practicalities

Demo


# Tools
* [Datawrapper](https://datawrapper.de/)
* [CartoDB](http://cartodb.com/)
* [Google fusiontable maps](https://support.google.com/fusiontables/answer/2571232?hl=en)
* [Leaflet](http://leafletjs.com/)
* [Tableau](http://www.tableausoftware.com/public/)
* [qgis](http://www.qgis.org/en/site/)
* [Mapstarter](http://mapstarter.com/)
* [Other Mapbox](https://www.mapbox.com/tilemill/)
* [Storymap](http://storymap.knightlab.com/) 
* [Timelinejs](http://timeline.knightlab.com/)
    
## Further help

* [Noah Veltman's simple explanation of maps](https://github.com/veltman/learninglunches/tree/master/maps)
* [Noah Veltman and Tom MacWrights great list mapping tools and helpers](https://github.com/veltman/maps-nicar14) 
* [Find out more about DDJ with the Data Journalism Handbook](http://www.datajournalismhandbook.org/)
* [Examples of what not to do](http://misguidedmaps.com/)
    





