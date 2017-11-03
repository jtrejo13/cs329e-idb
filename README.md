# CS329E idb Project - NetTunes
## About

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
python run.py
```

5. In your web browser, enter the following address:
```
http://localhost:8000
```

## To do  
+ ~~Write basic flask web frame work~~
+ Python crawling to find daily top rated songs, auto generate all links and pics of artist 
+ Add data base from the crawling 
+ CSS3 embed
+ js for interactive response
+ make the whole webpage responsive 
+ host on GCP
