# CS257-Kazoogle

Usage: python3 command_line.py --data <dataset> --var <variable> --sort <sorting method> --n <number of songs>

Possible Selections:
Dataset: high (Spotify high popularity songs), low (Spotify low popularity songs), mini (Dummy data)
Variable: tempo, energy, danceability, valence, loudness, acousticness, liveness, speechiness, instrumentalness, key, mode, time_signature, duration_ms, popularity.
Sorting Method: max, min.
Number of Songs: 1 - Size of Dataset.

Scanability: We've purposely kept the website very simple and uncluttered to help with scanability. 
There is very little jargon and terms are explained on an additional page.

Satisficing: The number of options the user has is also kept to a minimum. The main functionality
is all located on the homepage with preset options for all the variables they could possibly enter.
The page headers for the other pages are also simple and descriptive, and a user would never have to
even look there if they don't want to.

Muddling Through: Again the website is pretty simple. The user can muddle through the pages if needed, but
all the main functionality is on the homepage, hopefully reducing the need to muddle through.

# Design Improvements

1) Issue: invalid user input into the "number" box crashed the site.
Solution: We made it so the user gets an error message when entering in a decimal or empty input.
Page: searchPage.HTML

2) Issue: the style and look of each page was very different and it gave the website an unwanted discontinuity
Solution: We made changes to the UI (css and HTML files) so all the pages are in the same style
Page(s): created new CSS files (catergoriesStyle.css and datasetStyle.css), changed dataset.html and catergories.html

3) Issue: confusing terminology
Solution: changed "max" and "min" to "low-to-high" and "high-to-low"
Page: searcPage.html

4) Issue: results were unclear; the page refreshed upon entering a search and the user could no longer see what they searched up
Solution: We printed the search terms on top of the results upon refres
Page: searchPage.html

# Code Improvements

1) Code smell: get_query was doing more than one thing and was difficult to read
Solution: We refactored get_query in dataSource so that it's cleaner, splitting it into asc_or_desc and get_query, the former of which calls the latter. We got rid of the check for valid category input (tempo, valence, etc) since the only allowed inputs are given in a drop down menu. We got rid of the max/min check which decides whether to sort from low to high or high to low since that is also now a drop down menu with set inputs.
File/lines: dataSource.py (lines 20-50)

2) Code smell: bad variable names (naming issue)
Solution: in flask_app.py, variable names were refactored to be more descriptive: "variable" to "chosen catergory", and "maxormin" to "chosenorder", "num" to "chosennumber". The same variables had there names changed in other files accordingly.
File(s)/lines: flask_app.py (30-40), same names changed in datasource.py and searchPage.html

3) Code smell: old, commented code
Solution: removed it!
File(s): throughout dataSource.py and flask_app.py