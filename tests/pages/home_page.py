from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Opens desired category
    def open_category(self, wait, cat_num: int):
        if cat_num > 1 and cat_num < 4:
            try:
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.CSS_SELECTOR,
                            "div[class='list-group'] a:nth-of-type("
                            + str(cat_num)
                            + ")",
                        )
                    )
                ).click()
            except exceptions.ElementNotInteractableException as e:
                print("{0} >> {1}".format("open_cat", e))
        else:
            return "No category with such index"

    # Opens product page
    def open_product(self, wait, name: str):
        try:
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(), '" + name + "')]")
                )
            ).click()
        except exceptions.ElementNotInteractableException as e:
            print("{0} >> {1}".format("product", e))

    # Returns object with specified text
    def get_search_products(self, wait, prod_name):
        try:
            cat_products = wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//a[contains(text(), '" + prod_name + "')]")
                )
            )
        except exceptions.ElementNotVisibleException as e:
            print("{0} >> {1}".format("cat_products", e))

        return cat_products
