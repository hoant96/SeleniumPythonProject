from selenium.webdriver.common.by import By


class ConfirmPage:

    country = (By.ID, "country")
    countryLink = (By.LINK_TEXT, "India")
    checkCondition = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "[type = 'submit']")
    alertSuccess = (By.CLASS_NAME, "alert-success")


    def __init__(self, driver):
        self.driver = driver
