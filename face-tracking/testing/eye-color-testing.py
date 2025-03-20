import cv2
import dlib
import numpy as np

# Load the dlib face detector and shape predictor (68-point model)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Open the webcam or image file
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the image to grayscale for dlib's face detector
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = detector(gray)
    
    for face in faces:
        # Get the facial landmarks
        landmarks = predictor(gray, face)
        
        # Get the eye regions (using the 68-point model: landmarks 36-41 for left eye, 42-47 for right eye)
        left_eye_points = []
        right_eye_points = []
        
        for i in range(36, 42):
            left_eye_points.append((landmarks.part(i).x, landmarks.part(i).y))
        for i in range(42, 48):
            right_eye_points.append((landmarks.part(i).x, landmarks.part(i).y))
        
        # Draw the eye bounding boxes (optional for visualization)
        left_eye_rect = cv2.boundingRect(np.array(left_eye_points))
        right_eye_rect = cv2.boundingRect(np.array(right_eye_points))
        
        # Get pixel values within the left eye region
        left_eye_roi = frame[left_eye_rect[1]:left_eye_rect[1] + left_eye_rect[3],
                             left_eye_rect[0]:left_eye_rect[0] + left_eye_rect[2]]
        
        # Get pixel values within the right eye region
        right_eye_roi = frame[right_eye_rect[1]:right_eye_rect[1] + right_eye_rect[3],
                              right_eye_rect[0]:right_eye_rect[0] + right_eye_rect[2]]

        # Optionally: Sample a few pixels or average the color in the eye regions
        # Example: Compute the average color (mean RGB values)
        left_eye_avg_color = np.mean(left_eye_roi, axis=(0, 1))
        right_eye_avg_color = np.mean(right_eye_roi, axis=(0, 1))
        
        left_eye_avg_color_r = int(left_eye_avg_color[0])
        left_eye_avg_color_g = int(left_eye_avg_color[1])
        left_eye_avg_color_b = int(left_eye_avg_color[2])
        left_eye_avg_color_rgb = [left_eye_avg_color_r, left_eye_avg_color_g, left_eye_avg_color_b]
        
        right_eye_avg_color_r = int(right_eye_avg_color[0])
        right_eye_avg_color_g = int(right_eye_avg_color[1])
        right_eye_avg_color_b = int(right_eye_avg_color[2])
        right_eye_avg_color_rgb = [right_eye_avg_color_r, right_eye_avg_color_g, right_eye_avg_color_b]

        # Print out the average color of the eyes
        print(f"Left Eye Average Color (RGB): {left_eye_avg_color_rgb}")
        print(f"Right Eye Average Color (RGB): {right_eye_avg_color_rgb}")
        
        # Visualize the bounding boxes (optional)
        cv2.rectangle(frame, (left_eye_rect[0], left_eye_rect[1]),
                      (left_eye_rect[0] + left_eye_rect[2], left_eye_rect[1] + left_eye_rect[3]), 
                      (0, 255, 0), 2)
        cv2.rectangle(frame, (right_eye_rect[0], right_eye_rect[1]),
                      (right_eye_rect[0] + right_eye_rect[2], right_eye_rect[1] + right_eye_rect[3]), 
                      (0, 255, 0), 2)

    # Display the output frame
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()