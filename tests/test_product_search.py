from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import pandas as pd
from time import sleep

def test_demon(_browser):

    wait = WebDriverWait(_browser, 10)
    url = "https://www.demoblaze.com"
    data_csv = pd.read_table("data/data.csv", delimiter =",", float_precision='round_trip') 

    _browser.get(url)
    _browser.maximize_window()

    try:
        open_cat = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='list-group'] a:nth-of-type(3)"))
        )
    except exceptions.ElementNotInteractableException as e:
        print('{0} >> {1}'.format('open_cat', e))
        
    open_cat.click()
    
    _browser.implicitly_wait(1)

    try:
        cat_laptop = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), '"+ data_csv.iloc[1, 1] +"')]"))
        )
    except exceptions.ElementNotVisibleException as e:
        print('{0} >> {1}'.format('cat_laptop', e))

    assert data_csv.iloc[1, 1] in cat_laptop.text