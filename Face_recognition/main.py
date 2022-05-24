import cv2
from ultils.simple_facerec import SimpleFacerec
import sys, os

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("img/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    if face_names:
        print("Phat hien khuon mat")
        # time.sleep(5)
        
    else:
        print("Khong phat hien khuon mat")
        os.system("gnome-screensaver-command -l")
        sys.exit()
        # time.sleep(5)

cap.release()
cv2.destroyAllWindows()