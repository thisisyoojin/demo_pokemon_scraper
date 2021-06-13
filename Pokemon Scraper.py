from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
import json

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
        pk = Pokemon(**{'id':'#001'})
        
        