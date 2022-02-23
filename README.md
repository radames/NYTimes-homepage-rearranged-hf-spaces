---
title: NYTimes Homepage Sentiment Analysis 
emoji: 📰
colorFrom: red
colorTo: green
sdk: gradio
app_file: main.py
pinned: false
---

# The New York Times Sentiment Analysis

This project is an experiment running sentiment analysis on the current [New York Times](https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml) homepage headlines RSS. It also provides a sorting button to toggle between good and bad news first😛 . It's built with a [custom SvelveKit front-end](https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/tree/main/client) , served by a [Flask application](https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/blob/main/app.py) and using [transformers pipeline for the sentiment analysis.](https://huggingface.co/siebert/sentiment-roberta-large-english)

### Notes

#### Install Node with NVM

This [Node script](https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/blob/main/install-node.sh) install node LTS and create symbolic links to `/home/user/.local/bin/` as it seems like we don't have permission to update `$PATH` env

#### main.py

Because the Spaces run a python application, see [`app_file`](https://huggingface.co/docs/hub/spaces#:~:text=0.88.0%2C%200.89.0%2C%201.0.0.-,app_file,-%3A%20string%0APath%20to) on docs. main.py is just a simple python subprocess to run `make build-all` See [`Makefile`](https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/blob/main/Makefile)

#### SvelteKit Node Adapter?

SvelteKit eventually can be used as our primary web application with [`@sveltejs/adapter-node`](https://github.com/sveltejs/kit/tree/master/packages/adapter-node) adaptor and Flask the API application with your ML project. However, there is an unsolved issue to enable [dynamic basepath](https://github.com/sveltejs/kit/issues/595), which blocks the possibility to embedded deployment or using a relative path.

