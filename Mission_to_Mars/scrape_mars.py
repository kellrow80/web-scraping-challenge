
#Dependencies

from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#a function called scrape that will execute all of your scraping code from above
#and return one Python dictionary containing all of the scraped data.


def scrape():

# Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    
#URL to use for Mars News and open URL

    url = 'https://redplanetscience.com'
    browser.visit(url)

    news_title, news_teaser = news(browser)

    data = {
            "title": news_title,
            "teaser": news_teaser,
            "featured_image": image(browser),
            "info_table": table(browser),
            "hemisphere_images": hemisphere(browser)

    }

    browser.quit()

    return data

  

def news(browser):
#Create Beautiful Soup Object

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

#Get Latest News Title
    # try:
    news_title = soup.find('div', class_='content_title').text
        

    #Get Latest News teaser paragraph
    news_teaser = soup.find('div', class_='article_teaser_body').text

    # except AttributeError:
        # return None, None

    return (news_title, news_teaser)


#URL to use for Mars Images and open URL

def image(browser):

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

#Create BeautifulSoup Object

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

#Create URL string for featured image

    featured_image_url = (url + "image/featured/mars3.jpg")

    return featured_image_url


#Mars URL to use for table info


def table(browser):

    url = 'https://galaxyfacts-mars.com/'

#Use Pandas to read html

    mars_info = pd.read_html(url)

#Put table into dataframe

    mars_info_df = mars_info[0]

#Convert Dataframe into HTML

    html_table = mars_info_df.to_html()

    return html_table

#URL for Mars Hemispheres and open URL


def hemisphere(browser):

    url = 'https://marshemispheres.com/'
    browser.visit(url)

#Create BeautifulSoup Object

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


#Create URL string for Cerberus image

    cerberus_image = (url + "images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg")


#Create URL string for Schiaparelli image

    schiaparelli_image = (url + "images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg")


#Create URL string for Syrtis image

    syrtis_major_image = (url + "images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg")

#Create URL string for Valles Marineris image

    valles_marineris_image = (url + "images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg")


#Create dictionary for Hemisphere title and URL string

    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "image_url": "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
        {"title": "Schiaparelli Hemisphere", "image_url": "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
        {"title": "Syrtis Major Hemisphere", "image_url": "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
        {"title": "Valles Marineris Hemisphere", "image_url": "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"}
                            
    ]


    return hemisphere_image_urls


    



