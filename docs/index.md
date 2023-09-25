# Herb Classifier Backend

The server side application including the RestAPI with FastAPI and the ML models for the **Herb Classifier**
application. 

[![Version](https://img.shields.io/badge/version-1.2-brightgreen.svg)](https://pypi.org/project/ad-topic-recommender/)
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

 - [Installation](installation.md)
 - [API Documentation](api_documentation.md)
 - [tutorials.md](Tutorials)
 - [about.md](About)

## Contributing

Go ahead and check out the GitHub repository if you'd like to contribute to this project. Please check the contribution guidelines for more information.
[https://github.com/dilshankarunarathne/herb-classifier-backend/](Herb Classifier Backend)

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]  
[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa] 

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Contact Information

For questions or feedback, please contact the author:

- Author: Dilshan M. Karunarathne
- Email: ceo@altier.tech
- Website: [http://altier.tech](http://altier.tech)
