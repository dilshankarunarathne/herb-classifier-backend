import configparser 

config = configparser .RawConfigParser()
config.read('application.properties')

print(config.get('DatabaseSection', 'database.dbname'))
