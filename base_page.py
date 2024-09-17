from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# base class for common actions like clicking elements and asserting text on elements
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # default timeout of 10 seconds

    def click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def get_element_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text if element.text else element.get_attribute("innerText")

    # def get_element_text(self, by_locator):
    #     element = self.driver.find_element(by_locator)
    #     return element.text