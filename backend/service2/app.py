from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gning:samb98@postgres:5432/postgresdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Exemple de données d'absences (utilisez une base de données dans un environnement de production)
# absences = [
#     {"id": 1, "student_id": 1, "date": "2024-01-21", "reason": "Maladie"},
#     {"id": 2, "student_id": 2, "date": "2024-01-22", "reason": "Rendez-vous médical"},
#     # Ajoutez plus d'absences si nécessaire
# ]
db = SQLAlchemy(app)

class Absence(db.Model):
    __tablename__ = 'absences'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    
# Route pour obtenir la liste complète des absences
@app.route('/absences', methods=['GET'])
def get_absences():
    return jsonify({"absences": absences})

# Route pour obtenir une absence spécifique par ID
@app.route('/absences/<int:absence_id>', methods=['GET'])
def get_absence(absence_id):
    absence = next((a for a in absences if a["id"] == absence_id), None)
    if absence:
        return jsonify({"absence": absence})
    else:
        return jsonify({"message": "Absence non trouvée"}), 404

# Route pour créer une nouvelle absence
@app.route('/absences', methods=['POST'])
def create_absence():
    new_absence = request.get_json()
    absences.append(new_absence)
    return jsonify({"message": "Absence créée avec succès"}), 201

# Route pour mettre à jour une absence existante
@app.route('/absences/<int:absence_id>', methods=['PUT'])
def update_absence(absence_id):
    absence = next((a for a in absences if a["id"] == absence_id), None)
    if absence:
        updated_data = request.get_json()
        absence.update(updated_data)
        return jsonify({"message": "Absence mise à jour avec succès"})
    else:
        return jsonify({"message": "Absence non trouvée"}), 404

# Route pour supprimer une absence
@app.route('/absences/<int:absence_id>', methods=['DELETE'])
def delete_absence(absence_id):
    global absences
    absences = [a for a in absences if a["id"] != absence_id]
    return jsonify({"message": "Absence supprimée avec succès"})

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5004)