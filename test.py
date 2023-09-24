import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('application.properties')

print config.get('DatabaseSection', 'database.dbname');
