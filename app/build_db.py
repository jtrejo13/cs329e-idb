import json, logging

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment
from sqlalchemy.orm import sessionmaker
from app.models import Artists, Albums, Songs, engine, Base

# bind the engine to the base class. This makes the connection
# between our class definitions and the corresponding tables
# within our database
Base.metadata.bind = engine

# create session maker object to establish a link
# of communication between our code execution and
# the engine we just created
DBSession = sessionmaker(bind=engine)

# in order to create, read, update or delete information
# on our database, SQLAlchmey executes database operations
# via an interface called a session.
# A session allows us to write down all the commands
# we want to execute but not send them to the DB
# until we call "commit"
# create an instance of DBSession
session = DBSession()


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


def create_songs():
    song_dic = load_json('itunes_songs.json')

    for one_song in song_dic:
        name = one_song["song"]
        artist = one_song["artist"]
        album = one_song["album"]
        rank = one_song["rank"]
        song_link = one_song["albumLink"]
        genre = one_song["genre"]
        release_date = one_song["release_time"]
        duration = one_song["duration"]

        newSong = Songs(name = name, artist = artist, album = album, rank = rank, song_link = song_link, genre = genre, release_date = release_date, duration = duration)
        # After I create the book, I can then add it to my session.
        session.add(newSong)
        # commit the session to my DB.
        session.commit()


create_songs()