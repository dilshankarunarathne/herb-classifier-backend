from dao.location_dao import LocationDAO

dao = LocationDAO(host="localhost", user="root", password="", database="herb")
dao.connect()


def add_location(lon, lat, herb):
    dao.add_location(lon, lat, herb)


def get_location(herb):
    herbs = dao.get_location_by_herb(herb)
    return_list = []
    for d in herbs:
        return_list.append(d[0])
    return return_list
