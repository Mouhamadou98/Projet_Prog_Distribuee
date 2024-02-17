from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

#app = Flask(__name__)
#CORS(app) 
# Exemple de données d'étudiants (utilisez une base de données dans un environnement de production)
# students = [
#     {"id": 1, "name": "John Doe", "age": 20},
#     {"id": 2, "name": "Jane Smith", "age": 22},
#     # Ajoutez plus d'étudiants si nécessaire
# ]

app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
api = Api(app)
# Configuration de la base de données PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gning:samb98@postgres:5432/postgresdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Route pour obtenir la liste complète des étudiants
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({"students": students})

# Route pour obtenir un étudiant spécifique par ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify({"student": student})
    else:
        return jsonify({"message": "Étudiant non trouvé"}), 404

# Route pour créer un nouvel étudiant
@app.route('/students', methods=['POST'])
def create_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify({"message": "Étudiant créé avec succès"}), 201

# Route pour mettre à jour un étudiant existant
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        updated_data = request.get_json()
        student.update(updated_data)
        return jsonify({"message": "Étudiant mis à jour avec succès"})
    else:
        return jsonify({"message": "Étudiant non trouvé"}), 404

# Route pour supprimer un étudiant
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Étudiant supprimé avec succès"})

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5003)