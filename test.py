from dao.disease_dao import DiseaseDAO

dao = DiseaseDAO(host="localhost", user="root", password="", database="herb")
dao.connect()


def get_disease_details(disease):
    (id, disease_name, symptoms, treatment) = dao.query_disease(disease)


print(get_disease_details("semgedi"))
