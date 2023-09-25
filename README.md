# Herb Classifier Backend

The server side application including the RestAPI with FastAPI and the ML models for the **Herb Classifier**
application. It has OAuth2 authentication and JWT token generation. 

[![Version](https://img.shields.io/badge/version-1.2-brightgreen.svg)](https://pypi.org/project/ad-topic-recommender/)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Table of Contents

- [Herb Classifier Backend](#herb-classifier-backend)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
    - [Project Scope](#project-scope)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact Information](#contact-information)

## Description

We develop a centralized and comprehensive database system for Hela Wedakama using 
the medicinal plants used in these medicine in Sri Lanka. We use image processing 
techniques to identify five specific medicinal plants from weed plants that have similar 
morphological features, making it difficult to distinguish them through visual inspection 
alone.

The application allows users to add locations of known medicinal plants using GPS. 
Additionally, users can search for other plant locations using the application...

### Project Scope
This study aims to provide consumers with a reliable source of information on traditional 
medicines by developing a centralized database system for home remedies and medicinal 
plants used in Sri Lankan traditional home remedies, which can be accessed as a mobile 
application. 

1. A user can search what herbal plants can be medicinally useful for a certain illness / disease,
and vice-versa.
2. The model should at least be able to (trained for) identify three medicinal herbs.
3. The users should be able to get the locations of which areas the plants would grow, or can be found.

## Prerequisites

- Python 3.8 or higher
- pip 20.0 or higher
- fastapi
- uvicorn
- pydantic
- jose
- passlib
- mysql

## Contributing

If you'd like to contribute to this project, please check the contribution guidelines for more information.

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
