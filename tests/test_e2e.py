import importlib
import pytest
from Testdata import GooglePageData
from conftest import driver
from pageObject.AmazonHomePage import Amazonpage
from utilities.BaseClass import BaseClass
from pageObject.GooglePage import Googlepage



class TestOne(BaseClass):

    def test_e2e(self, getData):
        log = self.getLogger()
        googlepage = Googlepage(self.driver)
        #amazonpage = Amazonpage(self.driver)

        Googlepage.getsearchbar().send_keys(getData["website"])
        self.driver.find_element_by_xpath("//div[2]/input[1]").send_keys("amazon.in")
        Googlepage.getsearchbarclick().click()
        self.driver.find_element_by_xpath("//div[3]/center/input[1]").click()
        Googlepage.amazonclick().click()

        Amazonpage.getamazonsearchbar().send_keys(getData["amazonsearch"])
        Amazonpage.getamazonsubmitbutton().click()
        Amazonpage.getmobilesearch().click()

        a = driver.window_handles
        driver.switch_to.window(a[1])

        desc = Amazonpage.getmobiledesc().text
        print(desc)

        Amazonpage.getaddtocart().click()


    def test_e2e(self, getData):
        log = self.getLogger()
        googlepage = Googlepage(self.driver)


    @pytest.fixture(params=GooglePageData.GooglePageData.getTestData("Testcase1"))
    def getData(self, request):
        return (request)

