from dao.location_dao import LocationDAO

dao = LocationDAO(host="localhost", user="root", password="", database="herb")
dao.connect()


def add_location(lon, lat, herb):
    dao.add_location(lon, lat, herb)


def get_location(herb):
    
