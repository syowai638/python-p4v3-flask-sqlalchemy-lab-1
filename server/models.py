from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Define metadata
metadata = MetaData()

# Initialize database with metadata
db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)  # Added max length
    year = db.Column(db.Integer, nullable=False)

    # Serialization rules (optional)
    serialize_rules = ('-metadata',)  # Avoids unnecessary data exposure

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
