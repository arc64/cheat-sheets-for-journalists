# Walk through of Scraping for Journalists

Presented at #ijf14 by @annabelchurch

Slides are here:

## Why do I need to scrape?

So you want to investigate something, seek out information to see if there is a story there. Before the internet you had to find someone, phone someone, use your spy to seek out information.

And that is still valid; you can ask for data, you can find it, and you can collect it.

    * Asking: Freedom of Request - [does your country have this?](http://en.wikipedia.org/wiki/Freedom_of_information_laws_by_country)
    * Finding: You can find it on a public website and download it
    * Collecting: If you can't download this data in bulk you need to collect it. Either by hand, from an API, or by scraping a website or document like .PDF. Scraping is using a computer to automatically collect the data.

This information is data.

You can get your information from government, organisations or scientific institutions.

If you find data on a website and you need to scrape it, you will need to process it to be machine readable. Why? so that you can analyse it to see if there is any interesting stories there. Machine readable formats include CSV, excel spreadsheets, XML and JSON.

While you should be fine collecting publically avaliable data, there are [legal](http://datajournalismhandbook.org/1.0/en/getting_data_7.html) and [licencing](http://opendefinition.org/licenses/), and [compasionate](http://lethain.com/an-introduction-to-compassionate-screenscraping/) considerations when scraping.


## What can I do with it?


Open taps

[Dollars for Docs by Propublica](http://projects.propublica.org/docdollars/)
    - Money taken by doctors by drug companies

http://openinterests.eu/
https://openspending.org/


## Places to get data

### If you are in the right place at the right time sometimes documents appear
[Yanukovych Leaks](http://yanukovychleaks.org/)

### Ask someone
* A real person
* the internet at [get the data](http://getthedata.org/) or (Quora)[https://www.quora.com/]

 Introduction to “the web as data”:

### Seek it out

 Using Google to find data with advanced query options
    * Search by filetype
        * Spreadsheets - filetype:XLS
        * CSV - filetype:CSV
        * geodata shapefile - filetype:shp
        * database extracts - filetype:MDB, filetype:SQL, filetype:DB
        * PDF - filetype:pdf

     * Search portion of a url
         inurl:

    * Search a site
        * site:

    * Use keywords such as downloads, database download, directory listing etc

    Have a look at the [Data Journalism Handbook](http://datajournalismhandbook.org/1.0/en/getting_data_0.html)

### Root around for data

Look at data blogs and data stories to see what data has been used before to give you inspiration for what is around.

Mention data catalogues, e.g. datacatalogues.org and the World Bank portal.

Some examples:-

    * [Datacatalogs.org](http://datacatalogs.org/)

    ### Government
    * [US gov.data](data.gov)
    * [U.K.'s](data.gov.uk)
    * [Australia's](http://data.gov.au/)
    * [Italy's data catalog](http://www.dati.gov.it/content/datigovit-il-portale-dei-dati-aperti-della-pa)
    * [Tenders electronic data](http://ted.europa.eu/TED/main/HomePage.do)

    ### Oranisations
    * [World Bank](http://data.worldbank.org/)
    * [World Health Organization](http://www.who.int/research/en/)

    ### Scientific institutes
    * [NASA](http://nasa.org)
    * [Dryad](http://datadryad.org/)
    * [UK Data archive](http://www.data-archive.ac.uk/)

    ### Other places
    * [Freebase](http://www.freebase.com/)
    * [Datamarket](http://datamarket.com/)
    * [Open Access Directory’s data repository list](http://oad.simmons.edu/oadwiki/Data_repositories)
    * [Open Knowledge Foundation’s datahub.io](http://datahub.io/)
    * [World government data](http://www.theguardian.com/world-government-data)


## What does data look like on a website?

Show a data-bearing site and highlight the difference between sites where all the desired data is on a single page, versus those where there is an index page and many details pages.

     Single page example: http://www.imdb.com/name/nm0001392/?ref_=nv_sr_3
     Multipage example: http://www.pfizer.com/responsibility/working_with_hcp/payments_report

Play with one or two sites where you need to do a bit of wiggling to get a list of all entries, e.g. by doing a wildcard search or going through all regions on a regional search.


Mention that there are ways that online databases can expose raw data (APIs).

## Ways to scrape

There is some language you will have to understand.
    * HTML is the language in which documents on the internet are described
    * The DOM is how the browser understands HTML

    If you “View source” on a web page you will be able to see see how HTML looks behind any page on the internet. Developer tools in Chrome or Firbug aplugin for Firefox can help you understand the internals of a page by letting you do the following:
         * “Inspect element” function lets you understand the HTML of any element you can see on a page.
         * Network view shows you all the things that get downloaded when you open a page.


### Data tables and single pages

####Google Spreadsheets - scraping with IMPORTHTML (Very easy)

 So when you want to get a HTML table out of a webpage you can use Google Spreadsheets.
    * How to check if it is a table?

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

#### Table Capture for Chrome or Clipboard2Table for Chrome - browser extensions to extract tables (Very Easy)

    * get the addon you want
    * select the table you want, right click and save to a spreedsheet.

####Scraper - scraping with a browser extension (Easy)

A browser plugin or extension is a computer program that extends the functionality of your browser.
    * Get the plugin from the Chrome store
    * Try this again with [Wikipedia list of cities in Italy](http://en.wikipedia.org/wiki/List_of_cities_in_Italy)
        * Right click on the data you want to save and export to spreadsheet


    * or in my case I really want to know who is a member journalism/technology group I co run in Berlin - [Hacks/Hackers Berlin](http://www.meetup.com/Hacks-Hackers-Berlin/members/)
        * For demo
         //div[2]/div[2]/ul[1]/li
        .//h4
        .//div/div[2]/ul/li/span


    More info on [xpath syntax](http://www.w3schools.com/xpath/xpath_syntax.asp)

    [Scraper Extension for Chrome](http://schoolofdata.org/handbook/recipes/scraper-extension-for-chrome/) is a complete walk through


### Complex data formats and multiple pages


 [import.io](import.io) - Show the tool, explain how to download it and walk people through using it based on a simple page.



Advanced options like morph.io, ScraperWiki, coding with python


## What do you do after you have the data?

Explain next steps: cleaning the data with Refine, or making a nice pivot table with Excel that has a summary of the data the web site wouldn’t provide.

Dedupe dates and names

http://www.propublica.org/nerds/item/using-google-refine-for-data-cleaning


## Tools

For single pages:
[Scraper a Chrome plugin](https://chrome.google.com/webstore/detail/scraper/mbigbapnjcgaffohmbkdlecaccepngjd)

For more complex scraping:
[Scraperwiki]()
[import.io](https://import.io/)
[Kimono](http://www.kimonolabs.com/)

Beyond the scope of this walk through is Scraping with code using; Python, Beautiful Soup, Scrapy etc.

A place to upload your data afterwards is the Open Knowledge Foundations [datahub](http://datahub.io/)

# Resources

[Scraping for Journalists](https://leanpub.com/scrapingforjournalists)
[Data Journalism Handbook](http://datajournalismhandbook.org)
