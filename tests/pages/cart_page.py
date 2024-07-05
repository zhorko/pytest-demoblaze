from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    # Returns table with 'price', 'name' and 'delete' button
    def __get_table(self, wait):
        try:
            cart_table = wait.until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "tr.success td")
                )
            )
        except exceptions.ElementNotVisibleException as e:
            print("{0} >> {1}".format("cart_table", e))

        return cart_table

    # Returns product 'price' and 'name' in a list
    def get_product_details(self, wait):
        cart_table = self.__get_table(wait)

        return [cart_table[1], cart_table[2]]

    # Deletes product from cart
    def delete_product(self, wait):
        cart_table = self.__get_table(wait)
        cart_table[3].find_element(By.CSS_SELECTOR, "a").click()

    def verify_empty(self, wait):
        try:
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "tr.success td"))
            )
            el_found = True
        except exceptions.TimeoutException as e:
            print("{0} >> {1}".format("cart_empty", e))
            el_found = False

        return el_found
