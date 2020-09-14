from flask import render_template
from app import app

# views
@app.route('/')
def index():

    '''
    View root page function that reutns the home new page (index) and its data
    '''

    message = 'Hello World message'
    return render_template('index.html', message=message)

@app.route('/news_source/<int:news_id>')
def news_source(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news_source.html',id = news_id)
