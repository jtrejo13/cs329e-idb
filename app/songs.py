from app import app
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Songs, engine
from app.build_db import create_songs, session

@app.route('/songs')
def songs():
  songs = session.query(Songs)
  tableTitles = ['name', 'artist', 'album', 'rank', 'genre', 'release_date', 'duration']
  #tableTitles = ['name', 'artist', 'album', 'rank', 'song_link', 'genre', 'release_date', 'duration']
  return render_template("songs.html", tableTitles = tableTitles, songs = songs)




