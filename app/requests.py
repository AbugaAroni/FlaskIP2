from app import app
import urllib.request,json
from .models import news

News1 = news.News
NewsArticle2 = news.NewsArticle

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
        news_list: A list of dictionaries that contain news details

    Returns :
        newz_results: A list of news objects
    '''
    newz_results = []
    for source_info in newz_list:
        #source parses info from source{}

        source = source_info.get('source')

        id = source.get('id')
        broadcaster = source.get('name')
        title = source_info.get('title')
        description = source_info.get('description')
        image = source_info.get('urlToImage')
        URLsource = source_info.get('url')
        date = source_info.get('publishedAt')

        if  broadcaster:

            news_object = NewsArticle2(title,description,image,URLsource,date)
            newz_results.append(news_object)
            news_source_object = News1(id,broadcaster)
            newz_results.append(news_source_object)


    return newz_results

def get_broadcaster_news(id):
    get_broadcaster_news_url = base_url.format(id,apikey)

    with urllib.request.urlopen(get_broadcaster_news_url) as url:
        broadcaster_news_details_data = url.read()
        broadcaster_news_details_data_response = json.loads(broadcaster_news_details_data)

        bdnd_object = None

        if broadcaster_news_details_data_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results
