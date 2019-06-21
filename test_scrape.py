from bs4 import BeautifulSoup as BS
import unittest
import scrape_func


with open("./test_html/posts.html") as post_html:
    docs = BS(post_html, 'html.parser')

class TestScrape(unittest.TestCase):

    def setUp(self):
        self.testdata = docs

    def test_get_row(self):
        self.assertEqual(scrape_func.getRow("ID", "Name", "Date", "Body"), ["ID", "Name", "Date", "Body"])

    def test_get_all_posts(self):
        _valid_posts = scrape_func.get_all_posts(self.testdata)
        self.assertEqual(len(_valid_posts), 1)

    def test_parse_posts(self):
        self.assertEqual(scrape_func.parse_posts(self.testdata), None)
    
    


if __name__ == '__main__':
    unittest.main()