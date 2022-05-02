import pygame as pg
import sys
import cv2
from pygame.locals import *
from avatar import Avatar

# Inits
pg.init()

# File Paths
xmlName = './resources/haarcascade_frontalface_default.xml'

# Need cascade classifier to read the haarcascade xml
cascade = cv2.CascadeClassifier(xmlName)

# Setup pygame window and webcam
W, H = 700, 500
screen = pg.display.set_mode((W, H))
webcam = cv2.VideoCapture(0)

# Load images
backgroundImg = pg.image.load("./resources/background.jpeg")
faceImg = pg.image.load("./resources/face.png")
bodyImg = pg.image.load("./resources/body.png")

avatar = Avatar(screen, faceImg, bodyImg)
avatar.setAllFace(300, 0, 300, 300)
avatar.setAllBody(310, 95, 320, 320)

# Main Loop
while True:
    # Use Webcam to detect face
    unusedVar, cvImg = webcam.read()
    grayscale = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grayscale, 1.1, 15)

    # Draw Background
    screen.blit(backgroundImg, (0,0))

    # Draw a rectangle over detected face
    for (x,y,w,h) in faces:
        avatar.drawBody(-x, y)
        avatar.drawFace(-x, y)
       

    # Update Display
    pg.display.update()

    # check for exit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            webcam.release()
            sys.exit()
    

