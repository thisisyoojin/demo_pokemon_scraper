from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
import logging
import json


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

        
        
    def exec_func(func):
        """
        The decorator function to catch possible errors when reading each attribute
        """
        def wrapper(self):
            try:
                func(self)
            except Exception as e:
                logging.error(e)
        return wrapper

