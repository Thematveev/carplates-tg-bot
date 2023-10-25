from selenium.webdriver import Chrome, ChromeOptions, ChromeService
from . import helpers

options = ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = Chrome(options=options)

from .functions import get_plates_info, get_plates_info_mtsbu
