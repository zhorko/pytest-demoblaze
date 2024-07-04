from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    # Adds product to cart
    def buy_product(self, wait):
        try:
            wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success"))
            ).click()
        except exceptions.ElementNotInteractableException as e:
            print('{0} >> {1}'.format('add_to_cart', e))
    
    # Opens cart page
    def open_cart(self, wait):
        try:
            wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='cartur']"))
            ).click()
        except exceptions.ElementNotVisibleException as e:
            print('{0} >> {1}'.format('cart_btn', e))
    
    # Returns product details
    def get_product_details(self):
        prod_name = self.driver.find_element(By.CSS_SELECTOR, "div[id='tbodyid'] .name")
        prod_desc = self.driver.find_element(By.CSS_SELECTOR, "div[id='tbodyid'] div[id='more-information'] p")
        prod_price = self.driver.find_element(By.CSS_SELECTOR, "div[id='tbodyid'] h3[class='price-container']")
    
        return prod_name.text, prod_desc.text, prod_price.text