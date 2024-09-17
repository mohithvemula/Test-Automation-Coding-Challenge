from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from racing_page import RacingPage
from betslip_page import BetSlipPage
import time

# init driver
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

# path to local chromedriver TODO remove if driver already added to PATH
service = Service(executable_path=r"driver\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_window_size(420, 800) # set width to 420px as required
driver.get("https://www.sportsbet.com.au")

try:
    # Initialize page objects
    racing_page = RacingPage(driver)
    betslip_page = BetSlipPage(driver)

    # navigate and perform actions
    racing_page.navigate_to_racing()
    racing_page.select_first_race_card()

    # get element text
    first_bet_text = betslip_page.get_bet_1_text()

    # add first bet
    betslip_page.add_bet_1()

    # close bets header
    betslip_page.close_betslip_header()

    # get element text
    second_bet_text = betslip_page.get_bet_2_text()

    # add second bet
    betslip_page.add_bet_2()

    # open bets header
    betslip_page.open_betslip_header()

    # get element texts from both bets
    first_bet_name = betslip_page.get_first_bet_text_from_header()[:-4]
    second_bet_name = betslip_page.get_second_bet_text_from_header()[:-4]

    # assert that both names are the same (from the header and initial bet placing element)    
    # verification
    assert first_bet_name == first_bet_text, f"Expected {first_bet_text} but got {first_bet_name}"
    assert second_bet_name == second_bet_text, f"Expected {second_bet_text} but got {second_bet_name}"

    print("All tests have passed")

except AssertionError as e:
    print(f"Verification Failed: {e}")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    driver.quit()