import config
from dao.disease_dao import DiseaseDAO

dao = DiseaseDAO(
    host=config.get("database", "database.dbhost"),
    user=config.get("database", "database.dbuser"),
    password=config.get("database", "database.dbpassword"),
    database=config.get("database", "database.dbname")
)
dao.connect()


def get_disease_details(disease):
    (disease_id, disease_name, symptoms, treatment) = dao.query_disease(disease)
    return symptoms, treatment


def get_all_diseases():
    diseases = dao.get_all()
    return_list = []
    for d in diseases:
        return_list.append(d[0])
    return return_list
