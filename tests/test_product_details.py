from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

import pandas as pd
from time import sleep

def test_demon(_browser):

    wait = WebDriverWait(_browser, 10)
    data_csv = {}
    url = "https://www.demoblaze.com"
    name = "MacBook air"


    _browser.get(url)
    _browser.maximize_window()

    data_csv = pd.read_table("data/data.csv", delimiter =",", float_precision='round_trip') 

    #print(f"{data_csv}")

    # with open ("data/data.csv", 'r') as data:
    #     reader = csv.DictReader(data)
    #     for line in reader:
    #         data_csv.update(line)
    #         # for key, value in data_csv.items():
    #         #     print(f"{key}: {value}")

    try:
        open_cat = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='list-group'] a:nth-of-type(2)"))
        )
    except exceptions.ElementNotInteractableException as e:
        print('{0} >> {1}'.format('open_cat', e))
    
    #print(f"{open_cat.text = }")
    
    open_cat.click()
    
    sleep(1)

    try:
        wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='tbodyid'] div:nth-of-type(1) .hrefch"))
        ).click()
    except exceptions.ElementNotVisibleException as e:
        print('{0} >> {1}'.format('cat_laptop', e))

    try:
        item_name = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='tbodyid'] .name"))
        )
    except exceptions.ElementNotVisibleException as e:
        print('{0} >> {1}'.format('cat_laptop', e))

    #print(f"{item_name.text = }")

    try:
        item_desc = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='tbodyid'] div[id='more-information'] p"))
        )
    except exceptions.ElementNotVisibleException as e:
        print('{0} >> {1}'.format('cat_laptop', e))

    #print(f"{item_desc.text = }")

    try:
        item_price = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='tbodyid'] h3[class='price-container']"))
        )
    except exceptions.ElementNotVisibleException as e:
        print('{0} >> {1}'.format('cat_laptop', e))

    #print(f"{item_price.text = }")
    #item_price = item_price.text.replace(" *includes tax", "")

    assert data_csv.iloc[0, 3] in item_desc.text
    assert str(data_csv.iloc[0, 2].astype(int)) in item_price.text
    assert data_csv.iloc[0, 1] in item_name.text

    #sleep(300)