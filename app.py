from flask import Flask, request, redirect, render_template, Response
from backend import knn_search
import json
import os
from werkzeug.utils import secure_filename


# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        print("File: "+file.filename)
        k = request.form['k']
        print("K: "+k)

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            knn_search(file, int(k))
            print(filename)
            return render_template("index.html", filename=filename)

    # If no valid image file was uploaded, show the file upload form:
    return render_template("index.html")

@app.route('/galeria', methods=['GET'])
def sendjson():
    print("Asked for JSON.")
    with open('static/json/import.json') as f:
        galeria = json.load(f)
    return Response(json.dumps(galeria), mimetype='application/json')

if __name__ == "__main__":
    app.run()
