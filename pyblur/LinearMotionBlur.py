# -*- coding: utf-8 -*-
import math
import numpy as np
from PIL import Image
from scipy.signal import convolve2d
from skimage.draw import line

from LineDictionary import LineDictionary

lineLengths={3,5,7,9}
# lineLengths =[3,5,7,9]
lineTypes = ["full", "right", "left"]

lineDict = LineDictionary()

# def LinearMotionBlur_random(img):
#     lineLengthIdx = np.random.randint(0, len(lineLengths))
#     lineTypeIdx = np.random.randint(0, len(lineTypes)) 
#     lineLength = lineLengths[lineLengthIdx]
#     lineType = lineTypes[lineTypeIdx]
#     lineAngle = randomAngle(lineLength)
#     return LinearMotionBlur(img, lineLength, lineAngle, lineType)

def EdgeEnhance(img, dim, center_value):
    imgarray = np.array(img, dtype="float32")
    kernel = EEKernel(dim, center_value)
    convolved = convolve2d(imgarray, kernel, mode='same', fillvalue=255.0).astype("uint8")
    img = Image.fromarray(convolved)
    return img

def EEKernel(dim, center_value):
    kernelwidth = dim
    kernelCenter = int(math.floor(dim/2))
    kernel = -np.ones((kernelwidth, kernelwidth), dtype=np.float32)
    kernel[kernelCenter, kernelCenter] = center_value
        
    # normalizationFactor = np.count_nonzero(kernel)
    # kernel = kernel / normalizationFactor        
    return kernel


def LinearMotionBlur(img, dim, angle, linetype):
    imgarray = np.array(img, dtype="float32")
    kernel = LineKernel(dim, angle, linetype)
    convolved = convolve2d(imgarray, kernel, mode='same', fillvalue=255.0).astype("uint8")
    img = Image.fromarray(convolved)
    return img

def LineKernel(dim, angle, linetype):
    kernelwidth = dim
    kernelCenter = int(math.floor(dim/2))
    kernel = np.zeros((kernelwidth, kernelwidth), dtype=np.float32)
    # if dim in lineLengths:
    #     angle = SanitizeAngleValue(kernelCenter, angle)
    #     lineAnchors = lineDict.lines[dim][angle]
    # else:
    #     lineAnchors = [kernelCenter,0,kernelCenter,int(dim-1)]
    #     # starting point -> end point
    if(linetype == 'right'):
        lineAnchors[0] = kernelCenter
        lineAnchors[1] = kernelCenter
    if(linetype == 'left'):
        lineAnchors[2] = kernelCenter
        lineAnchors[3] = kernelCenter
    
    for i in range(dim):
        if i < kernelCenter:
            l = 2*i+1
        else:
            l = dim - 2*(i-kernelCenter)          
        start = int((dim - l)/2)
        for j in range(l):
            kernel[i,start+j] = 1
        
    normalizationFactor = np.count_nonzero(kernel)
    kernel = kernel / normalizationFactor        
    return kernel

def SanitizeAngleValue(kernelCenter, angle):
    numDistinctLines = kernelCenter * 4
    angle = math.fmod(angle, 180.0)
    if angle < 0:
        angle = 180.0 - angle
    # validLineAngles = np.linspace(0,180, numDistinctLines, endpoint = False)
    # angle = nearestValue(angle, validLineAngles)
    return angle

def nearestValue(theta, validAngles):
    idx = (np.abs(validAngles-theta)).argmin()
    return validAngles[idx]

def randomAngle(kerneldim):
    kernelCenter = int(math.floor(kerneldim/2))
    numDistinctLines = kernelCenter * 4
    validLineAngles = np.linspace(0,180, numDistinctLines, endpoint = False)
    angleIdx = np.random.randint(0, len(validLineAngles))
    return int(validLineAngles[angleIdx])
