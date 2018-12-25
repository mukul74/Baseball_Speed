import numpy as np
import cv2
import sys
import os
import math
from skimage.filters.rank import entropy
from skimage.morphology import disk
# check opencv version
centroid_X = []
centroid_Y = []
W_X = []
W_Y = []
W_Z = []
Camera_mat = np.array((25.81,4.53,-16711.12))
Camera_mat1=np.array((-4.53,26.23,-13565.88))
Camera_mat2=np.array((0,0,1))
x_w=0
y_w=0
z_w=0
fgbg = cv2.createBackgroundSubtractorMOG2()

for filename in os.listdir('X:\FC_Imagining\Study\CV'):
    filepath  = "X:/FC_Imagining/Study/CV/" +  filename
    ret = True
    # if ret is true than no error with cap.isOpened
    frame = cv2.imread(filepath)

    if ret == True:

        # apply background substraction
        fgmask = fgbg.apply(frame)

        # check opencv version

        if (type(frame) is np.ndarray):
            (im2, contours, hierarchy) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # looping for contours
            for c in contours:

                if cv2.contourArea(c) < 300:
                    continue
                approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
                counter = 0
                #print(len(approx))
                if (len(approx) > 10) and (cv2.contourArea(c) < 2000) and (cv2.contourArea(c) > 300):
                # get bounding box from countour'

                     (x, y, w, h) = cv2.boundingRect(c)
                     counter = 1

                     if(w <= 50 and h < 50) :
                        #entr = np.std(entropy(frame1[x:x+w,y:y+h], disk(10)))
                        # print(entr)
                        # draw bounding box
                        #if(entr <.35  and entr >.15):
                        print('Top Left X Coordinate : ', x, 'Top Left Y Coordinate : ', y, 'Width : ', w, 'Height :',  h)
                        centroid_X.append(x + 0.5*w)
                        centroid_Y.append(y + 0.5*h)
                        print('Centroid X : ',(x + 0.5*w),'Centroid Y : ',(y + 0.5*h))
                        x_w=(x + 0.5*w)*Camera_mat[0]+(y + 0.5*h)*Camera_mat[1]+1*Camera_mat[2]
                        y_w=(x + 0.5*w)*Camera_mat1[0]+(y + 0.5*h)*Camera_mat1[1]+1*Camera_mat1[2]
                        z_w=(x + 0.5*w)*Camera_mat2[0]+(y + 0.5*h)*Camera_mat2[1]+1*Camera_mat2[2]
                        W_X.append(x_w)
                        W_Y.append(y_w)
                        W_Z.append(z_w)
                        print(x_w,y_w,z_w)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255,0), 2)
                        if(counter == 1):
                            break

        #cv2.imshow('foreground and background', fgmask)
            cv2.imshow('rgb', frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

for i in range(10):
    v_x=math.sqrt((W_X[i+1]-W_X[i])*(W_X[i+1]-W_X[i])+(W_Y[i+1]-W_Y[i])*(W_Y[i+1]-W_Y[i])+(W_Z[i+1]-W_Z[i])*(W_Z[i+1]-W_Z[i]))/((0.0625)*1000)*3.6
    print(v_x)
cv2.destroyAllWindows()