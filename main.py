import pygame as pg
import sys
import cv2
from pygame.locals import *
from torch import det
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

# Initialize Avatar
avatar = Avatar(screen, faceImg, bodyImg)
avatar.setAllFace(W//2, 0, 300, 300)
avatar.setAllBody(W//2, 80, 320, 320)
avatar.setAnchor(W//2, H)

# Some storage
faceX, faceY = W//2, H
detection = False

# Main Loop
while True:
    # Use Webcam to detect face
    unusedVar, cvImg = webcam.read()
    grayscale = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grayscale, 1.1, 15)

    # Draw Background
    screen.blit(backgroundImg, (0,0))

    # Draw Avatar
    for (x,y,w,h) in faces:
        detection = True
        faceX, faceY = -x, y
        avatar.drawBody(faceX, faceY)
        avatar.drawFace(faceX, faceY)
    
    # Draw avatar's last position on loss of detection
    if not detection:
        avatar.drawBody(faceX, faceY)
        avatar.drawFace(faceX, faceY)

    # Visual representation of the anchor point
    pg.draw.circle(screen, (0,255,0), (avatar.anchorX, avatar.anchorY), 10)

    # Update Display
    pg.display.update()

    detection = False

    # check for exit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            webcam.release()
            sys.exit()
    

