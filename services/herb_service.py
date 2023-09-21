from dao.herb_dao import HerbDAO

dao = HerbDAO(host="localhost", user="root", password="", database="herb")
dao.connect()


def get_disease_by_herb(herb):
    diseases = dao.get_disease(herb)
    return_list = []
    for d in diseases:
        return_list.append(d[0])
    return return_list


def get_herb_by_disease(disease):
    herbs = dao.get_disease(herb)
    return_list = []
    for d in herbs:
        return_list.append(d[0])
    return return_list
