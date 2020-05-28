from selenium import webdriver
import allure
import pytest

class TestHRM:
    def test_logo(self):
        self.driver = webdriver.Chrome(executable_path = "C:/Users/subhaku2/chromedriver.exe" )

        url= "https://www.naukri.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        status = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/a/img').is_displayed()

        if status == True:
            assert True
        else:
            assert False
        self.driver.close()
