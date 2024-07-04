from flask import Flask
from flask_restful import Api
from resources import ProductResource, ProductListResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
