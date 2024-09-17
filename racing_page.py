from selenium.webdriver.common.by import By
from base_page import BasePage

class RacingPage(BasePage):
    # define const variables like locators
    RACING_TAB = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div/div/button[1]')
    NEXT_TO_JUMP_FIRST_CARD = (By.CSS_SELECTOR, '[data-automation-id="group-1-carousel-1-body-container-cell-1"]')

    def navigate_to_racing(self):
        self.click(self.RACING_TAB)
    
    def select_first_race_card(self):
        self.click(self.NEXT_TO_JUMP_FIRST_CARD)
