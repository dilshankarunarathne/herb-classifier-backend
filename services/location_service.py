from dao.location_dao import LocationDAO

dao = LocationDAO(host="localhost", user="root", password="", database="herb")
dao.connect()


def add_location


def get_location(herb):
    return dao.get_location(herb)
