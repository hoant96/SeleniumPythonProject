from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    cardContent = (By.XPATH, "//div[@class = 'card h-100']")
    cartTitle = (By.CSS_SELECTOR, ".card-title a")
    cardButton = (By.CSS_SELECTOR, ".card-footer button")
    checkoutItems = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutButton = (By.XPATH, "//button[@class = 'btn btn-success']")


    def __init__(self, driver):
        self.driver = driver

    def getCardContent(self):
        return self.driver.find_elements(*CheckoutPage.cardContent)

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cartTitle)

    def getCardButtons(self):
        return self.driver.find_elements(*CheckoutPage.cardButton)

    def checkout(self):
        return self.driver.find_element(*CheckoutPage.checkoutItems)

    def getConfirmPage(self):
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        confirmPage  = ConfirmPage(self.driver)
        return confirmPage
