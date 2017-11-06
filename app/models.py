import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know
# that our classes are special SQLAlchemy classes that
# corresponds to tables in our DB)
Base = declarative_base()


class Artists(Base):
    __tablename__ = 'artists'

    name = Column(String(80), primary_key=True, nullable=False)
    artist_link = Column(String)
    pic_link = Column(String)
    origin = Column(String(80))
    genre = Column(String(80))
    start_date = Column(String)
    latest_release = Column(String)
    bio = Column(Text) 
    

class Albums(Base):
    __tablename__ = 'albums'

    name = Column(String(80), primary_key=True, nullable=False)
    album_link = Column(String)
    pic_link = Column(String)
    release_date = Column(String)
    info = Column(Text)
    artist = Column(String)
    genre = Column(String)
    num_tracks = Column(Integer)
    track_list = Column(Text)



class Songs(Base):
    __tablename__ = 'songs'

    name = Column(String(80), primary_key=True, nullable=False)
    artist = Column(String)
    album = Column(String)
    rank = Column(String)
    song_link = Column(String)
    genre = Column(String(20))
    release_date = Column(String)
    duration = Column(String)


SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:12345@localhost/nettunes')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
