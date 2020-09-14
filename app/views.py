from flask import render_template
from app import app
from .requests import get_news

# views
@app.route('/')
def index():

    '''
    View root page function that reutns the home new page (index) and its data
    '''
    # Getting top headline news
    top_headlines = get_news('country=us')
    print(top_headlines)
    title = 'View the Top News Stories'
    return render_template('index.html', title = title,headlines = top_headlines)

@app.route('/news_source/<int:news_id>')
def news_source(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news_source.html',id = news_id)
