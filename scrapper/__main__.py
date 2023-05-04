import logging
import os
import concurrent.futures

from time import sleep
from dotenv import load_dotenv

from scrapper_boilerplate import init_log
from core import extract_bets
from utils import time_it


init_log()
load_dotenv()
user_target = os.getenv("user")


@time_it
def main():

    logging.info("Starting...")
    pages = range(1, 1000)
    with concurrent.futures.ProcessPoolExecutor(max_workers=30) as executor:
        executor.map(extract_bets, pages)
    # for page in pages:
    #     extract_bets(page)

    logging.info("Done!")


if __name__ == '__main__':
    main()
