import numpy as np
import cv2
from scipy.ndimage.filters import convolve

def myfunc(i):
    pass # do nothing

def gamma(x,a): #ガンマ変換
    c = 255
    y = 255*((x/255)**(a))
    return y

def filtering(x,a):
    if(a==2):
        w = np.ones((3,3)) * (-1)
        w[1,1] = 9
        return convolve(x, w) #k=9の場合の鮮鋭化フィルタ
    elif (a == 3):
        w = np.array([[1, 1, 1],
                     [1, -8, 1],
                     [1, 1, 1],
                     ])
        return convolve(x, w) #ラプラシアンフィルタ(3*3)
    elif (a==4):
        w = np.array([
                     [ 1,  1,  1],
                     [ 0,  0,  0],
                     [-1, -1, -1]
                     ])
        return convolve(x,w) #グラディエントフィルタ(3*3)
    else:
        return x

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('contrast', # name of value
                   'title', # win name
                   0, # min
                   200, # max
                   myfunc) # callback func

cv2.createTrackbar('red', # name of value
                   'title', # win name
                   0, # min
                   200, # max
                   myfunc) # callback func

cv2.createTrackbar('blue', # name of value
                   'title', # win name
                   0, # min
                   200, # max
                   myfunc) # callback func

cv2.createTrackbar('green', # name of value
                   'title', # win name
                   0, # min
                   200, # max
                   myfunc) # callback func

cv2.createTrackbar('filter', # name of value
                   'title', # win name
                   0, # min
                   4, # max
                   myfunc) # callback func

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)




while(True):

    ret, frame = cap.read()
    
    if not ret: continue


    v = cv2.getTrackbarPos('contrast',  # get the value
                           'title')  # of the win
    
    u = cv2.getTrackbarPos('red',  # get the value
                           'title')  # of the win
    
    x = cv2.getTrackbarPos('blue',  # get the value
                           'title')  # of the win
    
    w = cv2.getTrackbarPos('filter',  # get the value
                           'title')  # of the win
    
    y = cv2.getTrackbarPos('green',  # get the value
                           'title')  # of the win
    
    
    if(u != 0): #赤色の色調変化
        frame[:,:,2] = gamma(frame[:,:,2],u/100)
        
    if(x != 0): #青色の色調変化
        frame[:,:,0] = gamma(frame[:,:,0],x/100)  
        
    if(y != 0): #緑色の色調変化
        frame[:,:,1] = gamma(frame[:,:,1],y/100)
    
    if(v != 0):
        frame[:,:,0] = gamma(frame[:,:,0],v/100)
        frame[:,:,1] = gamma(frame[:,:,1],v/100)
        frame[:,:,2] = gamma(frame[:,:,2],v/100)

    if(w != 0):
        im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im_gray = filtering(im_gray,w)
        cv2.imshow('title', im_gray)# show in the win
    else:
        cv2.imshow('title', frame)
    
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()