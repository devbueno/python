import cv2
cam = cv2.VideoCapture(0)

ret, frame = cam.read()

img_name = "foto.png"

cv2.imwrite(img_name, frame)

cam.release()
cam.DestroyAllWindows()