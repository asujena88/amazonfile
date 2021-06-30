from selenium.webdriver.common.by import By


class Googlepage:

    def __init__(self, driver):
        self.driver = driver

        searchbar = (By.XPATH,"//div[2]/input[1]")
        searchbarclick = (By.XPATH, "//div[3]/center/input[1]")
        amazonclick = (By.XPATH, "//h3[contains(text(),'Amazon.in')]")

    def getsearchbar(self):
        return self.driver.find_element(*Googlepage.searchbar)

    def getsearchbarclick(self):
        return self.driver.find_element(*Googlepage.getsearchbarclick)

    def amazonclick(self):
        return self.driver.find_element(*Googlepage.amazonclick)