import cv2
 
img = cv2.imread('foto.png', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

_, jpeg = cv2.imencode('.jpg', resized)

out_j = jpeg.tobytes()

f = open('resize2.txt', 'a+')
f.write(str(out_j))


#print('Resized Dimensions : ',resized.shape) 
#cv2.imshow("Resized image", resized)
#cv2.waitKey(0)
#cv2.destroyAllWindows()