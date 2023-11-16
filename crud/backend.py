
from flask import Flask
from flask_restful import Api
from endpoints.products import Products
from endpoints.health import Health

app = Flask(__name__)
api = Api(app)

api.add_resource(Products, '/products', '/products/<id>')
api.add_resource(Health, '/health')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
