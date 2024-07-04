from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

from pages.product_page import ProductPage
from pages.home_page import HomePage


def test_product_details(_browser):

    wait = WebDriverWait(_browser, 10)
    data_csv = {}
    url = "https://www.demoblaze.com"

    _browser.get(url)
    _browser.maximize_window()

    data_csv = pd.read_table("data/data.csv",
                            delimiter =",",
                            float_precision='round_trip')

    # initializers
    home_page = HomePage(_browser)
    prod_page = ProductPage(_browser)

    home_page.open_category(wait, 2)
    home_page.open_product(wait, data_csv.iloc[0, 1])

    prod_details = prod_page.get_product_details()

    # Verify product details
    assert data_csv.iloc[0, 3] in prod_details[1]
    assert str(data_csv.iloc[0, 2].astype(int)) in prod_details[2]
    assert data_csv.iloc[0, 1] in prod_details[0]