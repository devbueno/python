import cv2

cam = cv2.VideoCapture(0) # video capture = fonte e o 0 é o dispositivo principal, variavel cam

ret, frame = cam.read() # ret = erro para capturar o dispositivo cam. Frame = o frame que pegamos da captura

_, jpeg = cv2.imencode('.jpg', frame) # codificação da imagem para array

out_j = jpeg.tobytes() # codificação da imagem para o formato em bytes 

#cv2.imwrite(img_name, frame)
f = open('enc_ph.txt', 'a+')    # cria um arquivo de texto
f.write(str(out_j))             # salva os bytes em string no bloco de texto

cam.release()                   # desconecta a camera
# cam.DestroyAllWindows() # Não é usado porque nenhuma tela é criada.