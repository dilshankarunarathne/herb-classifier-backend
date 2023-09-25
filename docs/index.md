# Herb Classifier Backend

The server side application including the RestAPI with FastAPI and the ML models for the **Herb Classifier**
application. 

[![Version](https://img.shields.io/badge/version-1.1-brightgreen.svg)](https://pypi.org/project/ad-topic-recommender/)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Project layout

<pre>
│   .gitattributes
│   .gitignore
│   application.properties
│   config.py
│   herb_classifier_api_v1.yaml
│   LICENSE
│   main.py
│   mkdocs.yml
│   README.md
│   requirements.txt
│   test.py
│   test_main.http
│
├───.github
│       FUNDING.yml
│
├───.idea
│   ...
│
├───auth
│   │   authorize.py
│   │   hashing.py
│   │   __init__.py
│   │
│   └───__pycache__
│           ...
│
├───bin
│       .gitkeep
│       classifier_sequential.h5
│
├───classifier
│       main.py
│       test.png
│       test.py
│       __init__.py
│
├───dao
│   │   disease_dao.py
│   │   herb_dao.py
│   │   location_dao.py
│   │   user_dao.py
│   │   __init__.py
│   │
│   └───__pycache__
│           ...
│
├───docs
│       about.md
│       getting_started.md
│       index.md
│       installation.md
│       tutorials.md
│
├───models
│   │   blacklist_model.py
│   │   disease_model.py
│   │   herb_model.py
│   │   location_model.py
│   │   token_model.py
│   │   user_model.py
│   │   __init__.py
│   │
│   └───__pycache__
│           ...
├───routes
│   │   auth.py
│   │   disease.py
│   │   herb.py
│   │   location.py
│   │   __init__.py
│   │
│   └───__pycache__
│           ...
│
├───services
│   │   disease_service.py
│   │   herb_service.py
│   │   location_service.py
│   │   token_service.py
│   │   user_service.py
│   │   __init__.py
│   │
│   └───__pycache__
│           ...
│
├───site
│   │   404.html
│   │   index.html
│   │   sitemap.xml
│   │   sitemap.xml.gz
│   │
│   ├───about
│   │       index.html
│   │
│   ├───assets
│   │   │   _mkdocstrings.css
│   │   │
│   │   ├───images
│   │   │       favicon.png
│   │   │
│   │   ├───javascripts
│   │   │   │   ...
│   │   │   │
│   │   │   ├───lunr
│   │   │   │   │   ...
│   │   │   │   │
│   │   │   │   └───min
│   │   │   │           ...
│   │   │   │
│   │   │   └───workers
│   │   │           ...
│   │   │
│   │   └───stylesheets
│   │           ...
│   │
│   ├───getting_started
│   │       index.html
│   │
│   ├───installation
│   │       index.html
│   │
│   └───tutorials
│           index.html
│
└───__pycache__
        ...
</pre>

 - [getting_started.md](Getting Started)
 - [installation.md](Installation)
 - [tutorials.md](Tutorials)

