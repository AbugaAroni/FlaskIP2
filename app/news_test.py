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


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_News.id,1234)
        self.assertEqual(self.new_News.title,"BBC")
        self.assertEqual(self.new_News.description,"Brexit happened because zyz")
        self.assertEqual(self.new_News.image,"https://ichef.bbci.co.uk/images/ic/1024x576/p08rdfbt.jpg")
        self.assertEqual(self.new_News.source,"https://www.cnn.com/2020/09/14/politics/election-2020-ballot-signature-mismatches/index.html")
        self.assertEqual(self.new_News.date,"2020-09-14T12:00:00Z")


if __name__ == '__main__':
    unittest.main()
