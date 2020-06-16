from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector


mydb = mysql.connector.connect(
  host="ifar.ayz.pl",
  user="ifar_gda24",
  password="Testgda24z!",
  database="ifar_testgda24z"
)

app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        mycursor = mydb.cursor()
        select = "SELECT * FROM noblisci"
        mycursor.execute(select)
        max_ID = mycursor.fetchall()
        return max_ID

    def post(self):
        mycursor = mydb.cursor()
        req_data = request.get_json()

        imie = req_data['imie']
        nazwisko = req_data['nazwisko']
        dziedzina = req_data['dziedzina']
        rok = req_data['rok']
        kraj = req_data['kraj']
        wiek = req_data['wiek']

        sql = "INSERT INTO noblisci (id, imie, nazwisko, dziedzina, rok, kraj, wiek) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = [0, imie, nazwisko, dziedzina, rok, kraj, wiek]

        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception:
            select = "SELECT MAX(id) FROM noblisci"
            mycursor.execute(select)
            max_ID = mycursor.fetchall()[0][0]
            val[0] = int(max_ID) + 1
            mycursor.execute(sql, val)
            mydb.commit()
        return {'status': 'success'}

#
# {
#     "imie": "Stefan",
#     "nazwisko": "Stefanski",
#     "dziedzina": "Stefana",
#     "rok": "2000",
#     "kraj": "Stefano",
#     "wiek": "18"
# }
#

api.add_resource(Employees, '/employees')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')