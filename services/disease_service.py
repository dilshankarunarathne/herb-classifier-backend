from dao.disease_dao import DiseaseDAO

dao = DiseaseDAO(host="localhost", user="root", password="", database="herb")
dao.connect()


def get_disease_details(disease):
    (disease_id, disease_name, symptoms, treatment) = dao.query_disease(disease)
    return symptoms, treatment


def get_all_diseases():
    diseases = dao.get_all()
    return_list = []
    
