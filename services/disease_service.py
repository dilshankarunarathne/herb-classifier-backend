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
    (disease_id, disease_name, symptoms, treatment) = dao.query_disease(disease)
    return symptoms, treatment


def insert_disease(disease, symptoms, treatment):
    dao.insert_new_disease(disease, symptoms, treatment)


def get_all_diseases():
    diseases = dao.get_all()
    return_list = []
    for d in diseases:
        return_list.append(d[0])
    return return_list
