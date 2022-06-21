import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        database="aitandata",
        user="root",
        password="TheLevys@Almagor2021" ,
        charset='utf8mb4' ,
        use_unicode=True,)

class GrowersDAL:
    def __init__(self):
        pass
   

    # ------------------------------------------------------

    def get_all_growers(self):
        growers_list=[]
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM growers")


        for row in cursor:
            new_dict={}
            new_dict={"grower": row[0], "is_active": row[1]}
            growers_list.append(new_dict)


        return growers_list