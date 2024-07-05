from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.home_page import HomePage


def test_cart_details(_browser):

    wait = WebDriverWait(_browser, 10)
    URL = "https://www.demoblaze.com"

    _browser.get(URL)
    _browser.maximize_window()

    data_csv = pd.read_table(
        "data/data.csv", delimiter=",", float_precision="round_trip"
    )

    # initializers
    home_page = HomePage(_browser)
    cart_page = CartPage(_browser)
    prod_page = ProductPage(_browser)

    home_page.open_category(wait, 2)

    home_page.open_product(wait, data_csv.iloc[0, 1])

    prod_page.buy_product(wait)
    prod_page.open_cart(wait)

    cart_table = cart_page.get_product_details(wait)

    assert str(data_csv.iloc[0, 2].astype(int)) in cart_table[1].text
    assert data_csv.iloc[0, 1] in cart_table[0].text


def test_cart_delete(_browser):

    wait = WebDriverWait(_browser, 10)
    URL = "https://www.demoblaze.com"

    _browser.get(URL)
    _browser.maximize_window()

    data_csv = pd.read_table(
        "data/data.csv", delimiter=",", float_precision="round_trip"
    )

    # initializers
    home_page = HomePage(_browser)
    cart_page = CartPage(_browser)
    prod_page = ProductPage(_browser)

    home_page.open_category(wait, 2)

    home_page.open_product(wait, data_csv.iloc[0, 1])

    prod_page.buy_product(wait)
    prod_page.open_cart(wait)

    cart_page.delete_product(wait)

    assert cart_page.verify_empty(wait)
