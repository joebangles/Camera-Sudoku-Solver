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
square_dim = height * 0.6

sliced = [[], [], [], [], [], [], [], [], []]

for y in range(9):
    y_top = height * 0.2 + y * (square_dim//9)
    y_bottom = y_top + square_dim // 9
    for x in range(9):
        x_left = width * 0.5 - height * 0.3 + x * square_dim // 9
        x_right = x_left + square_dim // 9
        sliced[y].append(Image.fromarray(np.uint8(framed[int(y_top):int(y_bottom), int(x_left):int(x_right)])))
        sliced[y][x].save(str(y) + " " + str(x) + ".jpg")


# Display photo
# im.show()
