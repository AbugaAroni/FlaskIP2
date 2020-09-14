class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,broadcaster,description,image,URLsource,date):
        self.id =id
        self.title = title
        self.broadcaster = broadcaster
        self.description = description
        self.image = image
        self.URLsource = URLsource
        self.date = date
