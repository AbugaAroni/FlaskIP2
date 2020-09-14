class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='http://newsapi.org/v2/top-headlines?{}&apikey={}'

#    http://newsapi.org/v2/top-headlines?country=us&apiKey=d9eecd93059443ebb15b5d47f09717fd
#    http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=d9eecd93059443ebb15b5d47f09717fd

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
