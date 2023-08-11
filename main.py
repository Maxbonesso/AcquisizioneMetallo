import math
import cv2
import numpy as np

def LinearToSrgb(val):
    neg_mask = val <= 0
    first_threshold_mask = (val > 0) * (val <= 0.0031308)  # and bit a bit
    second_threshold_mask = (val > 0.0031308) * (val <= 1)
    pos_mask = (val > 1)
    val[neg_mask] = 0
    val[first_threshold_mask] *= 12.92
    val[second_threshold_mask] = (np.power(val[second_threshold_mask], 0.41666) * 1.055) - 0.055
    val[pos_mask] = 1
    return val

def SrgbToLinear(val):
    neg_mask = val <= 0
    first_threshold_mask = (val > 0) * (val <= 0.04045)  # and bit a bit
    second_threshold_mask = (val > 0.04045) * (val <= 1)
    pos_mask = (val > 1)
    val[neg_mask] = 0
    val[first_threshold_mask] /= 12.92
    val[second_threshold_mask] = np.power((val[second_threshold_mask] + 0.055) / 1.055, 2.4)
    val[pos_mask] = 1
    return val

g_bSpecOrDiff = 0

albedo = cv2.imread('img/oggetto2_albedo.png').astype(float)/255
specular = cv2.imread('img/oggetto2_speculare.png').astype(float)/255
linA = SrgbToLinear(albedo)
linB = SrgbToLinear(specular)
linSpec = specular - albedo
linDiff = albedo * 2
texDiff = LinearToSrgb(linDiff)
texSpec = LinearToSrgb(linSpec)
cv2.namedWindow("test1", cv2.WINDOW_NORMAL)
cv2.imshow("test1", texSpec)
cv2.namedWindow("test2", cv2.WINDOW_NORMAL)
cv2.imshow("test2", texDiff)
cv2.waitKey(0)