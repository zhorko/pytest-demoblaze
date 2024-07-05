from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

from pages.home_page import HomePage


def test_demon(_browser):

    wait = WebDriverWait(_browser, 10)
    url = "https://www.demoblaze.com"
    data_csv = pd.read_table(
        "data/data.csv", delimiter=",", float_precision="round_trip"
    )

    _browser.get(url)
    _browser.maximize_window()

    # initializers
    home_page = HomePage(_browser)

    home_page.open_category(wait, 3)

    cat_prod = home_page.get_search_products(wait, data_csv.iloc[1, 1])

    assert data_csv.iloc[1, 1] in cat_prod.text
