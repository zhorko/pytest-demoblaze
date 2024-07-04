from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import pandas as pd
from time import sleep

def test_demon(_browser):

    wait = WebDriverWait(_browser, 10)
    data_csv = {}
    url = "https://www.demoblaze.com"


    _browser.get(url)
    _browser.maximize_window()

    data_csv = pd.read_table("data/data.csv", delimiter =",", float_precision='round_trip') 

    try:
        open_cat = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='list-group'] a:nth-of-type(2)"))
        ).click()
    except exceptions.ElementNotInteractableException as e:
        print('{0} >> {1}'.format('open_cat', e))

    _browser.implicitly_wait(1)

    try:
        item_name = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '"+ data_csv.iloc[0, 1] +"')]"))
        ).click()
    except exceptions.ElementNotInteractableException as e:
        print('{0} >> {1}'.format('product', e))

    try:
        wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success"))
        ).click()
    except exceptions.ElementNotInteractableException as e:
        print('{0} >> {1}'.format('add_to_cart', e))

    try:
        wait.until(EC.alert_is_present())
        alert_msg = _browser.switch_to.alert
        alert_msg.accept()
    except exceptions.NoAlertPresentException as e:
        print('{0} >> {1}'.format('cat_laptop', e))

    try:
        wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='cartur']"))
        ).click()
    except exceptions.ElementNotVisibleException as e:
        print('{0} >> {1}'.format('cart_btn', e))

    try:
        cart_table = wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tr.success td"))
        )
    except exceptions.ElementNotVisibleException as e:
        print('{0} >> {1}'.format('cart_table', e))
    
    assert str(data_csv.iloc[0, 2].astype(int)) in cart_table[2].text
    print("check price - SUCCESS")
    
    assert data_csv.iloc[0, 1] in cart_table[1].text
    print("check name - SUCCESS")
    
    cart_table[3].find_element(By.CSS_SELECTOR, "a").click()

    _browser.implicitly_wait(1)

    try:
        cart_empty = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tr.success td"))
        )
        el_found = True
    except exceptions.TimeoutException as e:
        print('{0} >> {1}'.format('cart_empty', e))
        el_found = False
        pass

    print(f"{el_found = }")

    # '1' - just headers, thereforth its empty
    assert el_found
    print("check emptyness - SUCCESS")