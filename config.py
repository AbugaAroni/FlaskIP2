import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='http://newsapi.org/v2/top-headlines?{}&apikey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

#    http://newsapi.org/v2/top-headlines?country=us&apiKey=d9eecd93059443ebb15b5d47f09717fd
#    http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=d9eecd93059443ebb15b5d47f09717fd

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
