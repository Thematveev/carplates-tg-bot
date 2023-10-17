from . import driver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions




def get_plates_info(plates: str):
    driver.get("https://baza-gai.com.ua/")
    WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.ID, 'number')))
    search_bar = driver.find_element(By.ID, 'number')
    search_button = driver.find_element(By.XPATH, '//*[@id="container-main"]/form/div[1]/div/button')
    search_bar.send_keys(plates)
    search_button.click()

    data_pack = {
        'plates': plates,
        'model': None,
        'vin': None,
        'year': None,
        'specs': None
    }

    try:
        vin = driver.find_element(By.CLASS_NAME, 'vin-code-erased').get_attribute('data-full')
        data_pack['vin'] = vin
    except NoSuchElementException:
        pass

    try:
        model = driver.find_element(By.CLASS_NAME, 'plate-model-card__content-title').text
        data_pack['model'] = model
    except NoSuchElementException:
        pass

    try:
        year = driver.find_element(By.CLASS_NAME, 'plate-model-card__content-date-model').text
        data_pack['year'] = year
    except NoSuchElementException:
        pass

    try:
        specs = driver.find_element(By.XPATH, '//*[@id="container-main"]/div[1]/div/div/div/div[2]/ul/li[3]/span/span').text
        data_pack['specs'] = specs
    except NoSuchElementException:
        pass

    return data_pack




# mtsbu
def get_plates_info_mtsbu(plates: str):
    driver.get('https://policy-web.mtsbu.ua/')
    plates_input = driver.find_element(By.XPATH, '//*[@id="RegNoModel_PlateNumber"]')
    plates_input.send_keys(plates)

    search_button = driver.find_element(By.XPATH, '//*[@id="submitBtn"]')
    search_button.click()

    data_pack = {
        'plates': plates,
        'model': None,
        'vin': None,
        'year': None,
        'specs': None
    }

    try:
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[18]')))
        vin = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[18]').text
        data_pack['vin'] = vin
    except NoSuchElementException:
        pass
    except TimeoutException:
        pass

    return data_pack





