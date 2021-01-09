from flask import render_template, request
from app import app

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    print(request)
    if request.method == 'POST':
        result = float(request.form['quantity'])
        print(result)
    else:
        result = 0

    site_info = {'store_name': 'TEST', 'bundle_name': 'TEST', 'bundle_description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."}

    return render_template('indexStyles.html', result=result, site_info=site_info)