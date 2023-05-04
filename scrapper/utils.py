import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_until_clicable(driver, by_tag, css_selector, timeout=30):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable((by_tag, css_selector)))
    return element


def js_click(driver, element):
    driver.execute_script("arguments[0].click();", element)


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"Execution time: {end - start} seconds")
        return result
    return wrapper