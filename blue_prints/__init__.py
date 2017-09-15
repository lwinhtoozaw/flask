from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from blue_prints.main.views import main
from blue_prints.fb.views import fb

app.register_blueprint(main)
app.register_blueprint(fb, url_prefix='/fb')