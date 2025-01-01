# selenium-quotes-scrapper
Here is a simple README file for your project:
Quotes Scraper

A Python-based web scraper that collects quotes from Quotes to Scrape using Selenium WebDriver, Selenium Wire for proxy handling, and Pandas for exporting results to a CSV file. It also fetches detailed author information, such as name, birth date, location, and bio.
Features

    Scrapes quotes, authors, and associated tags from the website.
    Navigates paginated results for each tag.
    Collects detailed author information for each quote.
    Supports proxy configuration for anonymous scraping.
    Exports the collected data to a CSV file.

Requirements

    Python 3.6+
    Selenium
    Selenium Wire
    Undetected ChromeDriver (for avoiding detection)
    WebDriver Manager
    Pandas

Installation
Step 1: Clone the repository

git clone https://github.com/your-username/quotes-scraper.git
cd quotes-scraper

Step 2: Install dependencies

Make sure you have Python 3.6+ installed, then run the following to install required dependencies:

pip install -r requirements.txt

Alternatively, if you don’t have a requirements.txt file yet, you can install the necessary libraries individually:

pip install selenium selenium-wire undetected-chromedriver webdriver-manager pandas

Step 3: Set up Proxy (Optional)

If you need to use a proxy for scraping, update the proxy details in the quotes_scrapper function. Modify the proxy_username, proxy_password, proxy_address, and proxy_port values.
Usage

Run the scraper by executing the script directly:

python scraper.py

What it does:

    Validates the page title of the Quotes to Scrape website.
    Scrapes the top tags and visits each tag to collect quotes.
    Collects additional information about the author of each quote.
    Exports the results to a quotes.csv file.

Sample Output:

Each quote in the CSV file contains:

    Quote text
    Author name
    Tags associated with the quote
    Author details (name, date of birth, location, bio)
