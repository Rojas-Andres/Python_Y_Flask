from flask import Flask, jsonify,render_template,request,Response
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
#postgresql://username:password@host:port/database
engine = create_engine('postgresql://postgres:postgres@localhost:5434/postgres')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/descargar_reporte')
def descargar_reporte():
    query = "SELECT * FROM DatosFalsos"
    df = pd.read_sql_query(query,con=engine)
    df.set_index('id', inplace = True)
    return Response(df.to_csv(), mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=personas.csv"})
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")