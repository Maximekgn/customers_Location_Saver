from flask import Flask, request, jsonify, render_template_string
from geopy.geocoders import Nominatim
import folium

app = Flask(__name__)

# Initialisation de Geopy
geolocator = Nominatim(user_agent="geoapiExercises")

# Route pour enregistrer un client avec ses coordonnées de géolocalisation
@app.route('/register_client', methods=['POST'])
def register_client():
    data = request.json
    address = data.get('address')
    location = geolocator.geocode(address)
    if location:
        client_data = {
            'address': address,
            'latitude': location.latitude,
            'longitude': location.longitude
        }
        # Enregistrez les données du client dans votre base de données ici
        return jsonify(client_data), 201
    else:
        return jsonify({'error': 'Adresse non trouvée'}), 400

# Route pour afficher les coordonnées sur une carte
@app.route('/map')
def map_view():
    # Exemple de données de clients (à remplacer par les données de votre base de données)
    clients = [
        {'address': 'Paris, France', 'latitude': 48.8566, 'longitude': 2.3522},
        {'address': 'New York, USA', 'latitude': 40.7128, 'longitude': -74.0060}
    ]

    # Création de la carte
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=2)

    # Ajout des marqueurs pour chaque client
    for client in clients:
        folium.Marker([client['latitude'], client['longitude']], popup=client['address']).add_to(m)

    # Sauvegarde de la carte dans un fichier HTML
    m.save('templates/map.html')

    # Rendu de la carte
    return render_template_string('<iframe src="/static/map.html" width="100%" height="600px"></iframe>')

if __name__ == '__main__':
    app.run(debug=True)
