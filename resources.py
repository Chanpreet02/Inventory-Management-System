from flask_restful import Resource, reqparse
from models import products, Product

product_parser = reqparse.RequestParser()
product_parser.add_argument('name', type=str, required=True, help="Name of the product is required")
product_parser.add_argument('price', type=float, required=True, help="Price of the product is required")
product_parser.add_argument('quantity', type=int, required=True, help="Quantity of the product is required")

class ProductResource(Resource):
    def get(self, product_id):
        product = next((p for p in products if p.product_id == product_id), None)
        if product:
            return product.__dict__, 200
        return {"message": "Product not found"}, 404

    def delete(self, product_id):
        global products
        products = [p for p in products if p.product_id != product_id]
        return {"message": "Product deleted"}, 200

    def put(self, product_id):
        args = product_parser.parse_args()
        product = next((p for p in products if p.product_id == product_id), None)
        if product:
            product.name = args['name']
            product.price = args['price']
            product.quantity = args['quantity']
            return product.__dict__, 200
        return {"message": "Product not found"}, 404

class ProductListResource(Resource):
    def get(self):
        return [product.__dict__ for product in products], 200

    def post(self):
        args = product_parser.parse_args()
        product_id = len(products) + 1
        new_product = Product(product_id, args['name'], args['price'], args['quantity'])
        products.append(new_product)
        return new_product.__dict__, 201
