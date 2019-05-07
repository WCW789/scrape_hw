from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)
    html1 = browser.html
    soup1 = BeautifulSoup(html1, 'html.parser')

    results1 = soup1.find_all('div', class_='list_text')[0]
    listings["news_title"] = results1.find('a').text
    listings["news_p"] = results1.find(
        'div', class_='article_teaser_body').text

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')

    results2 = soup2.find_all('div', class_='img')[0]
    listings["featured_image_url"] = (
        "https://www.jpl.nasa.gov" + results2.find('img')['src'])

    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    html3 = browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')

    results3 = soup3.find_all('div', class_='content')[0]
    listings["mars_weather"] = results3.find('p', class_='tweet-text').text

    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)
    html4 = browser.html
    soup4 = BeautifulSoup(html4, 'html.parser')

    # listings["table"] = soup4.find(
    #     'table', class_='tablepress tablepress-id-mars')
    tables = pd.read_html(url4)
    df = tables[0]
    df.rename(columns={0:'Key', 1:'Fact'}, inplace=True)
    html_table = df.to_html()
    listings["table"] = html_table.replace('\n', '')

    return listings
