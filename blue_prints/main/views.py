from flask import Blueprint, render_template, session, request

main = Blueprint('main', __name__, static_folder='statics', template_folder='templates')

# Views
@main.route('/')
def index():
    css = ['main.css', 'bootstrap.min.css', 'load/component.css']
    js = ['fb_sdk.js', 'fb_login.js', 'popper.min.js', 'bootstrap.min.js', 'holder.min.js', 'load/modernizr.custom.js', 'load/classie.js', 'load/cbpScroller.js']
    return render_template('main/index.html', js = js, css = css, session = session)

@main.route('/program')
def program():
    css = ['main.css', 'bootstrap.min.css', 'scroll/component.css', 'scroll/default.css']
    js = ['fb_sdk.js', 'fb_login.js', 'scroll/modernizr.custom.js', 'scroll/jquery.easing.min.js', 'scroll/waypoints.min.js', 'scroll/jquery.debouncedresize.js', 'scroll/cbpFixedScrollLayout.min.js', 'main.js']
    return render_template('main/program.html', js = js, css = css, session = session)