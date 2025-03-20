from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "../data/face-data.json"

# Load existing data or create an empty file
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({}, file)

def load_data():
    """Load face data from JSON file."""
    try:
        if not os.path.exists(DATA_FILE):
            print(f"{DATA_FILE} not found. Returning empty data.")
            return {}  # Return an empty dictionary if the file doesn't exist

        with open(DATA_FILE, "r") as file:
            # Check if the file is empty
            if file.read(1):
                # Not empty, go back to the beginning of the file
                file.seek(0)
                return json.load(file)  # Try loading the JSON data
            else:
                print(f"{DATA_FILE} is empty. Returning empty data.")
                return {}  # Return an empty dictionary if the file is empty

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return {}  # Return an empty dictionary if there is a decoding error
    except Exception as e:
        print(f"Error loading data from {DATA_FILE}: {e}")
        return {}  # Return an empty dictionary if something goes wrong

def save_data(data):
    """Save face data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def calculate_similarity(person, data):
    """Checks if the person's data is similar to already existing data"""
    for person_id, features in data.items():
        total_similarity = 0  # Track the total similarity for the current face
        
        # Loop through each feature and calculate the similarity
        for feature, value in features.items():
            if feature in person:
                similarity = abs(person[feature] - value)
                if similarity > 1:  # If similarity is too large, we ignore it
                    total_similarity += similarity
        
        # Check if total similarity for this person exceeds the threshold
        if total_similarity < 5:  # Adjust this threshold as needed
            return True  # Face is similar enough, we reject it

    return False  # No similar face found


@app.route("/")
def home():
    return "Face Data API is Running!"

@app.route("/save_face", methods=["POST"])
def save_face():
    """Save facial feature data to the database."""
    if request.content_type != "application/json":
        return jsonify({"error": "Request must be JSON"}), 400

    try:
        data = request.json  # Expecting JSON input
        if data is None:
            raise ValueError("Invalid JSON data")
        
        print(f"Received data: {data}")  # Print the incoming data for debugging

        # Load existing data
        face_data = load_data()
        
        # Check if any existing data is similar to the incoming face
        if len(face_data) >= 1:
            if calculate_similarity(data, face_data):
                print(f"This person is too similar to another / already exists")
                return jsonify({"error": "This person is too similar to another / already exists"}), 501

            else:
                # Generate a unique ID for the new entry
                person_id = f"person_{len(face_data) + 1}"
                face_data[person_id] = data

                save_data(face_data)
                return jsonify({"message": "Face data saved!", "id": person_id}), 201
            
        else:
            # If no existing data, save the first person
            person_id = f"person_{len(face_data) + 1}"
            face_data[person_id] = data

            save_data(face_data)
            return jsonify({"message": "Face data saved!", "id": person_id}), 201
    
    except Exception as e:
        print(f"Error saving face data: {e}")
        return jsonify({"error": "Error saving face data", "message": str(e)}), 500

@app.route("/get_faces", methods=["GET"])
def get_faces():
    """Retrieve all saved face data."""
    face_data = load_data()
    return jsonify(face_data)

@app.route("/check_face", methods=["POST"])
def check_face():
    """Check if face data already exists."""
    data = request.json
    face_data = load_data()

    for person_id, features in face_data.items():
        if features == data:
            return jsonify({"message": f"Match found: {person_id}"}), 200

    return jsonify({"message": "No match found"}), 404

if __name__ == "__main__":
    app.run(debug=True)