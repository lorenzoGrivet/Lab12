from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNazioni():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=False)

        query="""select distinct Country 
                from go_sales.go_retailers gr 
                """
        cursor.execute(query)

        risultato=[]
        for a in cursor:
            risultato.append(a[0])

        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getAllAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        query = """select distinct year( `Date` )
                    from go_sales.go_daily_sales gds 
                        """
        cursor.execute(query)

        risultato = []
        for a in cursor:
            risultato.append(a[0])

        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getRetailers(anno,nazione):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select gr.Retailer_code, gr.Retailer_name, gr.`Type` , gr.Country
                from go_sales.go_retailers gr , go_sales.go_daily_sales gds 
                where gr.Retailer_code =gds.Retailer_code and year (gds.`Date`)=%s and gr.Country =%s"""

        cursor.execute(query,(anno,nazione,))

        risultato = []

        for a in cursor:
            risultato.append(Retailer(**a))

        cursor.close()
        cnx.close()
        return risultato
