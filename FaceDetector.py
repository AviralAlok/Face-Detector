

import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	if ret == False:
		continue
	gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.1,4)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow("Video Frame",img)

	#wait for user imput -q, then stop the loop
	key_pressed= cv2.waitkey(1) & 0xFF
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
