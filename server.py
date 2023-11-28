from flask_app import app
from flask_app.controllers import images

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

if __name__ == "__main__":
    app.run(debug=True)