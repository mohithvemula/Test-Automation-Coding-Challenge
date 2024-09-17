from selenium.webdriver.common.by import By
from base_page import BasePage

class BetSlipPage(BasePage):
    # const variables; locators
    HORSE_BET_1 = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div/div/button/div/div/div/span/div')
    HORSE_BET_2 = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div[3]/div/div/div[2]/div/div/div/div/button/div/div/div/span/div')

    HORSE_BET_1_TEXT = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div/div/button/div/div/div/span/div/div/div/span')
    HORSE_BET_1_NAME = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/span[1]')
    HORSE_BET_2_TEXT = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div[3]/div/div/div[2]/div/div/div/div/button/div/div/div/span/div/div/div/span')
    HORSE_BET_2_NAME = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div[3]/div/div/div[1]/div[1]/span[1]')

    CLOSE_BETS_HEADER_BUTTON = (By.CSS_SELECTOR, '[data-automation-id="betslip-header-hide"]')
    OPEN_BETS_HEADER_BUTTON = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[1]/div/header/div[2]/button')

    HEADER_FIRST_BET_TEXT = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[4]/div/div/span/div/div[1]/div/div/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div[3]/div[3]/div/span')
    HEADER_FIRST_BET_NAME = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[4]/div/div/span/div/div[1]/div/div/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/span')
    HEADER_SECOND_BET_TEXT = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[4]/div/div/span/div/div[1]/div/div/div[1]/section/div/div[2]/div/div[3]/div[1]/div/div[3]/div[3]/div/div/div[2]/span')
    HEADER_SECOND_BET_NAME = (By.XPATH, '//*[@id="base"]/div/div[2]/div/div[4]/div/div/span/div/div[1]/div/div/div[1]/section/div/div[2]/div/div[3]/div[1]/div/div[3]/div[2]/div[1]/div/span')

    def add_bet_1(self):
        self.click(self.HORSE_BET_1)

    def get_bet_1_text(self):  # used for verify/assert methods
        return self.get_element_text(self.HORSE_BET_1_NAME)

    def add_bet_2(self):
        self.click(self.HORSE_BET_2)

    def get_bet_2_text(self):
        return self.get_element_text(self.HORSE_BET_2_NAME)

    def close_betslip_header(self): # header opens automatically after selecting first bet
        self.click(self.CLOSE_BETS_HEADER_BUTTON)

    def open_betslip_header(self):
        self.click(self.OPEN_BETS_HEADER_BUTTON)

    def get_first_bet_text_from_header(self):
        return self.get_element_text(self.HEADER_FIRST_BET_NAME)

    def get_second_bet_text_from_header(self):
        return self.get_element_text(self.HEADER_SECOND_BET_NAME)