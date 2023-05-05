import os


DATABASE="blaze"
TABLE="double"
mongo_db = os.getenv('MONGO_URI')
PAGE_LIMIT= 10000
MAX_WORKERS = 40