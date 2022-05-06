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

    def drawFace(self, surface, x, y):
        # Apply transformation
        img = pg.transform.scale(self.faceImg, (self.faceWidth, self.faceHeight))
        # Draw on screen
        surface.blit(img, (x - self.faceXOffset, self.faceYOffset + y))

    def drawBody(self, x, y):
        # Set Offsets
        xOff, yOff = x + self.bodyXOffset, y + self.bodyYOffset
        faceYOff = 0
        # Calculate angle of rotation
        angle = self.calcAngle(xOff, yOff)
        # print(f"Angle = {angle}")

        if abs(angle) >= 25:
            modifier = abs(angle) - 25
            faceYOff = modifier * 2
            print(f"abs(angle) = {abs(angle)}, modifier = {modifier}, faceYOff = {faceYOff}")

        # Apply transformations
        img = pg.transform.scale(self.bodyImg, (self.bodyWidth, self.bodyHeight))
        rotatedImg = pg.transform.rotate(img, angle)

        # Draw on screen
        # rotatedImg.blit(faceImg, (self.faceXOffset + x, -40))
        self.drawFace(rotatedImg, rotatedImg.get_width()//2, faceYOff)
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


    

        