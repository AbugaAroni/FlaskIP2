class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,broadcaster):
        self.id =id
        self.broadcaster = broadcaster

class NewsArticle:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,description,image,URLsource,date):
        self.title = title
        self.description = description
        self.image = image
        self.URLsource = URLsource
        self.date = date
