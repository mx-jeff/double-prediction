import logging
import os
import concurrent.futures

from time import sleep
from dotenv import load_dotenv

from scrapper_boilerplate import init_log
from scrapper.core import extract_bets
from scrapper.utils import time_it

from config import PAGE_LIMIT, MAX_WORKERS

init_log()
load_dotenv()
user_target = os.getenv("user")


@time_it
def scrape():

    logging.info("Starting...")
    pages = range(1, PAGE_LIMIT)
    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(extract_bets, pages)
    # for page in pages:
    #     extract_bets(page)

    logging.info("Done!")
