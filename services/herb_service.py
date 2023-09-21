from dao.herb_dao import HerbDAO

dao = HerbDAO(host="localhost", user="root", password="", database="herb")
dao.connect()