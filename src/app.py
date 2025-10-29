"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Crear la instancia de la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Endpoint 1: GET todos los miembros
@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

# Endpoint 2: GET un miembro específico por ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        
        if member is None:
            return jsonify({"error": "Member not found"}), 404
        
        return jsonify(member), 200
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

# Endpoint 3: POST agregar un nuevo miembro
@app.route('/members', methods=['POST'])
def add_member():
    try:
        # Obtener los datos del request body
        body = request.get_json()
        
        # Validar que se recibió información
        if body is None:
            return jsonify({"error": "Request body is required"}), 400
        
        # Validar campos requeridos
        if "first_name" not in body:
            return jsonify({"error": "first_name is required"}), 400
        
        if "age" not in body:
            return jsonify({"error": "age is required"}), 400
        
        if "lucky_numbers" not in body:
            return jsonify({"error": "lucky_numbers is required"}), 400
        
        # Agregar el miembro
        new_member = jackson_family.add_member(body)
        
        return jsonify(new_member), 200
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

# Endpoint 4: DELETE eliminar un miembro
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        deleted_member = jackson_family.delete_member(member_id)
        
        if deleted_member is None:
            return jsonify({"error": "Member not found"}), 404
        
        return jsonify({"done": True}), 200
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)