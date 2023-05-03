import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()

        service_obj = Service("/Users/htnguyen/Downloads/chromedriver_mac_arm64/chromedriver")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name == "firefox":
        service_obj = Service("/Users/htnguyen/Downloads/geckodriver")
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver

    yield
    driver.quit()

    # return driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



