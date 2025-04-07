# Proposal Requirements

In your project proposal, you should include the following:

1. Working title of your project

Searchify

2. A summary of the dataset(s) you will use in this project (e.g. topic, interesting variables,
etc)

Dataset of the most popular songs on Spotify. Includes scores for each song in 12 features,
including: Energy, Tempo, Danceability, Loudness, Liveness, Valence, Speechiness,
Instrumentalness, Mode, Key, Duration, and Accousticness. Each song is also given a
percentile popularity score based on the total number of Spotify streams.

3. Metadata for the dataset(s) from the Dataset Records (URL, date downloaded,
    authorship, exact name and version, terms of use, suggested citation)
       a. _If you’re having trouble filling out the following fields for your dataset, it may be a_
          _sign that you need to double-check the source of your dataset.

URL:_ https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset/code
Date downloaded: Jan 19, 2025
Author: Solomon Ameh
Version: 1
Terms of use/license: Database Contents License (DbCL) v1.

DOI Citation: N/A

4. 3 interesting or meaningful ways that a user could interact with the data. For each user
    interaction, include descriptions of:

a. Potential Users: Who may interact with your data? What are their motivations for
interacting with the data?

b. Interaction Mechanism: How may they interact with the data? (e.g. Search bar?
Different tabs? Which variables in your dataset?)

c. Potential Benefits: How may interacting with your data benefit users? Why?
If you don’t think users will benefit, then why bother developing that user
interaction? ̄\_(ツ)_/ ̄

Potential Harms: How may interacting with your data harm or exclude users? Why?
If you don’t think users will feel harmed or excluded by interacting with
your data, explain why.

The potential users are those looking to find new music to listen to, and or people that are
interested in the stats/rankings of songs.

The main way we see people interacting with this is to find new music that they would like, and there are
a few ways to go about this. First, they could input a song that is already on the list that they like, and 
our website would then return the most similar songs to it. For this, a simple search bar would work, maybe with
autocomplete so that they don't try to enter a song that isn't in the data set.

The second way we see the user interacting with it is to input one of the categorical variables they are interested in, for 
example, tempo. Our website would then return the highest (or lowest, depending on user input) tempo songs on the list. For this a
dropdown menu with all the different categories could be used.

Lastly, we want to incorporate a way of chaining different categories together, so that the user could enter in something that returns 
the highest tempo pop songs, for example.

The main benefit is that users can find songs that match their music taste that they otherwise might not know
about.

The main drawback/harm, for all of these interactions, is that it’s all Spotify data, so if Spotify isn’t used a lot in your culture and or country, your music
won’t be represented by this dataset. It’s all pretty Western centered. Additionally, it's only the most popular songs that are featured so, if you're trying to
find the song that best matches a bunch of variables, there's no guarantee that it's the best match of every song on Spotify.


