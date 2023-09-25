# Herb Classifier Backend

The server side application including the RestAPI with FastAPI and the ML models for the **Herb Classifier**
application. It has OAuth2 authentication and JWT token generation. 

## Project layout

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
│   │   ...
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
