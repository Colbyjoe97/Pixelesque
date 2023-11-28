import os
from flask import redirect, render_template, request, flash, url_for
from flask_app import app
from flask_app.models.image import Image
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(imageName):
    return '.' in imageName and imageName.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template("index.html", all_images = Image.get_all())

@app.route('/upload', methods=['POST'])
def upload_image():
    print(request.files['image'])
    if 'image' not in request.files:
        flash("No image selected")
        return redirect('/')
    
    image = request.files['image']
    if image.filename == "":
        flash("No image selected")
        return redirect('/')
    
    if not allowed_file(image.filename):
        flash("File type not accepted!")
        return redirect('/')

    if image and allowed_file(image.filename):
        print('------SUCCESS------')
        data = {
            'image': image.filename
        }
        dbImg = Image.save(data)
        imageName = str(dbImg) + '-' + secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(imageName)))
    return redirect('/')


@app.route('/delete/<int:id>/<string:imgName>')
def delete(id, imgName):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(str(id)+'-'+imgName)))
    Image.delete({'id': id})
    return redirect('/')

@app.route('/delete/all')
def deleteAll():
    Image.deleteAll()
    return redirect('/')