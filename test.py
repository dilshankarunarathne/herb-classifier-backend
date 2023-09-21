from dao.disease_dao import DiseaseDAO
from services.disease_service import get_all_diseases

dao = DiseaseDAO(host="localhost", user="root", password="", database="herb")
dao.connect()


print(get_all_diseases())
