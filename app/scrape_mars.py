import pandas as pandas
import datetime as dt
from bs4 import BeautifulSoup as soup
from splinter import Browser

#browser = Browser('chrome', **executable_path, headless=False)

def scrape_all():
   browser = Browser('chrome', **executable_path, headless=False)
   news_title, news_paragraph = mars_news(browser)
   data = {
       'news_title': news_title,
       'news_paragraph': news_paragraph,
       'featured_image': featured_image(browser),
       'facts': mars_facts(),
       'hemispheres': hemispheres(browser),
       'last_modified': dt.datetime.now()     
           
   }
   
   browser.quit()
   return data

def mars_news(browser):
    pass

def featured_image(browser):
    pass

def mars_facts():
    pass

def hemispheres(browser):
    pass


