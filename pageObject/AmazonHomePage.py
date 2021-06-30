from selenium.webdriver.common.by import By


class Amazonpage:

    def __init__(self, driver):
        self.driver = driver

        amazonsearchbar = (By.ID, "twotabsearchtextbox")
        amazonsubmitbutton = (By.XPATH, "//input[@id='nav-search-submit-button")
        mobilesearch = (By.XPATH, "//span[contains(text(),'Samsung Galaxy M42 5G ')]")
        mobiledesc = (By.XPATH, "'//div[@id='featurebullets_feature_div']/div[@id='feature-bullets']/ul[1]'")
        addtocart = (By.ID, "add-to-cart-button")


    def getamazonsearchbar(self):
        return self.driver.find_element(*Amazonpage.getamazonsearchbar)

    def getamazonsubmitbutton(self):
        return self.driver.find_element(*Amazonpage.getamazonsubmitbutton)

    def getmobilesearch(self):
        return self.driver.find_element(*Amazonpage.getmobilesearch())

    def getmobiledesc(self):
        return self.driver.find_element(*Amazonpage.getmobiledesc())

    def getaddtocart(self):
        return self.driver.find_element(*Amazonpage.getaddtocart())

