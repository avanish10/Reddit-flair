# Rflair
It is a Reddit Flair Detector for [r/india](https://www.reddit.com/r/india/) subreddit, 
that takes a post's URL as user input and predicts the flair for the post using a SVM Classifier model
The web-application is hosted on Heroku at (https://rflair.herokuapp.com/).

## Libraries Used:
- Scikit-learn
- PRAW
- NLTK
- Flask
- numpy
- pandas
- Json
- Matplotlib

The Scraped data is saved in Data folder withing the directory.

## What I made:
Developed a Web Application which predicts the flair of the respective url post inputed by user. 

Procedure:
1. Clone the repository
```
git clone https://github.com/avanish10/Reddit-flair.git
```
2. Set a path in terminal.
```
cd rflair
```
3. Finally, install the project dependencies
```
pip install -r requirements.txt
```
4. To run the server, execute the following command
```
python app.py
```

## Approach 
### Data Scraping
The python library PRAW has been used to scrape data from the subreddit r/india, with a  250 posts from each 14 different flairs.

### Data preprocessing
The data has been preprocessed using the NLTK library. The following procedures have been executed on the title, URLto clean the data:
1. Tokenizing and removing symbols
2. Removing stopwords

databases have been prepared and saved as a csv for training.

### Training 
The data has been loaded from a directory to a pandas DataFrame and split into 70-30 Training-Testing sets using scikit-learn.
Each of the post features: Title, Body, URL, Title+URL were trained on three algorithms: Naive Bayes, Linear SVM and Logistic Regression, for both datasets(with and without stemming).

After going through the flair-wise and overall prediction accuracies, the model trained using Title+Body+Comments on non-Stemmed data, using Logistic Regresssion was chosen. 

* Flair Prediction
The saved model is loaded for predicting the flair once the post features (title, body and comments) have been cleaned using NLTK. The returned result is displayed on the web-application.

* For automated post request, it can be done with: 
```
https://rflair.herokuapp.com/automated_testing?filename=%s" %filename
```

* Future plans:
I plan on adding the following features to the project:
1. Improving the prediction by training the model on user inputs.
2. Make a script which helps user in predicting flair of any reddit page.

* What I have learnt:
This task help to know my capabilities and make me more confident and passionate towards Machine learning.It's my 
first project in which I have used heroku.By working on NLP I have learned many things about how to do classification.
* Results:
### Results

#### Title +URL as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.4455445544      |
| Linear SVM                 | 0.58019801980     |
| Logistic Regression        | 0.582178217821782 |
| Random Forest              | 0.5188118811      |




* References:
1. [Scraping Reddit](https://www.storybench.org/how-to-scrape-reddit-with-python/)
2. [Pre-processing Data,Text Classification](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)
3. [Saving and loading models in ML](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/)
4. [Deploying Flask app to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
