---
title: Scraping with python
notesSeparator: \n...\n
revealOptions:
    transition: 'fade'
---


## Scraping with python

---

### We will be using Beautiful Soup

___

### Why Python?

Why not import.io? or R? or Ruby? or Javascript?

[Python vs R the basics](https://thedhrelay.wordpress.com/2015/04/27/side-by-side-web-scraping-in-r-vs-python/)

[Python vs R analysis](https://www.dataquest.io/blog/python-vs-r/)

To be honest, do what you know until it doesn't work and then change. I started with Python, but start with anything. You. will. be. Okay.

Python is good to learn with.

---

## Starting

### Editors

* [Atom](https://atom.io/) - https://atom.io/

* [Sublime](https://www.sublimetext.com/) - https://www.sublimetext.com/

---

### Installation

#### Mac, Windows, Linux

* You want to run Python 2.7 for this tutorial
* If you have a Mac you probably already have Python, and this should do for now. There are however [some limitations](http://docs.python-guide.org/en/latest/starting/install/osx/), so I do it differently


[full instructions](https://learnpythonthehardway.org/book/ex0.html)


---

### The Terminal
    python --version

---

### pip

#### Package management

Package managers that allow you to install what we need from the command line. It does make things easier, allowing you to type a command (into the terminal...) and have stuff install.

A package is code someone else has written, a library, a framework.



Python Package Index (PyPI)

So we are using an existing package manger to install another package manager

    easy_install pip

___

I installed my python with Homebrew.




---



So

https://virtualenv.pypa.io/en/stable/installation/

---

## requrements
    pip install beautifulsoup4
    pip install lxml

---

## [Virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### install
    pip install virtualenv

### run
    virtualenv env
    source ./env/bin/activate

...

    deactivate
    or close console

    pip freeze > requirements.txt
    pip install -r requirements.txt

---

## Editing files, file names, running files

---

## Inspecting

...

page composition
python repl (read–eval–print loop)
control D

---

## Getting stuff off a page

...

00 - Url checking
lxml - has to understand when html is broken

---

## BeautifulSoup

...

Pros and cons, saves time, bit more robust, can be a bit slower

---

## What if it is many pages

...

Button pressing / Next or number

---

## Dealing with downloading files

---

## Complexity, submiting

...

Form submission

---

# Loading and latency

---

# Kindness

Cache feverently. Stagger http requests. Take only what you need.


...

http://jonathansoma.com/lede/foundations/classes/friday%20sessions/advanced-scraping-form-submissions-completed/

http://lethain.com/an-introduction-to-compassionate-screenscraping/

speed
500milisecons
mimicing a client, multi-processing / multi-threading
if it is latency, then idle threads
