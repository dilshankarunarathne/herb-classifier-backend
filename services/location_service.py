from dao.herb_dao import HerbDAO
from dao.location_dao import LocationDAO

dao = LocationDAO(host="localhost", user="root", password="", database="herb")
dao.connect()
