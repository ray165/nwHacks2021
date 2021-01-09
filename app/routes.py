from flask import render_template, request
from app import app

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    user = {'username': 'Kyle'}
    if request.method == 'POST':
        result = float(request.form['quantity'])
    else:
        result = 0

    return render_template('index.html', user=user, result=result)