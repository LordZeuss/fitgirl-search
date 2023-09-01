# fitgirl-search
This is a tool which will display magnet links, download the torrent file, or open the webpage based on a searched game.

---
* [General Info](#general-info)
* [How do you use it](#how-do-you-use-it)
* [How it works](#how-does-it-work)
* [Why use it](#why-use-this-script)
* [Installation](#installation)
* [Installing Python](#installing-python)

## General Info

* The tool will display the magnet links for 1337x and RuTor
* The tool will start/display the torrent file download page
* The tool will open the game page on fitgirl's site directly

I will be creating a separate exe version for Windows shortly, to avoid users from having to install python on Windows.

---

## How do you use it?
Here are the steps to use the script
* Search for a game
* Select an option from the list of found games
* You will then be prompted to show
  * Magnet Links for 1337x and RuTor
  * Go to/Display torrent file download page
  * View Game's page on fitgirls site.
That's it!

---

## How does it work?
This script is essentially a webscraper and uses beautifulsoup with python under the hood.

I am simply scraping her official website for the games based on the user's search input, and based on their selection, giving the user a few options.

---

## Why use this script?
This tool can be beneficial for those who do not want to risk potentially using an unofficial fitgirl site

This tool can also speed up searching games, just run the program rather than use the browser.

Easy for beginners or people who just want to simply find a magnet link and off they go.

---

## Installation
Please make sure you have Python and Pip installed.

### Install the requirements
```
pip install -r requirements.txt
```
After that, simply run the script.

**Linux**
```
python3 ./fitgirl-search.py
```
**Windows**
```
python fitgirl-search.py
```

---

## Installing Python

### Linux
```
sudo apt-get install python3
sudo apt install python3-pip
```
### Windows
```
https://www.python.org/downloads/windows/
```
