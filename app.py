from flask import Flask , render_template, flash, request, redirect, url_for
from werkzeug.wrappers import response
import model as m
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = 'hiteshwar'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


ALLOWED_EXT=set(['png','jpg','jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXT


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/", methods=["GET",
                         "POST"])
def upload_image():
    if request.method=='POST':
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        filename = request.files['file']
        if filename.filename == '':
            flash("No image selected for uploading")
            return redirect(request.url)

        if filename and allowed_file(filename.filename):
            name = filename.filename
            driver_pred = m.detect(name)
            drp = driver_pred

            return render_template('index.html',filename = filename, pred = drp)
        else:
            flash('Allowed types png and jpeg')
            return redirect(request.url)

# @app.route('/display/<filename>')
# def display_image(filename):
#     return redirect(url_for('static',filename='uploads/'+filename),code=301)


if __name__ == "__main__":
    app.run(debug=True)

    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
