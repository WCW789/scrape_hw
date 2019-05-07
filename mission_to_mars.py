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
    df.rename(columns={0: 'Key', 1: 'Fact'}, inplace=True)
    html_table = df.to_html()
    listings["table"] = html_table.replace('\n', '')

    url5_1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url5_1)
    html5_1 = browser.html
    soup5_1 = BeautifulSoup(html5_1, 'html.parser')
    image5_1 = soup5_1.find_all('img', class_='wide-image')[0]["src"]

    url5_2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url5_2)
    html5_2 = browser.html
    soup5_2 = BeautifulSoup(html5_2, 'html.parser')
    image5_2 = soup5_2.find_all('img', class_='wide-image')[0]["src"]

    url5_3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url5_3)
    html5_3 = browser.html
    soup5_3 = BeautifulSoup(html5_3, 'html.parser')
    image5_3 = soup5_3.find_all('img', class_='wide-image')[0]["src"]

    url5_4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url5_4)
    html5_4 = browser.html
    soup5_4 = BeautifulSoup(html5_4, 'html.parser')
    image5_4 = soup5_4.find_all('img', class_='wide-image')[0]["src"]

    listings["img1"] = "https://astrogeology.usgs.gov/" + image5_1
    listings["img2"] = "https://astrogeology.usgs.gov/" + image5_2
    listings["img3"] = "https://astrogeology.usgs.gov/" + image5_3
    listings["img4"] = "https://astrogeology.usgs.gov/" + image5_4

    return listings
