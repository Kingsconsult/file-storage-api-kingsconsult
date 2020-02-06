import dj_database_url
from decouple import config


class DB:
    @classmethod
    def config(cls, debug):
        return cls.development() if debug else cls.production()

    @classmethod
    def production(cls):
        return {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'file-storage',
                'HOST': 'db:27017',
            }
        }

    @classmethod
    def development(cls):
        return {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'file-storage',
                'HOST': 'db:27017',
            }
        }