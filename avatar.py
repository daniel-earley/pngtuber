import math
import pygame as pg
from pygame.locals import *

class Avatar:
    def __init__(self, window, faceImg, bodyImg):
        self.window = window
        
        # Face
        self.faceImg = faceImg
        self.faceXOffset = 0
        self.faceYOffset = 0
        self.faceWidth = 0
        self.faceHeight = 0
        
        # Body
        self.bodyImg = bodyImg
        self.bodyXOffset = 0
        self.bodyyOffset = 0
        self.bodyWidth = 0
        self.bodyHeight = 0

        # Anchor Point
        self.anchorX = 0
        self.anchorY = 0

    def draw(self, x, y):
        # Set Offsets
        xOff, yOff = x + self.bodyXOffset, y + self.bodyYOffset

        # Calculate angle of rotation
        angle = self.calcAngle(xOff, yOff)
        
        # Apply transformations
        bodyImg = pg.transform.scale(self.bodyImg, (self.bodyWidth, self.bodyHeight))
        faceImg = pg.transform.scale(self.faceImg, (self.faceWidth, self.faceHeight))
        rotatedImg = pg.transform.rotate(bodyImg, angle)

        # Blit face onto rotated image
        bW, bH = bodyImg.get_size()
        fW, fH = faceImg.get_size()
        rW, rH = rotatedImg.get_size()
        rotatedImg.blit(faceImg, (bW//2 - fW//2, rH//2 - fH//2 - self.faceYOffset))

        rect = rotatedImg.get_rect()
        rect.center = (self.anchorX, self.anchorY)

        # Draw on screen
        self.window.blit(rotatedImg, (xOff, yOff))        

    def calcAngle(self, x, y):
        # Construct Imaginary Triangle
        adj = (x + (self.bodyWidth // 2)) - self.anchorX 
        opp = y - self.anchorY
        hyp = math.sqrt(adj**2 + opp**2)

        # Calculate angle
        theta = math.asin(opp/hyp)
        angle = math.degrees(theta)

        # Add 90 degrees
        if adj >= 0:
            return (angle + 90) * -1
        else:
            return angle + 90


    # Face Setters
    def setAllFace(self, xOff, yOff, width, height):
        self.faceXOffset = xOff
        self.faceYOffset = yOff
        self.faceWidth = width
        self.faceHeight = height

    def setFaceXOffset(self, offset):
        self.faceXOffset = offset

    def setFaceYOffset(self, offset):
        self.faceYOffset = offset
    
    def setFaceWidth(self, width):
        self.faceWidth = width
    
    def setFaceHeight(self, height):
        self.faceHeight = height
    
    # Body Setters
    def setAllBody(self, xOff, yOff, width, height):
        self.bodyXOffset = xOff
        self.bodyYOffset = yOff
        self.bodyWidth = width
        self.bodyHeight = height

    def setBodyXOffset(self, offset):
        self.faceXOffset = offset

    def setBodyYOffset(self, offset):
        self.faceYOffset = offset
    
    def setBodyWidth(self, width):
        self.faceWidth = width
    
    def setBodyHeight(self, height):
        self.faceHeight = height

    # Anchor Setters
    def setAnchor(self, x, y):
        self.anchorX = x
        self.anchorY = y

    def setAnchorX(self, x):
        self.anchorX = x
    
    def setAnchorY(self, y):
        self.anchorX = y


    

        