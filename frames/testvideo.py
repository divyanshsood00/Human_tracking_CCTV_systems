import cv2

img1 = cv2.imread('frames/aditya/aditya72.png')
img2 = cv2.imread('frames/avi/avi111.png')
img3 = cv2.imread('frames/divyansh/divyansh48.png')

height , width , layers =  img1.shape
# gst_out = "appsrc ! videoconvert ! x264enc noise-reduction=10000 tune=zerolatency byte-stream=true threads=4 " \
            #  " ! h264parse ! mpegtsmux ! rtpmp2tpay ! udpsink host=127.0.0.1 port=5000"
video = cv2.VideoWriter("landbc.avi",cv2.VideoWriter_fourcc(*'MPEG'),1,(width,height))

video.write(img1)
video.write(img2)
video.write(img3)

cv2.destroyAllWindows()
video.release()