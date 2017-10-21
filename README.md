# CS329E iDB Project  
## About
**Hi team**  
Here i quickly wrote a flask warpper of the structure of plain html with links to each subpages   
The app has a *package* structure rather than *module*, for easier maintenance.  
Tring to make CSS work with flask nicely     

## How it looks like now ?  
Current the website is hosted on yellowjacket, follow this link:  
[http://128.83.139.95:5000/](http://128.83.139.95:5000/)  

## How to Run  
Simply clone from this branch  
```
git clone git@github.com:jtrejo13/cs329e-idb.git
git pull origin flask_setup
git checkout flask_setup 
``` 
and if you havn't got flask install, do  
```
pip install -r requirements.txt
```
Then you should be good to go  
```
python3 run.py
```
Then check the page at  
```
localhost:5000
```

## To do  
+ ~~Write basic flask web frame work~~
+ Python crawling to find daily top rated songs, auto generate all links and pics of artist 
+ Add data base from the crawling 
+ CSS3 embed
+ js for interactive response
+ make the whole webpage responsive 
+ host on GCP
## Any suggestions ?  
You're welcomed to open a new issue and label it as "enhancement" 



