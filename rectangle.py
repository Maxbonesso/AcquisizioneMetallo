import os
import cv2
import glob

files = os.listdir('img/acquisizione_3/materiale7/')
num = 0
for img in glob.glob("img/acquisizione_3/materiale7/*.jpeg"):
    new = cv2.imread(img)
    new = cv2.rectangle(new, (2660, 0), (3836, 1742), (0, 0, 255), 2)
    cv2.imwrite('img/acquisizione_3/materiale7/rectangle/' + str(files[num]) + '', new)
    num = num + 1