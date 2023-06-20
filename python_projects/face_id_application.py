import face_recognition
import cv2

# Load the known faces
known_face_encodings = []
known_face_names = []

# Function to add known faces
def add_known_face(face_image_path, face_name):
    # Load and encode the known face
    face_image = face_recognition.load_image_file(face_image_path)
    face_encoding = face_recognition.face_encodings(face_image)[0]

    # Add the face encoding with the corresponding name
    known_face_encodings.append(face_encoding)
    known_face_names.append(face_name)

# Add known faces
add_known_face("path/to/known_face_1.jpg", "John Doe")
add_known_face("path/to/known_face_2.jpg", "Jane Smith")

# Face recognition code
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detect faces
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Recognize faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        if True in matches:
            # Known face found
            match_index = matches.index(True)
            name = known_face_names[match_index]

        # Draw rectangle around the face
        top, right, bottom, left = face_locations[match_index]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Face Recognition", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
