import unittest
from ProductionCode.helperFunctions import *
from flask_app import *
from ProductionCode.dataSource import DataSource

# I found that comparisons using the low_popularity.csv dataset are not working. After looking at the dataset
# I think it is because the ordering of information is different than the ordering in the high_popularity.csv dataset.
# python3 -m unittest discover Tests/ 3333

# SOME TESTS ARE COMMENTED OUT BECAUSE THEY NO LONGER APPLY TO THE DATABASE VERSION OF THE FLASK SITE

class TestWelcomePage(unittest.TestCase):
    def test_welcome(self):
        '''Tests that the welcome page prints correctly.'''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        # Have to encode the expected string into a byte to compare with the response.data
        self.assertIn(expected_welcome.encode("utf-8"), response.data)

class TestCatergories(unittest.TestCase):
    def test_catergories(self):
        '''Tests that the catergories page prints correctly'''
        self.app = app.test_client()
        response = self.app.get('/categories', follow_redirects=True)
        # Have to encode the expected string into a byte to compare with the response.data
        self.assertIn(expected_categories.encode("utf-8"), response.data)

class TestDataset(unittest.TestCase):
    def test_catergories(self):
        '''Tests that the catergories page prints correctly'''
        self.app = app.test_client()
        response = self.app.get('/dataset', follow_redirects=True)
        # Have to encode the expected string into a byte to compare with the response.data
        self.assertIn(expected_dataset.encode("utf-8"), response.data)


class TestOutputPage(unittest.TestCase):
    def test_404(self):
        self.app = app.test_client()
        response = self.app.get('/tempo/1/max/high_popularity.csv/hello', follow_redirects = True)
        expected = string_404_error

        self.assertEqual(clean_string(expected), byte_to_cleaned_string(response.data))


string_404_error = f"""
   404 Error: Page not found.
   Make sure the URL route ends in one of the following forms:
   /filter_top/&lt;variable&gt;/&lt;number_of_songs&gt;/&lt;sort_method&gt;/&lt;dataset&gt; 
   OR 
   /view_dataset/&lt;dataset_name&gt b

   SPECIFIC FEATURE USAGE INSTRUCTIONS:b
   To view one of the datasets, add '/view_dataset/' to the end of the webpage URL. 
   Then add the name of the dataset you want to view: 'high', 'low', or 'mini'. 
   For example: to view the high popularity dataset, add '/view_dataset/mini' to the URL.

   To get a list of top or bottom songs in a category, add to the URL with the following information: 
   filter_top/&lt;variable&gt;/&lt;number_of_songs&gt;/&lt;sort_method&gt;/&lt;dataset&gt;.
   """

expected_welcome = """<h2>Welcome to Searchify! Explore the statistics behind popular music.</h2>"""

expected_categories = """<p>Tempo - Measures the speed of a track in beats per minute.</p>"""

expected_dataset = """<p>A link to this source can be found <a href='https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset/code'>here.</a></p>"""