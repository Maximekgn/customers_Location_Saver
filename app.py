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

# Initialize database for each request in Vercel environment
@app.before_request
def before_request():
    if os.environ.get('VERCEL_REGION') is not None:
        with app.app_context():
            db.create_all()
            # Only add sample data if the table is empty
            if Location.query.count() == 0:
                sample_locations = [
                    Location(name="Paris", latitude=48.8566, longitude=2.3522),
                    Location(name="London", latitude=51.5074, longitude=-0.1278)
                ]
                db.session.add_all(sample_locations)
                db.session.commit()

# Create tables for local development
if os.environ.get('VERCEL_REGION') is None:
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    return redirect(url_for('add_location'))

# Route pour enregistrer une géolocalisation
@app.route('/add', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        try:
            name = request.form['name']
            latitude = float(request.form['latitude'])
            longitude = float(request.form['longitude'])

            new_location = Location(name=name, latitude=latitude, longitude=longitude)
            db.session.add(new_location)
            db.session.commit()
            return redirect(url_for('map'))
        except Exception as e:
            return str(e), 500

    return render_template('form.html')

@app.route('/map')
def map():
    try:
        locations = Location.query.all()
        locations_list = [location.to_dict() for location in locations]
        return render_template('map.html', locations=locations_list)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
