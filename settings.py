import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    ENV = os.getenv("ENVIRONMENT")

    @classmethod
    def for_actual_environment(cls):
        all_config_objects = [TestConfig, DevelopmentConfig]
        for config_object in all_config_objects:
            print(cls.ENV)
            if config_object.is_correct_for(cls.ENV):
                return config_object

        return DevelopmentConfig


class TestConfig(Config):
    TESTING = True
    ENV = os.getenv("ENVIRONMENT")
    MONGO_DBNAME = os.getenv('MONGO_TEST_DBNAME')
    MONGO_URI = os.getenv('MONGO_TEST_URI')

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == 'testing'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = os.getenv("ENVIRONMENT")
    MONGO_DBNAME = os.getenv('MONGO_DBNAME')
    MONGO_URI = os.getenv('MONGO_URI')

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == 'development'
