# Books to Scrape - Book Details Scraper

This Python script uses Selenium to scrape book details from the "All Products" section of the [Books to Scrape - Sandbox](http://books.toscrape.com/) website. It extracts the following information:
- Book name
- Price
- Stock status (in stock or out of stock)
- Description

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Selenium (`pip install selenium`)
- WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/chromium.org/driver/) for Google Chrome)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/seunrae/book-scrapper.git
    cd book-scraper
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium
    ```

3. Download and configure the appropriate WebDriver for your browser.

## Usage

1. Open the `scraper.py` file and ensure the path to your WebDriver is correctly specified.
   
2. Run the script:
    ```sh
    python scraper.py
    ```
