import config
from dao.disease_dao import DiseaseDAO

dao = DiseaseDAO(
    host=config.get("database", "database.host"),
    user=config.get("database", "database.user"),
    password=config.get("database", "database.password"),
    database=config.get("database", "database.dbname")
)
dao.connect()


def get_disease_details(disease):
    try:
        (disease_id, disease_name, symptoms, treatment) = dao.query_disease(disease)
        return symptoms, treatment
    except TypeError:
        return None


def add_disease(disease, symptoms, treatment) -> bool:
    if get_disease_details(disease) is None:
        dao.insert_new_disease(disease, symptoms, treatment)
        return True
    else:
        return False


def get_all_diseases():
    diseases = dao.get_all()
    return_list = []
    for d in diseases:
        return_list.append(d[0])
    return return_list
