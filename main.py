from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import seleniumwire.undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.proxy import *
import pandas as pd
import os

def quotes_scrapper(url: str) -> list:
    BASE_URL = url
    quotes_list: list[dict] = []
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    proxy_username = "ybhosgpe"
    proxy_password = "p6zoviga3pv4"
    proxy_address = "198.23.239.134"
    proxy_port = 6540

    proxy_url = f"https://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}"

    seleniumwire_options = {
    "proxy": {
        "http": proxy_url,
        "https": proxy_url
        },
    }

    options = Options()
    options.add_argument("--headless=new")

    # initialize the Chrome driver with service, selenium-wire options, and chrome options
    driver = uc.Chrome(options=options, seleniumwire_options=seleniumwire_options)
    # Validate page title
    try:
        expected_title = "Quotes to Scrape"
        breakpoint()
        actual_title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
        if actual_title == expected_title:
            print("Title validated.")
        else:
            print(f"Title validation failed: Expected '{expected_title}', got '{actual_title}'.")
    except TimeoutException:
        print("Failed to validate page title.")
        driver.quit()
        return []

    # Scrape top tags
    try:
        top_tags = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tags-box")))
        tag_links = [tag.get_attribute("href") for tag in top_tags.find_elements(By.TAG_NAME, "a")]
    except TimeoutException:
        print("Failed to fetch top tags.")
        driver.quit()
        return []

    # Process each tag link
    for tag_href in tag_links:
        print(f"Scraping URL: {tag_href}")
        driver.get(tag_href)

        while True:
            try:
                # Wait for quotes to load
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))
                quotes = driver.find_elements(By.CLASS_NAME, "quote")

                for quote in quotes:
                    try:
                        quote_text = quote.find_element(By.CLASS_NAME, "text").text
                        author_name = quote.find_element(By.CLASS_NAME, "author").text
                        author_link = quote.find_element(By.XPATH, ".//span/a").get_attribute("href")
                        try:
                            tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
                        except NoSuchElementException:
                            tags = []

                        # Fetch author details
                        author_info = fetch_author_info(driver, author_link)

                        quotes_list.append({
                            "quote": quote_text,
                            "author": author_name,
                            "tags": tags,
                            "author_info": author_info,
                        })
                    except Exception as e:
                        print(f"Error processing quote: {e}")

                # Navigate to the next page if it exists
                try:
                    next_button = driver.find_element(By.CSS_SELECTOR, "ul.pager li.next a")
                    next_button.click()
                    print("Clicked 'Next' to go to the next page.")

                    # Wait for the next page to load by checking for the presence of quotes
                    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))
                except NoSuchElementException:
                    print("No more pages for this tag.")
                    break

            except TimeoutException:
                print("Error loading quotes on the page.")
                break

    driver.quit()
    return quotes_list

def fetch_author_info(driver, url: str) -> dict:
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    try:
        author_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "author-title"))).text
        dob = driver.find_element(By.CLASS_NAME, "author-born-date").text
        location = driver.find_element(By.CLASS_NAME, "author-born-location").text
        description = driver.find_element(By.CLASS_NAME, "author-description").text
    except TimeoutException:
        print(f"Failed to fetch author info from {url}")
        return {}

    driver.back()

    return {
        "name": author_name,
        "dob": dob,
        "location": location,
        "bio": description,
    }

def write_to_csv(quotes: list[dict]) -> None:
        print("Writing data to CSV...")
        df = pd.DataFrame(quotes)
        df.to_csv("quotes.csv", index=False)

def proxy(driver):
    driver.open

if __name__ == "__main__":
    BASE_URL = "https://quotes.toscrape.com"
    results = quotes_scrapper(BASE_URL)
    write_to_csv(results)
    for result in results:
        print(result)
