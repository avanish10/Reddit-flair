from flask import Flask, render_template,request, make_response,jsonify
from flair_predictor import detect_flair
import json
import requests
import os
import urllib
from urllib.parse import urlparse
app = Flask(__name__)


@app.route('/flairDetect', methods=['POST'])
def flairDetect():
	redditURL = request.form['redditpost']
	print(redditURL)
	predicted_flair = str(detect_flair(str(redditURL)))
	print(predicted_flair)
	return render_template('home.html', predicted_flair = predicted_flair)
@app.route('/automated_testing', methods=['GET'])
def apiFlairDetect():
    multidict = {}
    filename = request.args
    url = ("http://rflair.herokuapp.com/automated_testing?filename=%s" %filename)
    print(url)
    data = urllib.request.urlopen(url) # it's a file like object and works just like a file
    for line in data: 
        decoded_line = line.decode("utf-8")# files are iterable
        print(decoded_line)
        redditURL = str(decoded_line)
        redditURL = redditURL[redditURL.find(",")+3:-4]
        print(redditURL)
        flair = str(detect_flair(redditURL))
        multidict[redditURL] = flair
    
    return jsonify(multidict)

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost',port=5678,debug=False)
