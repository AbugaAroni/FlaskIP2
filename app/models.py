class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,broadcaster):
        self.id =id
        self.broadcaster = broadcaster

class NewsArticle(News):
    '''
    News class to define News Objects
    '''

    def __init__(self,id,broadcaster,title,description,image,URLsource,date):
        super().__init__( id, broadcaster)
        self.title = title
        self.description = description
        self.image = image
        self.URLsource = URLsource
        self.date = date
