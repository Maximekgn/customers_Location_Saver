from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db, Location

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

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
