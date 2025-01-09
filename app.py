from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importer le modèle
from models import Location

@app.route('/')
def home():
    return redirect(url_for('add_location'))

# Route pour enregistrer une géolocalisation
@app.route('/add', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        name = request.form['name']
        latitude = request.form['latitude']
        longitude = request.form['longitude']

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
    return render_template('map.html', locations=locations)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
