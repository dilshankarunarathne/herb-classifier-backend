# Setup MySQL database

1. Install MySQL (version 5.7.31 is recommended)  
[WAMP](https://sourceforge.net/projects/wampserver) or [XAMPP](https://www.apachefriends.org/download.html) can be used to install MySQL on Windows.

2. Create a database for the application with the name `herb` and grant all privileges to a user with the name `root`.

```mysql
CREATE DATABASE herb;
```

If you want to use a different database name or a different user name, you can change the database configurations in the `config.py` file in the root directory of the project.

3. Import the database dump from `herb.sql` file in the root directory of the project.
You can find the `herb.sql` file in the [Resources](/resources/herb.sql) directory of the project.

# Get the project

1. Clone the project from GitHub.

```bash
git clone https://github.com/dilshankarunarathne/herb-classifier-backend.git
```

2. And then change the directory to the project root.

```bash
cd herb-classifier-backend
```

# Setup the environment

1. Install Python 3.11

Visit [https://www.python.org/downloads/](https://www.python.org/downloads/release/python-3110/) to download and install Python 3.11.

2. Install the dependencies using `requirements.txt` file.

```bash
pip install -r requirements.txt
```

3. Make sure to install this
```bash
pip install git+ https://github.com/yuce/pyswip@master#egg=pyswip
```

