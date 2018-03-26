import werkzeug
from flask import render_template, request
from requests.exceptions import MissingSchema

import get_data
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/get_info', methods=['GET', 'POST'])
def get_info():
    try:
        url = request.form['appURL']
        info = get_data.get_app_info(url)
        if not info[0]:
            e = "We couldn't find that app. Please check the url and try again"
            return render_template('index.html', error=e)
    except MissingSchema:
        e = 'Invalid URL, please check it and try again'
        return render_template('index.html', error=e)
    return render_template('index.html', info=info)


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return render_template('index.html', error="Bad request"), 400


@app.errorhandler(404)
def not_found(e):
    return render_template('index.html', error="Url not found"), 404

app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, not_found)
