from app import app
import codecs, json, os
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Albums, engine
from build_db import create_albums, session

@app.route('/albums')
def albums():
    albums = session.query(Albums)
    tableTitles = ['NAME', 'NO_OF_TRACKS', 'BAND', 'GENRE', 'YEAR_OF_RELEASE']
    return render_template("albums.html",
                           tableTitles = tableTitles,
                           albums = albums)
