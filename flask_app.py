from flask import Flask, abort,  render_template, request
from ProductionCode.helperFunctions import *
from Models.view_dataset_model import ViewDatasetModel
from Models.filter_top_model import FilterTopModel
# import psycopg2
# import ProductionCode.psqlConfig as config
from ProductionCode.dataSource import DataSource
from flask import *

app = Flask(__name__)

test = DataSource()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def show_categories():
    """Renders a page with all of our categories and a description."""
    return render_template('categories.html')

@app.route('/dataset')
def show_dataset():
    """Renders a page that gives information on the source of our dataset."""
    return render_template('dataset.html')

@app.route('/searchPage', methods=['GET', 'POST'])
def show_searchPage():
    searchResults = None
    chosenCategory = None
    chosenOrder = None
    if request.method == 'POST':
        chosenCategory = request.form.get('category')
        chosenOrder = request.form.get('sortOrder')
        chosenNumber = request.form.get('numResults')
        searchResults = test.asc_or_desc(chosenCategory, chosenNumber, chosenOrder)

    return render_template('searchPage.html', searchResults=searchResults, chosenCategory=chosenCategory, chosenOrder=chosenOrder)
    

@app.errorhandler(404)
def page_not_found(e):
   '''Prints an error message on the webpage if the URL is incorrectly inputted.'''

   return f"""<pre> 
   404 Error: Page not found.
   Make sure the URL route ends in one of the following forms:
   /filter_top/&lt;variable&gt;/&lt;number_of_songs&gt;/&lt;sort_method&gt;/&lt;dataset&gt; 
   OR 
   /view_dataset/&lt;dataset_name&gt

   <b1>SPECIFIC FEATURE USAGE INSTRUCTIONS: </b1>
   To view one of the datasets, add '/view_dataset/' to the end of the webpage URL. 
   Then add the name of the dataset you want to view: 'high', 'low', or 'mini'. 
   For example: to view the high popularity dataset, add '/view_dataset/mini' to the URL.

   To get a list of top or bottom songs in a category, add to the URL with the following information: 
   filter_top/&lt;variable&gt;/&lt;number_of_songs&gt;/&lt;sort_method&gt;/&lt;dataset&gt;.
   </pre>"""

@app.errorhandler(500)
def python_bug(e):
   '''Prints a bug message on the webpage, indicating that there is a problem in the code.'''
   return "Bug found, please review your code."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5200)