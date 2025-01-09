from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Location(db.Model):
    # Définition des colonnes de la base de données
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Nom de la localisation
    latitude = db.Column(db.Float, nullable=False)  # Latitude de la localisation
    longitude = db.Column(db.Float, nullable=False)  # Longitude de la localisation

    def to_dict(self):
        # Convertit l'objet Location en un dictionnaire
        return {
            'id': self.id,
            'name': self.name,
            'latitude': float(self.latitude),
            'longitude': float(self.longitude)
        }

    def __repr__(self):
        # Représentation de l'objet Location sous forme de chaîne de caractères
        return f"<Location {self.name}>"
