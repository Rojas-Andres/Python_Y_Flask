from flask import Flask, jsonify,render_template,request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

ALLOWED_EXTENSIONS = set(['PNG', 'jpg', 'jpeg', 'gif'])
def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True 
    return False

@app.route('/upload',methods=["POST"])
def upload():
    file = request.files['uploadFile']
    # Pásele un nombre de archivo y le devolverá una versión segura. 
    # Este nombre de archivo se puede almacenar de forma segura en un sistema de archivos normal y 
    # pasar a os.path.join()
    filename = secure_filename(file.filename)
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filenameimage = file.filename
        return render_template('upload_file.html',mensaje="archivo subido exitosamente")
    return render_template('upload_file.html',mensaje="No se subio el archivo")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")