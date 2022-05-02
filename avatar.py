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

    def drawFace(self, x, y):
        img = pg.transform.scale(self.faceImg, (self.faceWidth, self.faceHeight))
        self.window.blit(img, (x + self.faceXOffset, y + self.faceYOffset))

    def drawBody(self, x, y):
        img = pg.transform.scale(self.bodyImg, (self.bodyWidth, self.bodyHeight))
        self.window.blit(img, (x + self.bodyXOffset, y + self.bodyYOffset))

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


    

        