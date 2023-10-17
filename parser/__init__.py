from selenium.webdriver import Chrome, ChromeOptions, ChromeService
from . import helpers

options = ChromeOptions()
options.add_argument('--headless=new')

service = ChromeService(
    executable_path='./assets/chromedriver'
)

driver = Chrome(service=service, options=options)

from .functions import get_plates_info, get_plates_info_mtsbu