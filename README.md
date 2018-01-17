# CS329E idb Project - NetTunes
## About
Visit Nettunes [here](http://www.nettunes.me)!

Nettunes is an on-line music database which allows users to search for artists, albums, and songs. The site was built
on Google Cloud Platform with HTML5/CSS3/Javascript, utilizing Python and SQLAlchemy to interact with the
postrgreSQL database, and Jinja2 templates for the individual pages. Scrapy was used to extract data from iTunes to
build the database.


## How to Run  
To run the NetTunes app on your local computer:

1. Clone the repository
```
git clone git@github.com:jtrejo13/cs329e-idb.git
git pull origin master
``` 

2. If you don't have virtualenv, install it using pip.
```
sudo pip install virtualenv
```
3. Create an isolated Python environment, and install dependencies:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
4. Run the application:
```
python main.py
```

5. In your web browser, enter the following address:
```
http://localhost:8000
```
