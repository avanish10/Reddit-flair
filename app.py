from flask import Flask, render_template,request, make_response
from flair_predictor import detect_flair
import json
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
'''@app.route('/postAnalysis')
def postAnalysis():
	return render_template('analysis.html')
@app.route('/api/resource', methods=['GET'])
def apiFlairDetect():
	redditURL = request.args
	redditURL = str(redditURL)
	redditURL = redditURL[redditURL.find(",")+3:-4]
	print(redditURL)
	flair = str(detect_flair(redditURL))
	flairPrediction = {'status': 'successful', 'status_code': 200, 'result':{'flair':flair}}
	return json.dumps(flairPrediction)
@app.errorhandler(404)
def not_found(error):
	return make_response(json.dumps({'status': 'failed', 'status_code': 404, 'result': {'error': 'Not found'}}))
@app.errorhandler(500)
def internal_server_error(error):
	return make_response(json.dumps({'status': 'failed', 'status_code': 500, 'error': '500: Incorrect request format'}),500)
    '''
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
    #fle = url[url.rfind("=")+1:]
    #filename_small = fle.replace(".", ".txt")
    #file1 = open(filename_small, 'r') 
    #file1 = open(filename, 'r') 
    #Lines = file1.readlines() 
        redditURL = str(decoded_line)
        redditURL = redditURL[redditURL.find(",")+3:-4]
        print(redditURL)
        flair = str(detect_flair(redditURL))
        multidict[redditURL] = flair
        #flairPrediction = {'status': 'successful', 'status_code': 200, 'result':{redditURL:flair}}
        #payload = json.dumps(flairPrediction)
    with open('result.json', 'w') as fp:
        return json.dump(multidict, fp)

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost',port=5098,debug=False)
