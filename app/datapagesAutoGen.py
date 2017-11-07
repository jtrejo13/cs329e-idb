# datapagesAutoGen.py ---
#
# Filename: datapagesAutoGen.py
# Description:
#
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu
#
# Created: Wed Oct 25 23:11:53 2017 (-0500)
# Version:
# Last-Updated: Wed Oct 25 23:15:15 2017 (-0500)
#           By: yulu
#     Update #: 9
#

from app import app
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Songs, Artists, Albums, engine
from app.build_db import create_songs, create_artists, create_albums, session

songs = session.query(Songs)
artists = session.query(Artists)
albums = session.query(Albums)


@app.route('/database/song/<title>')
def database(title=None):
    return render_template('song-indiv.html', songs = songs, title = title)  
    
@app.route('/database/artist/<artist>')
def database2(artist=None):
    return render_template('artist-indiv.html', artists = artists, artist = artist)

@app.route('/database/album/<album>')
def database3(album=None):
    return render_template('album-indiv.html', albums = albums, album = album)
