import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_News = News(1234,'BBC','Brexit happened because zyz',"https://ichef.bbci.co.uk/images/ic/1024x576/p08rdfbt.jpg"
,"https://www.cnn.com/2020/09/14/politics/election-2020-ballot-signature-mismatches/index.html"
,"2020-09-14T12:00:00Z"
,)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_News,News))


if __name__ == '__main__':
    unittest.main()
