import cv2
import dlib
import requests
from scipy.spatial.distance import euclidean

### NOTE ###
#0 - 16: Jawline  
#17 - 21: Right Eyebrow  
#22 - 26: Left Eyebrow  
#27 - 30: Nose Bridge  
#31 - 35: Nostrils  
#36 - 41: Right Eye  
#42 - 47: Left Eye  
#48 - 59: Outer Lips  
#60 - 67: Inner Lips  
############

class FaceTracking:
    
    IP_ADDR = "127.0.0.1"
    API_URL = f"http://{IP_ADDR}:5000"
    
    def __init__(self):
        # Initialize the camera, face detector, and predictor
        self.cap = cv2.VideoCapture(1)  # Adjust to your camera device
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("../models/shape_predictor_68_face_landmarks.dat")
        self.is_idle = True
        self.faces_detected = False

    def detect_faces(self, frame):
        """Detect faces and draw landmarks."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        if len(faces) >= 1:
            self.faces_detected = True
            for face in faces:
                self.landmarks = self.predictor(gray, face)
            
                # Draw landmarks on the frame
                for n in range(0, 68):  # Draw landmarks
                    x, y = self.landmarks.part(n).x, self.landmarks.part(n).y
                    if n == 39 or n == 42:
                        cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
                    elif n == 27 or n == 30:
                        cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
                    elif n == 31 or n == 35:
                        cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
                    elif n == 1 or n == 15:
                        cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
                    elif n == 48 or n == 54:
                        cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
                    else:
                        cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        
        else:
            self.faces_detected = False
        
        return frame

    def calculate_distance(self, point1, point2):
        """Calculate the Euclidean distance between two points."""
        return float(euclidean((point1.x, point1.y), (point2.x, point2.y)))
    
    def idle_mode(self):
        """Detect faces continuously in idle mode."""
        ret, frame = self.cap.read()
        if ret:
            frame = self.detect_faces(frame)  # Detect faces and draw landmarks
            cv2.imshow("Face Tracking", frame)  # Display the frame
        else:
            print("Failed to capture image.")
    
    def access_face_data(self):
        """Obtain the data stored within face-data.json"""
        print("Accessing face-data.json...")
        face_data = requests.get(url=f"{FaceTracking.API_URL}/get_faces")
        face_data_usable = face_data.json()
        return face_data_usable
    
    def save_data(self):
        """Save facial data."""
        print("Saving facial data...")
        if self.faces_detected:
            # Get specific landmark points
            # For example, getting the eyes and calculating distance between them:
            right_eye = self.landmarks.part(39)     # Right eye start
            left_eye = self.landmarks.part(42)      # Left eye start
        
            nose_top = self.landmarks.part(27)      # Top of the nose bridge
            nose_bottom = self.landmarks.part(30)   # Bottom of the nose bridge
        
            right_nostril = self.landmarks.part(31) # Right nostril
            left_nostril = self.landmarks.part(35)  # Left nostril
        
            right_ear = self.landmarks.part(1)      # Right side of the face
            left_ear = self.landmarks.part(15)      # Left side of the face
        
            right_mouth = self.landmarks.part(48)   # Right end of the lip
            left_mouth = self.landmarks.part(54)    # Left end of the lip
        
            eye_distance = self.calculate_distance(right_eye, left_eye)
            bridge_distance = self.calculate_distance(nose_top, nose_bottom)
            nose_width = self.calculate_distance(right_nostril, left_nostril)
            face_width = self.calculate_distance(right_ear, left_ear)
            mouth_width = self.calculate_distance(right_mouth, left_mouth)
            
            face_data = {
                "eye distance": eye_distance,
                "nose bridge distance": bridge_distance,
                "nose width": nose_width,
                "face width": face_width,
                "mouth width": mouth_width,
            }

            print(f"Saving face data: {face_data}")
            
            # Post face data to the Flask server
            try:
                response = requests.post(f"{self.API_URL}/save_face", json=face_data)
                if response.status_code == 200 or response.status_code == 201:
                    print("Face data successfully saved to the server!")
                else:
                    print(f"Failed to save face data: {response.status_code}")
            except Exception as e:
                print(f"Error posting data to server: {e}")
            
        else:
            print(f"No faces detected!")

    def check_data(self):
        """Check if the facial data already exists (to be implemented)."""
        print("Checking for existing facial data...")
        if self.faces_detected:
            face_data = requests.get(f"{self.API_URL}/get_faces")
            face_data = face_data.json()

    def run(self):
        """Main loop for running the face tracking system."""
        while True:
            if self.is_idle:
                self.idle_mode()  # Keep detecting faces in idle mode
            
            # Check if any key is pressed
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):  # Exit the program if 'q' is pressed
                break
            elif key == ord('s'):  # 's' for saving data
                self.is_idle = False # Set is_idle to False while the program runs save_data()
                self.save_data()
                self.is_idle = True # Set is_idle to True when the program finishes save_data()
            elif key == ord('c'):  # 'c' for checking data
                self.is_idle = False # Set is_idle to False while the program runs check_data()
                self.check_data()
                self.is_idle = True # Set is_idle to True when the program finishes check_data()


        # Clean up
        self.cap.release()
        cv2.destroyAllWindows()

# Initialize and run the program
face_tracking = FaceTracking()
face_tracking.run()