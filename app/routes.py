from flask import render_template, request
from app import app

total_cart_value = 0
@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    global total_cart_value
    itemPrice = 5
    if request.method == 'POST':
        result = int(request.form['quantity'])
        total_cart_value += result
    else:
        result = 0

    site_info = {'store_name': 'Asian Grocery', 'bundle_name': 'TEST', 'bundle_description': "Don't stress about tonight's "
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
    bullet_points = ["lamb", "pork", "beef slices", "fresh vegetables", "Ichiran ramen"]
    return render_template('indexStyles.html', total_cart_value=total_cart_value, itemPrice=itemPrice, site_info=site_info, bullet_points=bullet_points)