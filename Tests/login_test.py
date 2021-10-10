from selenium import webdriver
import pytest
import allure

from Pages.loginpage import loginpage
from Pages.homepage import Homepage
from utilis import utilis as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = loginpage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.enter_login()

        #1driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
        #driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
        #driver.find_element_by_xpath("//*[@id='btnLogin']").click()

    def test_logout(self):
        try:
           driver = self.driver
           homepage = Homepage(driver)
           homepage.click_welcome()
           homepage.click_logout()
           x = driver.title
           assert x == "abc"


        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("there was an exception")
            raise
        else:
            print("no exception occurrd")
        finally:
            print("i am inside finally block")




        #driver.find_element_by_id("welcome").click()
        #driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[3]/a").click()

       # driver.close()
       # driver.quit()
       # print("Test Completed")



