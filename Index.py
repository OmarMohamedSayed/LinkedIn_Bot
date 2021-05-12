from selenium import webdriver
# from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, WebDriverException
# from selenium.webdriver import DesiredCapabilities
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

from conf import EMAIL,PASSWORD,DRIVER_PATH
"""
number of seconds used to wait the web page's loading.
"""
WAIT_TIMEOUT = 10


def get_by_xpath(driver, xpath, wait_timeout=None):
    """
    Get a web element through the xpath passed by performing a Wait on it.
    :param driver: Selenium web driver to use.
    :param xpath: xpath to use.
    :param wait_timeout: optional amounts of seconds before TimeoutException is raised, default WAIT_TIMEOUT is used otherwise.
    :return: The web element.
    """
    if wait_timeout is None:
        wait_timeout = WAIT_TIMEOUT
    return WebDriverWait(driver, wait_timeout).until(
        ec.presence_of_element_located(
            (By.XPATH, xpath)
        ))


def login(driver, LINKEDIN_LOGIN_URL):
    """
    Logs in Linkedin.
    :param driver: The yet open selenium webdriver.
    :return: Nothing
    """
    driver.get(LINKEDIN_LOGIN_URL)

    print('Searching for the Login btn')
    get_by_xpath(driver, '//*[@id="username"]').send_keys(EMAIL)

    print('Searching for the password btn')
    get_by_xpath(driver, '//*[@id="password"]').send_keys(PASSWORD)

    print('Searching for the submit')
    get_by_xpath(driver, '//*[@type="submit"]').click()

def cograts(driver):
    """
    Open Notifications,
    Scroll to get more congrats
    Collect all Users need to congrats
    Finally open chats and congrats all  
    :param driver: The yet open selenium webdriver.
    :return: Nothing
    """
    driver.execute_script("window.scrollTo(0, 1000000);")
    time.sleep(WAIT_TIMEOUT)
    
    users = driver.find_elements(By.XPATH,'//button[contains(@aria-label,"Say congrats")]')
    
    print(f'length of Users: {len(users)}')
    
    for user in users:
        user.click()
        get_by_xpath(driver,'//button[@class="msg-form__send-button artdeco-button artdeco-button--1"]').click()
        get_by_xpath(driver,'//button[@class="msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]').click()
        time.sleep(1)
    
if __name__ == "__main__":
    
    LINKEDIN_LOGIN_URL = 'https://www.linkedin.com/login'
    driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    
    login(driver,LINKEDIN_LOGIN_URL)
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(ec.title_is('Feed | LinkedIn'))
    print("loggin success")
    get_by_xpath(driver,"//*[@data-test-global-nav-link='notifications']").click()
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(ec.title_is('Notifications | LinkedIn'))
    print("Notifications")
    time.sleep(WAIT_TIMEOUT)
    cograts(driver)
    print("Success congrats")