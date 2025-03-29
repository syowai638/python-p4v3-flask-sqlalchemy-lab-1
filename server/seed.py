#!/usr/bin/env python3
# server/seed.py

from app import app  # Ensure we import app
from models import db, Earthquake

with app.app_context():
    try:
        print("Creating tables if they don't exist...")
        db.create_all()  # Ensure tables exist before inserting data

        print("Clearing old data...")
        db.session.query(Earthquake).delete()

        earthquakes = [
            {"magnitude": 9.5, "location": "Chile", "year": 1960},
            {"magnitude": 9.2, "location": "Alaska", "year": 1964},
            {"magnitude": 8.6, "location": "Alaska", "year": 1946},
            {"magnitude": 8.5, "location": "Banda Sea", "year": 1934},
            {"magnitude": 8.4, "location": "Chile", "year": 1922}
        ]

        print("Seeding database...")
        db.session.bulk_insert_mappings(Earthquake, earthquakes)

        db.session.commit()
        print("Database seeded successfully!")

    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {e}")

    finally:
        db.session.close()
