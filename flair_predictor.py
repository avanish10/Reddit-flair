# installing libraries
import sklearn
import pickle
import praw
import re
import pandas as pd
from bs4 import BeautifulSoup
import nltk
nltk.download('all')
from nltk.corpus import stopwords
#preprocessing of data
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))
def clean_text(text):
    text = BeautifulSoup(text, "lxml").text
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text
#Flair detection 
def detect_flair(u):
    reddit = praw.Reddit(client_id='69D-_faFMb67Ww', client_secret='NicR7Ux1OFwOTuN1QDn49wq6itM',username='singhalavanish',password='cookies12', user_agent='singhalavanish')
    flair_dict={0:'Political',1:'Non-Political',2:'[R]eddiquette',3:'AskIndia',4:'Science/Technology',5:'Policy/Economy',6:'Finance/Business',7:'Sports',8:'Food',9:'Photography',10:'AMA',11:'Coronavirus'}
    loaded_model = pickle.load(open('./Model/finaliz_model.sav', 'rb'))
    submission = reddit.submission(url=u)

    data = {}

    data['title'] = submission.title
    data['url'] = submission.url

    data['title'] = clean_text(data['title'])
    data['combine'] = data['title'] + data['url']

    return loaded_model.predict([data['combine']])[0]
	
