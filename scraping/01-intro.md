---
title: Scraping
separator: \n---\n
verticalSeparator: \n----\n
notesSeparator: \n___\n
revealOptions:
    transition: 'fade'
---

# Get all the data
(A walk-through of Scraping for Journalists)

---

with your co-host [@annabelchurch](http://twitter.com/annabelchurch)

---

## Why do I need to scrape?

it isn't always in the format we want

___

So you want to investigate something, seek out information to see if there is a story there. Before the internet you had to find someone, phone someone, use your spy to seek out information.

---

## Ask for it, find it, collect it.

___

And this is still true; you can ask for data, you can find it, and you can collect it. However, the web is a storehouse of data.

  * Asking: Freedom of Request - [does your country have this?](http://en.wikipedia.org/wiki/Freedom_of_information_laws_by_country)
  * Finding: You can find it on a public website and download it
  * Collecting: If you can't download this data in bulk you need to collect it. Either by hand, from an [API](https://github.com/veltman/learninglunches/tree/master/apis), or by scraping a website or document like a PDF. Scraping is using a computer to automatically collect the data.

---

## Information is data.

___

You can get your information from government, organisations or scientific institutions.

If you find data on a website and you need to scrape it, you will need to process it to be machine readable. Why? so that you can analyse it to see if there is any interesting stories there. Machine readable formats include CSV, excel spreadsheets, XML and JSON.

While you should be fine collecting publically avaliable data, there are [legal](http://datajournalismhandbook.org/1.0/en/getting_data_7.html), [licencing](http://opendefinition.org/licenses/), and [compasionate](http://lethain.com/an-introduction-to-compassionate-screenscraping/) considerations to think of when scraping.

One thing to remember when you scrape is that computers are fast. Humans are slow, and if you scrape a lot of data very fast from someones website - you can stop that site from working.

---

## Most common things to scrape

content, tables, URLs

___

So scraping. You can look for a specific piece of content.

i.e. All of the actors in a movie, or all of the images for a movie from [IMDB](http://www.imdb.com/title/tt0121210/)

Or a table.

i.e Like demographic [data on wikipedia](https://en.wikipedia.org/wiki/European_migrant_crisis)

Or URLs to more content.

i.e Like the bios of all the [deceased members of the house of lords](https://www.parliament.uk/mps-lords-and-offices/lords/deceased-lords/)





