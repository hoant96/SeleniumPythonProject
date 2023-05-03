import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getEmail().send_keys(getData["email"])
        log.info("email is " + getData["email"])
        homePage.getPassword().send_keys("123456")
        homePage.getCheckbox().click()

        homePage.getName().send_keys(getData["name"])
        log.info("name is " + getData["name"])
        homePage.getRadioBtn1().click()

        # dropdown
        self.selectOPtionByText(homePage.getGender(), getData["gender"])
        log.info("gender is " + getData["gender"])
        homePage.getSubmitBtn().click()
        message = homePage.getSuccessAlert().text

        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getData(self, request):
        return request.param



