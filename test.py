from dao.disease_dao import DiseaseDAO

dao = DiseaseDAO(host="localhost", user="root", password="", database="herb")


def get_disease_details(disease):
    dao.query_disease(disease)