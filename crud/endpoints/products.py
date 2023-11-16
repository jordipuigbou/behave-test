import json
from pymongo import MongoClient
from bson import json_util, ObjectId
from flask import request
from flask_restful import Resource

def parse_json(data):
    return json.loads(json_util.dumps(data))

class Products(Resource):
    client = MongoClient('mongodb://mongo:27017/', username='root', password='example')
    db = client["products"]

    def get(self, id=None):
        products = []
        try:
            if id is not None:
                products = self.db.products.find({"_id": ObjectId(id)})
            else:
                products = self.db.products.find({})
            products = list(products)
            products = parse_json(products)
            return products, 200
        except:
            return {"status": "error reading products"}, 500

    def post(self):
        json_data = request.get_json(force=True)
        try:
            self.db.products.insert_one(json_data)
            return {"status": "product inserted"}, 200
        except:
            return {"status": "product not insterted"}, 500

    def put(self, id=None):
        if id is None:
            return {"status": "product not updated"}, 500
        json_data = request.get_json(force=True)
        try:
            self.db.products.update_one({"_id": ObjectId(id)}, {"$set": json_data})
            return {"status": "product updated"}, 200
        except:
            return {"status": "product not updated"}, 500

    def delete(self, id):
        if id is None:
            return {"status": "product not deleted because id is not provided"}, 500
        try:
            self.db.products.delete_one({"_id": ObjectId(id)})
            return {"status": f"product {id} deleted"}, 200
        except:
            return {"status": "product not deleted"}, 500