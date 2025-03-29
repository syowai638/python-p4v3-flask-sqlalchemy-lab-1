# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify
from models import db, Earthquake

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///earthquakes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize db with the app
db.init_app(app)

# Ensure tables are created before running the server
with app.app_context():
    db.create_all()

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    earthquake = db.session.get(Earthquake, id)  # ✅ Use db.session.get()
    if earthquake:
        return jsonify({
            "id": earthquake.id,
            "magnitude": earthquake.magnitude,
            "location": earthquake.location,
            "year": earthquake.year
        }), 200
    return jsonify({"message": f"Earthquake {id} not found."}), 404  # ✅ Fix message key


@app.route('/earthquakes/magnitude/<magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    try:
        magnitude = float(magnitude)  # Convert string to float manually
    except ValueError:
        return jsonify({"error": "Invalid magnitude"}), 400

    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return jsonify({
        "count": len(earthquakes),
        "quakes": [{"id": eq.id, "magnitude": eq.magnitude, "location": eq.location, "year": eq.year} for eq in earthquakes]
    }), 200
