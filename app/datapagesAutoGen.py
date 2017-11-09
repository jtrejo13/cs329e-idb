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
# Last-Updated: Thu Nov  9 11:00:20 2017 (-0600)
#           By: yulu
#     Update #: 18
#

from app import app
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Songs, Artists, Albums, engine
from app.build_db import create_songs, create_artists, create_albums, session


@app.route('/song/<title>')
def database(title=None):
    songs = session.query(Songs)
    albums = session.query(Albums)
    return render_template('song-indiv.html', songs = songs, title = title, albums = albums)  
    
    
@app.route('/artist/<artist>')
def database2(artist=None):
    artists = session.query(Artists)
    albums = session.query(Albums)
    songs = session.query(Songs)
    return render_template('artist-indiv.html', artists = artists, artist = artist, songs = songs, albums = albums)

@app.route('/album/<album>')
def database3(album=None):
    albums = session.query(Albums)
    songs = session.query(Songs)
    #for dic in albums:
    #    if ''.join(dic['name'].split()).lower() == album:
    #        album_dic = dic
    return render_template('album-indiv.html', albums = albums, album = album, songs = songs)
