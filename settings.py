import os
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    # DEBUG = os.environ['DEBUG']
    DEVELOPMENT = os.getenv("ENVIRONMENT")
    # TESTING = os.environ['TESTING']
    MONGO_DBNAME = os.environ['MONGO_DBNAME']
    MONGO_URI = os.environ['MONGO_URI']
    # SECRET_KEY = os.environ['SECRET_KEY']
