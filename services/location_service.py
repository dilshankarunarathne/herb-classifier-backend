from config import config
from dao.location_dao import LocationDAO

dao = LocationDAO(
    host=config.get("database", "database.host"),
    user=config.get("database", "database.user"),
    password=config.get("database", "database.password"),
    database=config.get("database", "database.dbname")
)
dao.connect()


def add_location(lon, lat, herb, added_user):
    dao.add_location(lon, lat, herb, added_user)


# def get_location(herb):
#     herbs = dao.get_location_by_herb(herb)
#     return_list = []
#     for h in herbs:
#         return_list.append({h[1], h[2], h[4]})
#     return return_list


def get_location(herb):
    herbs = dao.get_location_by_herb(herb)
    return_list = []
    for h in herbs:
        val_dict = {'id': h[0], 'longitude': h[1], 'latitude': h[2], 'herb': h[3], 'added user': h[4]}
        return_list.append(val_dict)
    return return_list
