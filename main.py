# import the opencv library
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
import colorsys

def convert_rgb_to_hsv(r,g,b):
    h ,s,v = colorsys.rgb_to_hsv(r/255,g/255,b/255)
    (h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
    return h,s,v
def convert_hsv_to_wavelength(h,s,v):
    if ( h >= 0 and h   <= 270):
        return 620 - 170/179*h
    # define a video capture object
def average(r,g,b):
    return sum(r)/(len(r)*255) , sum(g)/(255*len(g)), sum(b)/(255*len(b))
vid = cv2.VideoCapture(1)
count = 61
red = list()
green = list()
blue = list()
xaxis = list()
startTime = time.time()
wavelength = list()
while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame

    color = frame[300,300]
    b,g,r = color[0],color[1],color[2]
    xaxis.append(int(time.time()- startTime))
    red.append(r)
    green.append(g)
    blue.append(b)
    print(r,g,b)
    h,s,v = convert_rgb_to_hsv(r,g,b)
    wavelength_in_nm = convert_hsv_to_wavelength(h,s,v)
    print(wavelength_in_nm)
    wavelength.append(wavelength_in_nm)
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

# org
    org = (230, 250)

# fontScale
    fontScale = 1

# Blue color in BGR
    color = (255, 0, 0)

# Line thickness of 2 px
    thickness = 2

    # Using cv2.putText() method
    frame = cv2.putText(frame, f'({r},{g},{b})', org, font,
                   fontScale, color, thickness, cv2.LINE_AA)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
'''plt.plot(np.array(xaxis),np.array(red),color='red')
plt.plot(np.array(xaxis),np.array(blue),color='blue')
plt.plot(np.array(xaxis),np.array(green),color='green')
plt.xlabel('Time in Seconds')
plt.title('RGB Value of Blue Material ')
plt.ylabel('Color out of 255')
plt.savefig('rgb-value.png') '''
yticks = list(range(0,275,60))
print(yticks)
#plt.plot(np.array(xaxis),np.array(red),color=average(red,green,blue))
plt.subplot(2,2,1)
plt.plot(np.array(xaxis),np.array(green),color='green')
plt.xlabel('Time in Seconds')
plt.yticks(yticks)
plt.ylabel('Green value out of 255')
plt.title('Green Count over a period of time')

plt.subplot(2,2,2)
plt.plot(np.array(xaxis),np.array(red),color='red')
plt.yticks(yticks)
plt.ylabel('Green value out of 255')
plt.xlabel('Time in Seconds')
plt.ylabel('Red value out of 255')
plt.title('Red Count over a period of time')


plt.subplot(2,2,3)
plt.plot(np.array(xaxis),np.array(blue),color='blue')
plt.yticks(yticks)
plt.ylabel('Green value out of 255')
plt.xlabel('Time in Seconds')
plt.ylabel('Blue value out of 255')
plt.title('Blue Count over a period of time')
plt.tight_layout()

plt.show()
plt.savefig('test.jpg')
