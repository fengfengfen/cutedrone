#!/usr/bin/python
"""
This program is demonstration for face and object detection using haar-like features.
The program finds faces in a camera image or video stream and displays a red box around them.

Original C implementation by:  ?
Python implementation by: Roman Stanchak, James Bowman
"""
import sys
import socket
import cv
from optparse import OptionParser

# Parameters for haar detection
# From the API:
# The default parameters (scale_factor=2, min_neighbors=3, flags=0) are tuned 
# for accurate yet slow object detection. For a faster operation on real video 
# images the settings are: 
# scale_factor=1.2, min_neighbors=2, flags=CV_HAAR_DO_CANNY_PRUNING, 
# min_size=<minimum possible face size

min_size = (20, 20)
image_scale = 2
haar_scale = 1.2
min_neighbors = 2
haar_flags = 0

global previousPos
previousPos = False

global sock
sock = socket.socket( socket.AF_INET,socket.SOCK_DGRAM )

def controlMessage(msg):
  global sock
  print msg
  sock.sendto(msg, ("127.0.0.1", 4321) )

def detect_and_draw(img, cascade):
    global previousPos
    # allocate temporary images
    gray = cv.CreateImage((img.width,img.height), 8, 1)
    small_img = cv.CreateImage((cv.Round(img.width / image_scale),
			       cv.Round (img.height / image_scale)), 8, 1)

    # convert color input image to grayscale
    cv.CvtColor(img, gray, cv.CV_BGR2GRAY)

    # scale input image for faster processing
    cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)

    cv.EqualizeHist(small_img, small_img)

    if(cascade):
        t = cv.GetTickCount()
        xcenter = 640/2
        ycenter = 480/2
	centersize = 150
        innercentersize = 100
	cv.Rectangle(img, (xcenter-centersize,ycenter-centersize), (xcenter+centersize,ycenter+centersize), cv.RGB(0, 255, 0), 3, 8, 0)
        cv.Rectangle(img, (xcenter-innercentersize,ycenter-innercentersize), (xcenter+innercentersize,ycenter+innercentersize), cv.RGB(0, 0, 255), 3, 8, 0)
        faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                     haar_scale, min_neighbors, 1, min_size)
        t = cv.GetTickCount() - t
        print "detection time = %gms" % (t/(cv.GetTickFrequency()*1000.))
        if faces:
            for ((x, y, w, h), n) in faces:
                # the input to cv.HaarDetectObjects was resized, so scale the 
                # bounding box of each face and convert it to two CvPoints
                pt1 = (int(x * image_scale), int(y * image_scale))
                pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
                cv.Rectangle(img, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
                
		xval = x+w/2
		yval = y+h/2
                print "(%sx%s,%sx%s)" % (x,y,w,h)
		print "(%s,%s)=%s" % (xcenter,xval,xcenter-xval)
                msgs = False
                if 1:
                #if previousPos:
                    if (xval>170):
                       controlMessage("left")
                       msgs = True
                    elif (xval<130):
                       controlMessage("right")
                       msgs = True
                    #else:
                    #	   controlMessage("stayx")
                    if (w>centersize):
                       msgs = True
                       controlMessage("up")
                    elif (w<innercentersize):
                       msgs = True
                       controlMessage("down")
                    
                    if not msgs:
                       controlMessage("stay")
                #previousPos = (xval,yval)
	#	if (xval
		

    cv.ShowImage("result", img)

if __name__ == '__main__':

    parser = OptionParser(usage = "usage: %prog [options] [filename|camera_index]")
    parser.add_option("-c", "--cascade", action="store", dest="cascade", type="str", help="Haar cascade file, default %default", default = "../../data/haarcascades/haarcascade_frontalface_alt.xml")
    (options, args) = parser.parse_args()

    cascade = cv.Load("haarcascade_frontalface_alt.xml")
    
    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    input_name = args[0]
    if input_name.isdigit():
        capture = cv.CreateCameraCapture(int(input_name))
    else:
        capture = None

    cv.NamedWindow("result", 1)

    if capture:
        frame_copy = None
        while True:
            frame = cv.QueryFrame(capture)
            if not frame:
                cv.WaitKey(0)
                break
            if not frame_copy:
                frame_copy = cv.CreateImage((frame.width,frame.height),
                                            cv.IPL_DEPTH_8U, frame.nChannels)
            if frame.origin == cv.IPL_ORIGIN_TL:
                cv.Copy(frame, frame_copy)
            else:
                cv.Flip(frame, frame_copy, 0)
            
            detect_and_draw(frame_copy, cascade)

            if cv.WaitKey(10) >= 0:
                break
    else:
        image = cv.LoadImage(input_name, 1)
        detect_and_draw(image, cascade)
        cv.WaitKey(0)

    cv.DestroyWindow("result")
