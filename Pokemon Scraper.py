from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
import logging
import json

# setup the configuration of logging
logging.basicConfig(filename='scraping_error.log', encoding='utf-8', level=logging.DEBUG)

class PokemonScraper:
    """
    Class to scrape Pokemon's data
    """
    def __init__(self, idx:int, headless=True):
        
        # In case headless
        opt = FirefoxOptions()
        if headless:    
            opt.add_argument('--headless')    
        # Driver
        self.driver = webdriver.Firefox(options=opt)        
        
        # Open the URL
        self.ROOT_DOMAIN = "https://www.pokemon.com/us/pokedex"
        self.idx = idx
        self.pokedex = {}
        
        
    def catch_error(func):
        """
        The decorator function to catch possible error on reading each attribute
        """
        def wrapper(self):
            try:
                func(self)
            except Exception as e:
                logging.error(e)
        return wrapper


    @catch_error
    def get_page(self):
        """
        Getting a pokemon deatil webpage by index
        """
        self.driver.get(f'{self.ROOT_DOMAIN}/{self.idx}')
        self.driver.implicitly_wait(5)

