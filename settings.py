import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    ENV = os.getenv("ENVIRONMENT")

    @classmethod
    def for_actual_environment(cls):
        all_config_objects = [TestConfig, DevelopmentConfig, ProductionConfig]
        for config_object in all_config_objects:
            print(cls.ENV)
            if config_object.is_correct_for(cls.ENV):
                return config_object

        return DevelopmentConfig

    @classmethod
    def name(cls):
        raise NotImplementedError('Subclass responsibility')

    @classmethod
    def need_authorization(cls):
        raise NotImplementedError('Subclass responsibility')

    @classmethod
    def should_handle_errors(cls):
        raise NotImplementedError('Subclass responsibility')


class TestConfig(Config):
    NAME = 'testing'
    TESTING = True
    ENV = os.getenv("ENVIRONMENT")
    MONGO_DBNAME = os.getenv('MONGO_TEST_DBNAME')
    MONGO_URI = os.getenv('MONGO_TEST_URI')

    @classmethod
    def name(cls):
        return cls.NAME

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == cls.name()

    @classmethod
    def need_authorization(cls):
        return False

    @classmethod
    def should_handle_errors(cls):
        return False


class DevelopmentConfig(Config):
    NAME = 'development'
    DEBUG = True
    ENV = os.getenv("ENVIRONMENT")
    MONGO_DBNAME = os.getenv('MONGO_DBNAME')
    MONGO_URI = os.getenv('MONGO_URI')
    TOKEN = os.getenv('TOKEN')

    @classmethod
    def name(cls):
        return cls.NAME

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == cls.name()

    @classmethod
    def token(cls):
        return cls.TOKEN

    @classmethod
    def need_authorization(cls):
        return True

    @classmethod
    def should_handle_errors(cls):
        return False


class ProductionConfig(Config):
    NAME = 'production'
    DEBUG = True
    ENV = os.getenv("ENVIRONMENT")
    MONGO_DBNAME = os.getenv('MONGO_DBNAME')
    MONGO_URI = os.getenv('MONGO_URI')
    TOKEN = os.getenv('TOKEN')

    @classmethod
    def name(cls):
        return cls.NAME

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == cls.name()

    @classmethod
    def token(cls):
        return cls.TOKEN

    @classmethod
    def need_authorization(cls):
        return True

    @classmethod
    def should_handle_errors(cls):
        return True
