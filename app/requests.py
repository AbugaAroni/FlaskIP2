from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
apikey = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(categories):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(categories,apikey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(newz_list):
    '''
    Function  that processes the news result and transforms it to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        newz_results: A list of movie objects
    '''
    newz_results = []
    for news_item in newz_list:
        id = news_item.get('source.id')
        title = news_item.get('title')
        broadcaster = news_item.get('source.name')
        description = news_item.get('description')
        image = news_item.get('urlToImage')
        URLsource = news_item.get('url')
        date = news_item.get('publishedAt')

        if image:
            news_object = News(id,title,broadcaster,description,image,URLsource,date)
            newz_results.append(news_object)

    return newz_results
