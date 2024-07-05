# Demoblaze QA Automation

## Project Overview

This project provides a comprehensive QA automation suite for testing functionalities of the [Demoblaze](https://demoblaze.com) website. The suite is developed using Python, Selenium, and Pytest, focusing on interactions with dropdowns, checkboxes, radio buttons, and forms. The aim is to ensure reliable performance and functionality of the web application across different scenarios and browsers.

## Features

- Automated browser interaction using Selenium WebDriver.
- Data-driven testing with dynamic JSON test data.
- Cross-browser testing capabilities.
- Detailed logging and reporting of test results.

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/zhorko/pytest-demoblaze.git
    cd pytest-demoblaze
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download and install the browser drivers:**
    - Download the appropriate drivers for the browsers you intend to test:
        - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Chrome.
        - [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox.
    - Ensure the drivers are in your system's PATH.

## Running the Tests

1. **Execute the test suite:**
    ```bash
    pytest tests/
    ```

2. **Run tests in a specific browser:**
    To run tests in a different browser, update the `browser` field in the `config.json` file. The available options are:

    - `Firefox`
    - `Chrome`
    - `Headless Chrome`
    - `Headless Firefox`

    Modify `config.json` to specify the desired browser, and then run the tests:
    ```json
    {
      "browser": "Chrome"  # or Firefox, Headless Chrome, Headless Firefox
    }
    ```

    Execute the tests with the configured browser:
    ```bash
    pytest tests/
    ```

3. **Generate a test report:**
    ```bash
    pytest tests/ --html-report=./report --title='TITLE'   
    ```

## Test Data

The test data is maintained in the `data/test_data.json` file, allowing for easy modification and extension of test scenarios. This file includes data for form fields, dropdown selections, and checkbox states.

## Key Files

- **`test_demoblaze.py`**: Contains the main test cases for interacting with the Demoblaze website.
- **`base_page.py`**: A base class for page objects, providing common methods and utilities.
- **`test_data.json`**: Holds the test data for data-driven testing.
- **`driver_setup.py`**: Configures and initializes the WebDriver for different browsers.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
