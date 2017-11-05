from app import app
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Songs, engine
from build_db import create_songs, session

@app.route('/songs')
def songs():
    songs = session.query(Songs)
    tableTitles = ['NAME', 'DURATION', 'BAND', 'ALBUM', 'GENRE', 'YEAR_OF_RELEASE', 'LYRICS_LINK', 'VIDEO_LINK']
    return render_template("songs.html",
                           tableTitles = tableTitles,
                           songs = songs)




