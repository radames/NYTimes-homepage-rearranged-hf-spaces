from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from transformers import pipeline
import feedparser
import json
from dateutil import parser

nyt_homepage_rss = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"

load_dotenv()
# Load Setiment Classifier
sentiment_analysis = pipeline(
    "sentiment-analysis", model="siebert/sentiment-roberta-large-english")
app = Flask(__name__, static_url_path='/static')

CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/news')
def get_news():
    nyt_homepage = get_nytimes()
    # filter only titles for sentiment analysis
    try:
        with open('last_predictions_cache.json') as file:
            cache = json.load(file)
    except:
        cache = {}

    # if new homepage is newer than cache, update cache and return
    if not cache or parser.parse(nyt_homepage['last_update']) > parser.parse(cache['last_update']):
        print("Updating cache with new preditions")
        titles = [entry['title'] for entry in nyt_homepage['entries']]
        # run sentiment analysis on titles
        predictions = [sentiment_analysis(sentence) for sentence in titles]
        # parse Negative and Positive, normalize to -1 to 1
        predictions = [-prediction[0]['score'] if prediction[0]['label'] ==
                       'NEGATIVE' else prediction[0]['score'] for prediction in predictions]
        # merge rss data with predictions
        entries_predicitons = [{**entry, 'sentiment': prediction}
                               for entry, prediction in zip(nyt_homepage['entries'], predictions)]
        output = {'entries': entries_predicitons,
                  'last_update': nyt_homepage['last_update']}
        # update last precitions cache
        with open('last_predictions_cache.json', 'w') as file:
            json.dump(output, file)
        # send back json
        return jsonify(output)
    else:
        print("Returning cached predictions")
        return jsonify(cache)


@ app.route('/predict', methods=['POST'])
def predict():
    # get data from POST
    if request.method == 'POST':
        # get current news
        # get post body data
        data = request.get_json()
        if data.get('sentences') is None:
            return jsonify({'error': 'No text provided'})
        # get post expeceted to be under {'sentences': ['text': '...']}
        sentences = data.get('sentences')
        # prencit sentiments
        predictions = [sentiment_analysis(sentence) for sentence in sentences]
        # parse Negative and Positive, normalize to -1 to 1
        predictions = [-prediction[0]['score'] if prediction[0]['label'] ==
                       'NEGATIVE' else prediction[0]['score'] for prediction in predictions]
        output = [dict(sentence=sentence, sentiment=prediction)
                  for sentence, prediction in zip(sentences, predictions)]
        # send back json
        return jsonify(output)


def get_nytimes():
    feed = feedparser.parse(nyt_homepage_rss)
    return {'entries': feed['entries'], 'last_update': feed["feed"]['updated']}


if __name__ == '__main__':
    app.run(host='0.0.0.0',  port=int(os.environ.get('PORT', 7860)))
