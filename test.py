from dao.disease_dao import DiseaseDAO

dao = DiseaseDAO(host="localhost", user="root", password="", database="herb")
dao.connect()

def get_disease_details(disease):
    return dao.query_disease(disease)


for i in get_disease_details("semgedi"):
    print(i)
