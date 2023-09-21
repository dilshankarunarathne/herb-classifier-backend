from dao.disease_dao import DiseaseDAO

dao = DiseaseDAO(host="localhost", user="root", password="", database="herb")
dao.connect()


print(dao.get_all())
