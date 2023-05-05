import logging
from scrapper_boilerplate import setSelenium, explicit_wait, mimic_user_input, load_code, dataToCSV
from selenium.webdriver.common.by import By

from database import mongoInsert


def login(driver, user_target):
    logging.info("Log in...")
    email_field = explicit_wait(driver, By.CSS_SELECTOR, 'input[type="email"]')
    password_field = explicit_wait(driver, By.CSS_SELECTOR, 'input[type="password"]')
    button_field = explicit_wait(driver, By.CSS_SELECTOR, 'button[type="submit"]')

    mimic_user_input(email_field, user_target)
    mimic_user_input(password_field, user_target)
    button_field.click()
    logging.info("Login successful!")


def extract_bets(page):

    logging.info(f"Extracting page {page}...")
    with setSelenium(headless=True, profile=True) as driver:
        driver.set_window_size(2000, 1900)
        driver.maximize_window()
        driver.get("https://www.historicosblaze.com/users/sign_in?locale=br")
        explicit_wait(driver, By.TAG_NAME, 'body')
        # login(driver, user_target)
        # navigation
        driver.get(f"https://www.historicosblaze.com/br/blaze/doubles?page={str(page)}")
        html = load_code(driver, full_page=True)
        container = html.select("#doubles div")

        for item in container:
            data = item.select_one("div.entry > div")
            if data:
                to_save = {
                    'color': data.select_one("span.color-table").text,
                    'number': data.select_one("span.number-table").text,
                    'minute': data.select_one("span.minute-table").text,
                    'date': data.select_one("span.date-table").text,
                    'redbets': data.select_one("span.redbets-table").text,
                    'whitebets': data.select_one("span.whitebets-table").text,
                    'blackbets': data.select_one("span.blackbets-table").text,
                    'seed': data.select_one("span.seed-table").text
                }
                
                logging.info(to_save)
                mongoInsert([to_save])
