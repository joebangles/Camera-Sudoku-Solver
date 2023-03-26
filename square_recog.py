import cv2
from PIL import Image

cam = cv2.VideoCapture(0)


while True:
    # open feed from camera, ignoring boolean confirmation
    _, img = cam.read()

    # B&W
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    for cnt in contours:
        x1, y1 = cnt[0][0]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            pos, dim, r = cv2.minAreaRect(cnt)
            x, y = pos
            w, h = dim
            ratio = float(w) / h
            if 0.9 <= ratio <= 1.1 and w > 200:
                print(r, w)
                img = cv2.drawContours(img, [cnt], -1, (0, 255, 255), 3)
                cv2.putText(img, 'Board Found', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv2.imshow('frame', img)

    # If q is pressed, quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        _, framed = cam.read()
        framed = cv2.cvtColor(framed, cv2.COLOR_BGR2GRAY)
        break
