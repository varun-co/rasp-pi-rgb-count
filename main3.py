# import the opencv library
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
import colorsys

vid = cv2.VideoCapture(0)
red = list()
green = list()
blue = list()
xaxis = list()
startTime = time.time()
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
yticks = list(range(0,255,50))
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
