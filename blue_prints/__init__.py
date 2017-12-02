from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_recaptcha import ReCaptcha
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_pyfile('config.py')

#Google Recaptcha
app.config.update({'RECAPTCHA_ENABLED': True,'RECAPTCHA_SITE_KEY':'6Ld_bC0UAAAAAHn7AcV3YdHD8wUM0wxMigsTs9x0','RECAPTCHA_SECRET_KEY':'6Ld_bC0UAAAAAOIQaaM7owbcREIwkbXFjA1YAJhv'})
recaptcha = ReCaptcha()
recaptcha.init_app(app)

#cstf protect
csrf = CSRFProtect()
csrf.init_app(app)

from blue_prints.main.views import main
app.register_blueprint(main)

from blue_prints.fb.views import fb
app.register_blueprint(fb, url_prefix='/fb')

from blue_prints.admin.views import admin
app.register_blueprint(admin, url_prefix='/admin')


