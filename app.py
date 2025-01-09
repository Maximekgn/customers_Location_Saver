from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Check if running on Vercel
if os.environ.get('VERCEL_REGION') is not None:
    # Use in-memory SQLite database when on Vercel
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
else:
    # Use file-based SQLite database when running locally
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db, Location

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()
    # Add some sample data when running on Vercel (since it's in-memory)
    if os.environ.get('VERCEL_REGION') is not None:
        sample_locations = [
            Location(name="Paris", latitude=48.8566, longitude=2.3522),
            Location(name="London", latitude=51.5074, longitude=-0.1278)
        ]
        db.session.add_all(sample_locations)
        db.session.commit()

@app.route('/')
def home():
    return redirect(url_for('add_location'))

# Route pour enregistrer une géolocalisation
@app.route('/add', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        name = request.form['name']
        latitude = float(request.form['latitude'])  # Convert to float
        longitude = float(request.form['longitude'])  # Convert to float

        # Enregistrer les données dans la base
        new_location = Location(name=name, latitude=latitude, longitude=longitude)
        db.session.add(new_location)
        db.session.commit()
        return redirect(url_for('map'))

    return render_template('form.html')

# Route pour afficher la carte
@app.route('/map')
def map():
    locations = Location.query.all()
    locations_list = [location.to_dict() for location in locations]  # Convert to list of dicts
    return render_template('map.html', locations=locations_list)

if __name__ == '__main__':
    app.run(debug=True)
