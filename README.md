---
title: NYTimes Homepage Sentiment Analysis
emoji: 📰
colorFrom: red
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# The New York Times Sentiment Analysis

This project is an experiment running sentiment analysis on the current [New York Times](https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml) homepage headlines RSS. It also provides a sorting button to toggle between good and bad news first😛 . It's built with a [custom SvelveKit front-end](https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/tree/main/client) , served by a [Flask application](https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/blob/main/app.py) and using [transformers pipeline for the sentiment analysis.](https://huggingface.co/siebert/sentiment-roberta-large-english)

### Running

#### Server

```bash
python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python app.py
```

#### Client

```bash
cd frontend
npm install
npm run dev
```

go http://localhost:5173/

or

```bash
make build-all
make run
```

go http://127.0.0.1:7860
