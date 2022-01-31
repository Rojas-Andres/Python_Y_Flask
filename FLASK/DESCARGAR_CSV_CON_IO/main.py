from flask import Flask, jsonify,render_template,request,Response
from sqlalchemy import create_engine
import io
import csv 

app = Flask(__name__)

#postgresql://username:password@host:port/database
engine = create_engine('postgresql://postgres:postgres@localhost:5434/postgres')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/descargar_reporte')
def descargar_reporte():
    query = "SELECT * FROM datosfalsos"
    with engine.connect() as con:
        rs = con.execute(query)
    columns = ["Id,First_name,Last_name,email,gender,ip_address"]
    # Lo primero comprendamos el módulo stringIO (Python lee y escribe datos en la memoria.
    #  Los módulos utilizados son StringIO y BytesIO. 
    # StringIO solo puede ser str. Si desea manipular datos binarios, debe usar BytesIO)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(columns)
    for row in rs:
        cadena = f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}"
        linea = [cadena]
        writer.writerow(linea)
    # Nos paramos al inicio del archivo
    output.seek(0)
    return Response(output,mimetype="text/csv",headers={"Content-Disposition":"attachment;filename=reporte_personas.csv"})
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")