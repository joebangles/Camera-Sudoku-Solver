from PIL import Image
import cv2
import numpy as np
import pytesseract as tesseract

cam = cv2.VideoCapture(0)

while(True):
    # open feed from camera, ignoring boolean confirmation
    _, cap = cam.read()

    # B&W
    cap = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    cap = cv2.cvtColor(cap, cv2.COLOR_GRAY2BGR)

    # Assemble rectangle
    height, width = cap.shape[:2]
    print(width, height)

    top_left = (int(width * 0.5 - height * 0.3), int(height * 0.2))
    bottom_right = (int(width * 0.5 + height * 0.3), int(height * 0.8))

    cap = cv2.rectangle(cap, top_left, bottom_right, (0, 255, 255), int(width/150))

    cv2.imshow('frame', cap)

    # If q is pressed, quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        _, framed = cam.read()
        framed = cv2.cvtColor(framed, cv2.COLOR_BGR2GRAY)
        break

cam.release()
cv2.destroyAllWindows()

# Convert numpy array to PIL image
im = Image.fromarray(np.uint8(framed))
width, height = im.size

# Display photo
im.show()
