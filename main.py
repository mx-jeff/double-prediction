import sys
from prediction import prediction
from scrapper import scrape


def main():
    args = sys.argv[1]

    if args == "prediction":
        prediction()

    elif args == "scraper":
        scrape()


if __name__ == "__main__":
    main()