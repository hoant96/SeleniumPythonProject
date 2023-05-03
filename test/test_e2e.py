import logging

from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Getting all card titles.......")
        products = checkoutPage.getCardTitles()
        i = -1
        for product in products:
            i = i+1
            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getCardButtons()[i].click()

        checkoutPage.checkout().click()
        confirmPage = checkoutPage.getConfirmPage()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
        sucText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Received message is " + sucText)
        assert "Success! Thank you" in sucText







