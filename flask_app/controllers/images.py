from flask import redirect, render_template, request, flash
from flask_app import app
from flask_app.models import image
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '../static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(imageName):
    return '.' in imageName and imageName.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template("index.html")

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

    if image and allowed_file(image.filename):
        print('------SUCCESS------')
        print(image)
        imageName = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], imageName))

    return redirect('/')