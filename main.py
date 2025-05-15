# importiere Flask von dem Modul flask
from flask import Flask, jsonify, request

# initialisiere ein app-Objekt von der Klasse Flask
app = Flask(__name__)

## Haus in einer Liste speichern -> Local Storage
houses = [
    { "id": 1, "name": "single-familiy-house", "age": 5, "type": "wooden-house"},
    { "id": 2, "name": "multi-familiy-house", "age": 2, "type": "brick"}
    { "id": 3, "name": "villa", "age": 88, "type": "brick"}
]

## Test-Route für Startseite
@app.route("/")
def home():
    return "Hallo, das eine Haus-Api"

## GET-Route implementieren, d.h. Daten abrufen bzw. alle Häuser anzeigen
@app.route("/api/houses", methods=['GET'])
def show_houses():
    return jsonify(houses), 200

## POST-Route implementieren, d.h. neues Haus hinzufügen
@app.route("/api/houses", methods=['POST'])
def add_houses():
    ## Funktion um die Daten im JSON-Format aus dem Request-Objekt zu bekommen
    new_house = request.get_json() # Hole dir aus dem Request-Objekt die Daten im JSON-Format
    # { "id": 3, "name": .., "age": ..., "type": ...}

    houses.append(new_house) # hänge das Objekt im JSON-Format hinten dran
    return f"{new_house} wurde erfolgreich hinzugefügt", 201

## DELETE-Route, um ein Haus aus der Liste zu löschen
@app.route("/api/houses/<name>", methods=['DELETE'])
def delete_house(name):
    for house in houses:
        if house["name"] == name:
            houses.remove(house)
            return f"{name} wurde gelöscht", 200
    return f"{name} wurde nicht gefunden", 404

## Baue eine Funktion, zum Updaten
## PUT-Route -> Ersetze alle Eigenschaften eines Hauses (Eigenschaften im Body als JSON)
@app.route("/api/houses/<name>", methods=['PUT'])
def put_house(name):
    data = request.get_json() 
    
    for house in houses:
        if house["name"] == name:
            house.clear() # Lösche alle Werte des gefundenen Hauses
            house.update(data) # Werte, die im JSON-Format in der Variablen data gespeichert sind
            return f"{name} wurde geupdated", 200
    return f"{name} wurde nicht gefunden", 404


## PATCH-Route -> Ersetze spezifisch einzelne Eigenschaften, d.h. hier schicken wir nur die zu ändernden Eigenschaften im Body als JSON mit
@app.route("/api/houses/<name>", methods=["PATCH"])
def patch_house(name):
    data = request.get_json()
    for house in houses:
        if house["name"] == name:
            house.update(data)
            return f"{name} wurde geupdatet", 200
    return f"{name} wurde nicht gefunden", 404

# App starten
if __name__ == "__main__":
    app.run(debug=True)