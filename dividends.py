import logging
import pandas as pd
import requests
import time

from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CURRENT_STOCKS = Path(f'{Insert Path Here')
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}


def main():
    driver = setup_driver()
    metadata = []
    stocks = open(CURRENT_STOCKS)
    tickers = stocks.read().split('\n')
    for ticker in tickers:
        website = f'https://www.nasdaq.com/market-activity/stocks/{ticker}/dividend-history'
        stock_info = get_info(ticker, website, driver)
        metadata.append(stock_info)
        
    driver.quit()
    df = pd.DataFrame(
        metadata,
        columns = [
            'Ex/EFF DATE', 'TYPE', 'CASH AMOUNT',
            'DECLARATION DATE', 'RECORD DATE',
            'PAYMENT DATE', 'STOCK'
        ]
    )
    df.to_csv('dividends.csv', index=False)


def setup_driver():
    options = Options()
    options.add_argument('log-level=3')
    return webdriver.Chrome(options=options)


def get_info(ticker, website, driver):
    driver.get(website)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    dividend_row = soup.findAll('tr')
    try:
        stock_info = [item.text for item in dividend_row[1]]
        stock_info.append(ticker)
    except (IndexError, AttributeError):
        try:
            website = f'https://www.nasdaq.com/market-activity/funds-and-etfs/{ticker}/dividend-history'
            driver.get(website)
            time.sleep(30)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            dividend_row = soup.findAll('tr')
            stock_info = [item.text for item in dividend_row[1]]
            stock_info.append(ticker)
        except (IndexError, AttributeError):
            logging.info(f'Stock {ticker} has no dividend history.')
            return ['NA', 'NA', 'NA', 'NA', 'NA', 'NA', ticker]
    return stock_info


if __name__ == '__main__':
    main()
