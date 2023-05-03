from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage():

    shop = (By.XPATH, "//a[contains(@href, 'shop')]")
    email = (By.NAME, 'email')
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    exCheck = (By.ID, "exampleCheck1")
    radioBtn1 = (By.CSS_SELECTOR, "#inlineRadio1")

    submitBtn = (By.XPATH, "//input[@type='submit']")
    alertSuccess = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.exCheck)

    def getRadioBtn1(self):
        return self.driver.find_element(*HomePage.radioBtn1)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getSuccessAlert(self):
        return self.driver.find_element(*HomePage.alertSuccess)


