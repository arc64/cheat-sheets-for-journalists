# Walk through of Scraping for Journalists

Presented at #ijf14 by [@annabelchurch](http://twitter.com/annabelchurch)

Slides are here: [Getting your data out of the Web - Scraping for Jouralists](https://docs.google.com/presentation/d/1lajIwLfRMwP1VPNp5g9KAqvgPgWt9wXNSEs1E3MUFfU/edit#slide=id.g33298cfa3_025)

## Why do I need to scrape?

So you want to investigate something, seek out information to see if there is a story there. Before the internet you had to find someone, phone someone, use your spy to seek out information.

And this is still true; you can ask for data, you can find it, and you can collect it. However, the web is a storehouse of data.

  * Asking: Freedom of Request - [does your country have this?](http://en.wikipedia.org/wiki/Freedom_of_information_laws_by_country)
  * Finding: You can find it on a public website and download it
  * Collecting: If you can't download this data in bulk you need to collect it. Either by hand, from an [API](https://github.com/veltman/learninglunches/tree/master/apis), or by scraping a website or document like a PDF. Scraping is using a computer to automatically collect the data.

This information is data.

You can get your information from government, organisations or scientific institutions.

If you find data on a website and you need to scrape it, you will need to process it to be machine readable. Why? so that you can analyse it to see if there is any interesting stories there. Machine readable formats include CSV, excel spreadsheets, XML and JSON.

While you should be fine collecting publically avaliable data, there are [legal](http://datajournalismhandbook.org/1.0/en/getting_data_7.html), [licencing](http://opendefinition.org/licenses/), and [compasionate](http://lethain.com/an-introduction-to-compassionate-screenscraping/) considerations to think of when scraping.


## What can I do with it?

Some fabulous examples of what you can do with data driven journalism are:

* [Dollars for Docs by Propublica](http://projects.propublica.org/docdollars/) - Money taken by doctors by drug companies.
* [Large earthquakes in the Los Angeles area by the LA times](http://graphics.latimes.com/responsivemap-large-earthquakes-los-angeles-area/) - Map of magnitude 4 or higher in the LA area.
* [Mars rover tracker by NYT](http://www.nytimes.com/interactive/science/space/mars-curiosity-rover-tracker.html) - showing what you can do with NASA image data
* [Italy public spending: where does the money go? Openspending embeded by the Guardian](http://www.theguardian.com/news/datablog/2011/apr/19/italy-public-spending)
* [Gun ownership by ZeitOnline](http://www.zeit.de/2014/04/waffen-deutschland)

Making data more accessible:

* [OpenInterests](http://openinterests.eu/) - Who has financial or political interests in the European institutions?
* [OpenSpending](https://openspending.org/) - OpenSpending exists to “map the money worldwide”


## Places to get data

If you are in the right place at the right time sometimes documents appear -
[Yanukovych Leaks](http://yanukovychleaks.org/), but mostly you have to do some of the following:

### Ask someone

Ask a real person or the internet at [get the data](http://getthedata.org/) or [Quora](https://www.quora.com/)

### Seek it out

Using Google to find data with advanced query options

For example: "filetype:csv crime" in google will bring back search results that have the keyword crime and a filetype of CSV.

* Search by filetype
	* Spreadsheets - filetype:XLS
    * CSV - filetype:CSV
    * geodata shapefile - filetype:shp
    * database extracts - filetype:MDB, filetype:SQL, filetype:DB
    * PDF - filetype:pdf

* Search portion of a url
    * inurl:

* Search a site
    * site:

* Use keywords such as downloads, database download, directory listing etc

Have a look at the [Data Journalism Handbook](http://datajournalismhandbook.org/1.0/en/getting_data_0.html)

### Root around for data

Look at data blogs and data stories to see what data has been used before to give you inspiration for what is around.

Some examples:-

  * [Datacatalogs.org](http://datacatalogs.org/)

    #### Government
    * [US gov.data](data.gov)
    * [U.K.'s](data.gov.uk)
    * [Australia's](http://data.gov.au/)
    * [Italy's data catalog](http://www.dati.gov.it/content/datigovit-il-portale-dei-dati-aperti-della-pa)
    * [Tenders electronic data](http://ted.europa.eu/TED/main/HomePage.do)

    #### Oranisations
    * [World Bank](http://data.worldbank.org/)
    * [World Health Organization](http://www.who.int/research/en/)

    #### Scientific institutes
    * [NASA](http://nasa.org)
    * [Dryad](http://datadryad.org/)
    * [UK Data archive](http://www.data-archive.ac.uk/)

    #### Other places
    * [Freebase](http://www.freebase.com/)
    * [Datamarket](http://datamarket.com/)
    * [Open Access Directory’s data repository list](http://oad.simmons.edu/oadwiki/Data_repositories)
    * [Open Knowledge Foundation’s datahub.io](http://datahub.io/)
    * [World government data](http://www.theguardian.com/world-government-data)


## What does data look like on a website?

Data can be contained on a single page like the movies produced by [Peter Jackson on IMDB](http://www.imdb.com/name/nm0001392/?ref_=nv_sr_3) or data can be contained in multiple pages like this [Pfizer data](http://www.pfizer.com/responsibility/working_with_hcp/payments_report)


## Ways to scrape

There is some language you will have to understand.

* HTML is the language in which documents on the internet are described
* The DOM is how the browser understands HTML

If you “View source” on a web page you will be able to see see how HTML looks behind any page on the internet. Developer tools in Chrome or Firebug a plugin for Firefox can help you understand the internals of a page by letting you do the following:
	
* “Inspect element” function lets you understand the HTML of any element you can see on a page.
* Network view shows you all the things that get downloaded when you open a page.


### Data tables and single pages

####Google Spreadsheets - scraping with IMPORTHTML (Very easy)

 So when you want to get a HTML table out of a webpage you can use Google Spreadsheets.
 
 How to check if it is a table? "inspect element" and see if it is a table tag

 Scraping a list of Italian cities with Google spreadsheets:
 
 * [Wikipedia list of cities in Italy](http://en.wikipedia.org/wiki/List_of_cities_in_Italy)
    * Open google spreadsheet
    * =IMPORTHTML("http://en.wikipedia.org/wiki/List_of_cities_in_Italy","table",1)
        * autocomplete is your friend
        * Remember the quotes
        * 1 means the first table on the page

    * This auto-updates from the source
    * If you want to keep this dataset fixed you would need to copy it and paste values only

[Extracting data from HTML tables](http://schoolofdata.org/handbook/recipes/liberating-html-tables/) is a complete walkthrough.

#### Extracting tables with browser extensions (Very Easy)
[Table Capture](https://chrome.google.com/webstore/detail/table-capture/iebpjdmgckacbodjpijphcplhebcmeop?hl=en) for Chrome or [Clipboard2Table](https://addons.mozilla.org/en-US/firefox/addon/dafizilla-table2clipboard/) for Firefox

* get the addon you want
* select the table you want, right click and save to a spreedsheet.

#### Extracting more complex data with Scraper - a Chrome extension (Easy)

A browser plugin or extension is a computer program that extends the functionality of your browser.

* Get the [Scraper](https://chrome.google.com/webstore/detail/scraper/mbigbapnjcgaffohmbkdlecaccepngjd) from the Chrome store
* Try this again with [Wikipedia list of cities in Italy](http://en.wikipedia.org/wiki/List_of_cities_in_Italy)
* Right click on the data you want to save and export to spreadsheet

In my case I really want to know who is a member journalism/technology group I co-run in Berlin - [Hacks/Hackers Berlin](http://www.meetup.com/Hacks-Hackers-Berlin/members/)

* Select the whole item you would like to scrape right click and "scrape similiar"
* The main xpath should look like this "//div[2]/div[2]/ul[1]/li"
* If you want to collect more data you could add specific columns to get:
	* the persons name ".//h4""
    * the persons join date ".//div/div[2]/ul/li/span"

More info on [xpath syntax](http://www.w3schools.com/xpath/xpath_syntax.asp)

[Scraper Extension for Chrome](http://schoolofdata.org/handbook/recipes/scraper-extension-for-chrome/) is a complete walk through


### Complex data formats and multiple pages

[import.io](import.io) - download it!



#Where to go from here?

Once you have the data you will have to clean it up, remove duplicates and analyse it. A place to upload and share your data afterwards is the Open Knowledge Foundations [datahub](http://datahub.io/).

There are plenty more resources including:

* [Veltman's learning lunches explain basic internet concepts](https://github.com/veltman/learninglunches)	
* [Scraping for Journalists](https://leanpub.com/scrapingforjournalists)
* [Data Journalism Handbook](http://datajournalismhandbook.org)
* [School of Data](http://schoolofdata.org)

Beyond the scope of this walk through are more complex scraping methods with [Kimono](http://www.kimonolabs.com/), [morph.io](morph.io), [Scraperwiki](https://scraperwiki.com/) or scraping with code using; Python, Beautiful Soup, Scrapy etc.




