import cv2
cam = cv2.VideoCapture(0)

cv2.namedWindow("JotaCam")

img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("Nao foi possivel obter um frame.")
        break
    
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    
    if k%256 == 27:
        print("Esc apertado, fechando app!")
        break
    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Videoshot taken")
        img_counter+=1
         
cam.release()
cam.DestroyAllWindows()
