# CIDER analysis:

***Added during sprint 1 - command line***
## Assumption 1: The user uses Spotify

Since the dataset features the most popular songs on spotify, and
Spotify is primarily used in "Western" countries, the songs featured
in our dataset will be pretty limited. If a user is from a country where
Spotify isn't used, their music tastes won't be represented here.

To improve this in future interations we could try to get data from
other sources to track what is popular more globally.

## Assumption 2: The user has vision

Although one doesn't need sight to listen to music, they do need it
for this software which could be limiting. They need to be able to see
in order to type into the command line and view the results.

To improve upon this, a text to speech function could be implemented, or 
perhaps once it's hosted as a website, a web browser could have their own
text to speech functionality that fixes this.

## Assumption 3: The user is familiar with popular music

Our dataset only has statistics for several thousand of the most popular songs,
which is not very helpful or useful for users who don't listen to popular
music but want similar functionality for the music they listen to.

To improve upon this, we could scrape data from a custom input of songs using
the Spotify API. Another solution would be a larger database, but this
would be an unfair use of the remote computing resources for the class.

***Added during sprint 2 - flask app***
## Assumption 4: The user has access to the internet

Users who don't have the database and source code on their device can only use this
website if they have access to the internet. 

To improve our program in accordance with this assumption, we could allow users to
download the database and source code when they do have access to the internet
so they can use the application offline. This improvement is limited to users
who have access to the internet at some point.

## Assumption 5: The user has access to a web browser

This program is, at its core, a website, so it obviously assumes the user
has access to a web browser. People without access to one, such as
potential users with cetain distributions of linux, cannot use it.

This assumption has already been addressed by the construction of a command
line app. Users with access to a terminal, but no web browser, can still
have some functionality.

## Assumption 6: The user doesn't have software/administration blocking http activity

This program generates a website that uses http, not https, which some
softwares and administrations don't allow access to, given that it is less
secure and very few websites still use it.

To improve upon this, we could buy an https certificate, although this would
not be cheap.

***Added during sprint 3 - database***
## Assumption 7: The user is familiar with concepts of music theory

The dataset contains information about time signature, tempo, key, and other
statistcs that assume the user is familiar with music theory. Without some 
basic knowledge on the topic,users cannot get any valuable insight on much of the dataset.

This assumption can easily be handled by providing a short lesson on music theory
available in the taskbar.

## Assumtion 8: The user is familiar with niche descriptors

The dataset has field such as "valence", "speechiness", and "instrumentalness", which
don't have clear definitions at first glance. Thus, the dataset assumes users are familiar with
niche descriptors and technical music terms.

To improve upon this assumption, the dropdown menu where the field is selected could
provide question mark buttons that show a blurb describing the catergory.

## Assumption 9: The catergories can be fully represented objectively using numbers

This dataset assumes that music can be described well by numbers; that popular music fits
objectively into a formula of sorts. In reality, music is completely subjective like any
other form of art, and the "happiness" (valence) of a song cannot be reduced to a number.

To handle this assumption, we could provide a disclaimer on the home page of the website
warning that any correlative patterns don't necessarily cause the popularity of a song.

***Added during sprint 4 - front-end***

## Assumption 10: Visually-impaired users have screen-reader softwares available

Although our HTML objects have correctly named ID's and other descriptions for screen-
reading capabilities, the GUI still assumes visually impaired users have such softwares installed.
If they don't they will not have access to any of the information on the site.

To handle this assumption, we could add a text-to-speech function that is built-in to the site,
and announces its presence to the user as soon as the site is opened.

## Assumption 11: User has a functioning mouse

The GUI assumes the user can use cursor movement to access many of the buttons and move 
to other pages using the taskbar. In comparison, the CLI app only required a functioning keyboard.

To handle this assumption, we could create typable commands (like the tab key in forms)
to allow users to move between HTML features.

## Assumption 12: The user is not colorblind

The website has some elements (colored text inset in colored boxes) that could pose issues
for certain kinds of colorblindness. The GUI thus assumes the user has only the more common
kinds of color blindess.

To handle this assumptions, we could have a preferences tab where users can indicate their
colorblindness, and the color scheme of the websie will change accordingly.

# Potential Users:

The potential users of this software would be those who are interested in
how popular songs compare to each other.

With our GUI, a screen reader now can effectively display the contents of 
our website, allowing usability for visually-impaired users.

# Potential Benefits:

Our software allows users to sort and view data based on a variety of variables.
This can allow users to find song they think they might like. For example, if they
like slow songs, they can sort by tempo and use the min keyword to return the lowest
tempo songs. Conversly, they can also use the max keyword to find highest tempo
songs.