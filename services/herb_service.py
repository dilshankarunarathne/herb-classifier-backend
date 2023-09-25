from dao.herb_dao import HerbDAO

dao = HerbDAO(
    host=config.get("database", "database.host"),
    user=config.get("database", "database.user"),
    password=config.get("database", "database.password"),
    database=config.get("database", "database.dbname")
)
dao.connect()


def get_disease_by_herb(herb):
    diseases = dao.get_disease(herb)
    return_list = []
    for d in diseases:
        return_list.append(d[0])
    return return_list


def get_herb_by_disease(disease):
    herbs = dao.get_herb(disease)
    return_list = []

    if herbs is None:
        raise TypeError("returned data is null")

    for d in herbs:
        return_list.append(d[0])
    return return_list
