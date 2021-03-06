from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news, get_broadcaster_news

# Views
@main.route('/')
def index():

    '''
    View root page function that reutns the home new page (index) and its data
    '''
    # Getting top headline news
    top_headlines = get_news('country=us')
    print(top_headlines)
    title = 'View the Top News Stories'
    return render_template('index.html', title = title,headlines = top_headlines)

@main.route('/news_source/<string:news_id>')
def news_source(news_id):

    '''
    View news page function that returns the news broadcasters page and its data
    '''
    broadcaster_search="sources="+ news_id
    broadcasternews = get_broadcaster_news(broadcaster_search)
    print(broadcasternews)
    title = "News from your selected Broadcaster"
    return render_template('news_source.html',title=title,broadcasternews=broadcasternews)
