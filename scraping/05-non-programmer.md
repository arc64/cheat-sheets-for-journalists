
## Data tables and single pages

---

### IMPORTHTML

scraping with Google Spreadsheets

(Very easy)

___

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

___

[Paul Bradshaw - scrape in 60 minutes](http://www.slideshare.net/onlinejournalist/scraping1hr-data-harvest-slideshare)
[Dataharvest](http://www.kaasogmulvad.dk/en/2014/05/training-at-data-harvest-2014/)

---

### Extracting tables with browser extensions

(Very Easy)

...

[Table Capture](https://chrome.google.com/webstore/detail/table-capture/iebpjdmgckacbodjpijphcplhebcmeop?hl=en) for Chrome or [Clipboard2Table](https://addons.mozilla.org/en-US/firefox/addon/dafizilla-table2clipboard/) for Firefox

* get the addon you want
* select the table you want, right click and save to a spreedsheet.

---

### Extracting more complex data with Scraper, a Chrome extension

(Easy)

___

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

---

### [import.io](import.io)

(intermediate)

Complex data formats and multiple pages

---

### [Helium scraper](http://www.heliumscraper.com/en/index.php)

(intermediate)

---

### [Web scraper](http://webscraper.io/)