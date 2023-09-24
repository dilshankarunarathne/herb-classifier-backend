import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

print config.get('DatabaseSection', 'database.dbname');
