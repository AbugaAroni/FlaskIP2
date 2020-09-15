import unittest
from models import news
News1 = news.News
News2 = news.NewsArticle

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_News1 = News1(1234,'BBC')
        self.new_News2 = News2(1234,'BBC','Title of the story','Brexit happened because zyz',"https://ichef.bbci.co.uk/images/ic/1024x576/p08rdfbt.jpg"
            ,"https://www.cnn.com/2020/09/14/politics/election-2020-ballot-signature-mismatches/index.html"
            ,"2020-09-14T12:00:00Z"
            ,)

    def test_instance(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertTrue(isinstance(self.new_News1,News1))
        self.assertTrue(isinstance(self.new_News2,News2))


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_News1.id,1234)
        self.assertEqual(self.new_News1.broadcaster,"BBC")
        self.assertEqual(self.new_News2.title,"Title of the story")
        self.assertEqual(self.new_News2.description,"Brexit happened because zyz")
        self.assertEqual(self.new_News2.image,"https://ichef.bbci.co.uk/images/ic/1024x576/p08rdfbt.jpg")
        self.assertEqual(self.new_News2.URLsource,"https://www.cnn.com/2020/09/14/politics/election-2020-ballot-signature-mismatches/index.html")
        self.assertEqual(self.new_News2.date,"2020-09-14T12:00:00Z")


if __name__ == '__main__':
    unittest.main()
