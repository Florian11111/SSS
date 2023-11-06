import cv2

cap = cv2.VideoCapture(0)
i = 0
if not cap.isOpened():
    print("fehler")
    exit()

cap.set(11, 32)
cap.set(10, 128)
cap.set(12, 32)
cap.set(17, 5300)
cap.set(14, 16)
cap.set(15, -7)

while(True):
    ret, frame = cap.read()

    cv2.imshow("test", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(f"Weiß{i}.png", frame)
        print("bild wurde gespeichert!")
        i += 1
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()