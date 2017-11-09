
import os
from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from flask import *
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, LargeBinary, Boolean

from app.models import *

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class tests(TestCase):
	
	# Test that table "Artists" is writable
	def test_write_artists(self):
		query = session.query(artists).all()
		startSize = len(query)

		session.add(artists(name = 'ARTIST', genre = 'GENRE'))
		session.commit()
		query = session.query(artists).all
		endSize = len(query)
		
		self.assertEqual(startSize + 1, endSize)


	# Test that table "Artists" can be written multiple queries 
	def test_write_artist_multiple(self):
		query = session.query(artists).all()
		startSize = len(query)

		session.add(artists(name = 'ARTIST_MULTIPLE_1', genre = 'GENRE'))
		session.add(artists(name = 'ARTIST_MULTIPLE_2', genre = 'GENRE'))
		session.commit()
		query = session.query(artists).all()
		endSize = len(query)

		self.assertEqual(startSize + 2, endSize)

	
	# Test that table "Artists" is readable
	def test_read_artists(self):
		session.add(artists(name = 'TESTREAD', genre = 'GENRE'))
		session.commit

		query = session.query(artists).all()
		found = False

		for artist in query:
			if(artist.name == 'TESTREAD' and artist.genre == 'GENRE'):
				found = True

		self.assertTrue(found)

	
	# Test that table "Artists" is readable and accounts for case sensitivity
	def test_read_artists_case_sensitive(self):
		session.add(artists(name = 'TESTCASE', genre = 'GENRE'))
		session.commit()

		query = session.query(artists).all()
		found = False

		for artist in query:
			if(artist.name == 'TESTCASE'):
				found = True
			if(artist.name == 'testcase'):
				found = False

		self.assertTrue(found)

	
	# Test filtering "Artists" by an attribute
	def test_read_artists_atribute(self):
		session.add(artists(name = 'TESTATTR', genre = 'Alternative-Rock'))
		session.commit()

		query = session.query(artists).filter(artists.name == 'TESTATTR').first()

		self.assertTrue(query is not None)
		self.assertTrue(query.genre == 'Alternative-Rock')

	
	# Test filtering "Artists" by an attribute returns multiple unique results
	session.add(artists(name = 'TESTATTR1', genre = 'Alternative-Pop'))
	session.add(artists(name = 'TESTATTR1', genre = 'Electronic'))
	session.commit

	query = session.query(artists).filter(artists.name == 'TESTATTR1').all()

	self.assertTrue(query is not None)
	self.assertTrue(len(query) == 2)

	genres = []
	for artist in query:
		genres.append(artist.genre)

	self.assertTrue(gneres[0] != genres[1])

	
	# Test deletion of a row in table "Artists"
	def test_artists_delete(self):
		session.add(artists(name = 'ARTISTDEL'))
		session.commit

		query = session.query(artists).filter(artists.name == 'ARTISTDEL').first()

		self.assertTrue(query is not None)

		session.delete(query)
		session.commit()
	
		new_query = session.query(artists).filter(atists.name == 'ARTISTDEL').first()
		self.assertTrue(new_query is None)

	# Test creating object from "Artists"
	new_entry = artists(
		name = 'artist',
	    artist_link = 'website.com',
	    pic_link = 'pic.com',
	    origin = 'middle of nowhere',
	    genre = 'genre',
	    start_date = '11/5/2017',
	    latest_release = '11/6/2017',
	    bio = 'Some bio'
	)

	result = {
		name: 'artist',
	    artist_link: 'website.com',
	    pic_link: 'pic.com',
	    origin: 'middle of nowhere',
	    genre: 'genre',
	    start_date: '11/5/2017',
	    latest_release: '11/6/2017',
	    bio: 'Some bio'
	}

	self.assertTrue(artists.get_obj(new_entry) == result)



if __name__ == "__main__":
	main()