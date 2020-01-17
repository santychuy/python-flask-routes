from flask import Flask, jsonify
from products import products

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({ "message": "Empieza" })

@app.route('/products')
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    return jsonify(product_found)

if __name__ == "__main__":
    app.run(debug=True, port=3000)