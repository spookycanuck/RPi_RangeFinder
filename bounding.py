import cv2

path = r'/home/pi/Desktop/smartCooler/test.jpg'

image = cv2.imread(path)

window_name = 'TEST'

startPoint = (10,10)
endPoint = (600,1900)

s2 = (2000,10)
e2 = (2580,1900)

color = (255,0,0) #RGB
c2 = (0,255,0)
thickness = 2

image = cv2.rectangle(image,startPoint,endPoint, color, thickness)
image2 = cv2.rectangle(image,s2,e2, c2, thickness)
resize = cv2.resize(image, (900,600))
r2 = cv2.resize(image2, (900,600))

try:
    cv2.imshow(window_name,resize)
    cv2.imshow(window_name,r2)
    cv2.waitKey(15000)
    cv2.destroyAllWindows()
except Exception as e:
    print(e)
    raise
