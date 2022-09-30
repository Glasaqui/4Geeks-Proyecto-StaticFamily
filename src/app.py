"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

familyarreglo = [
    {
        "id":1,
        "age": 33,
        "first_name": "John",
        "lucky_numbers": [7, 13,22]
    },
    {
        "id":2,
        "age": 35,
        "first_name": "Jane",
        "lucky_numbers": [10, 14,3]
    },
    {
        "id":3,
        "age": 5,
        "first_name": "Jimmy",
        "lucky_numbers": [1]
    }
]

# create the jackson family object
#jackson_family = FamilyStructure("Jackson")
# create the jackson family object
jackson_family = FamilyStructure("Jackson",familyarreglo)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
       
        "family": members
    }


    return jsonify(response_body), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_a_member(id):
    
    # Obtener un solo miembro de la familia Jackson

    member = jackson_family.get_member(id)
    
    if member is None:
        return jsonify('No encontrado'),404
    return jsonify(member),200
   
@app.route('/member', methods=['POST'])
def add_a_member():
    member= json.loads(request.data)
    jackson_family.add_member(member)

    return jsonify({"msg": "success"}), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_a_member(id):
    jackson_family.delete_member(id)
    return jsonify({"done": True}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
