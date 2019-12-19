# Dependencies
import requests
#from config import api_key
import json
from splinter import Browser

def init_browser():
    # Setting up windows browser with chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape(target_city):
    browser = init_browser()

    value_data = {}

    api_key = "eeea2890108b4260a41918a9ad781cec"

    target_url = (f'https://api.opencagedata.com/geocode/v1/json?q={target_city}&key={api_key}')

    latlongdata = requests.get(target_url).json()

    longvalue = latlongdata['results'][0]['geometry']['lng']
    latvalue = latlongdata['results'][0]['geometry']['lat']
    value_data['long'] = longvalue
    value_data['lat'] = latvalue
    return value_data

if __name__ == "__main__":
    scrape()