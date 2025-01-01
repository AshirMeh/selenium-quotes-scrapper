# Quote Scraper with Proxy Support

This project is a Python script that scrapes quotes from [Quotes to Scrape](https://quotes.toscrape.com) website using Selenium WebDriver. It supports navigating through multiple pages and extracting quotes, author information, and tags. The script also supports using a proxy server to anonymize requests and bypass restrictions.

## Features

- Scrapes quotes, author names, and associated tags.
- Supports pagination to scrape quotes from multiple pages.
- Fetches author details like name, birthdate, location, and biography.
- Supports proxy configuration for bypassing restrictions and geolocation-based access control.
- Stores the scraped data into a CSV file.

## Prerequisites

Before running this project, you will need:

- Python 3.x
- Selenium
- ChromeDriver (or a different WebDriver if you're using a different browser)

### Install Dependencies

1. Install the necessary Python packages:

```bash
pip install selenium pandas
