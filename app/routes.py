from flask import render_template, request
from app import app

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    print(request)
    itemPrice = 5
    if request.method == 'POST':
        result = float(request.form['quantity'])
        print(result)
    else:
        result = 0

    site_info = {'store_name': 'TEST', 'bundle_name': 'TEST', 'bundle_description': "Dont stress about tonight's "
                                                                                    "winter dinner! Friends and "
                                                                                    "family can snuggle up to the "
                                                                                    "warmth of this mouthwatering "
                                                                                    "ramen. Staff picked, "
                                                                                    "this celebrated bundle consists "
                                                                                    "of marbleized lamb, pork, "
                                                                                    "and beef slices. Paired with "
                                                                                    "fresh vegetables and Ichiran "
                                                                                    "ramen, tonight's dinner hassle "
                                                                                    "is covered by us!"}
    return render_template('indexStyles.html', result=result*itemPrice, site_info=site_info)