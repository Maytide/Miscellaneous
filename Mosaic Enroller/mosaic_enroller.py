# Source:
# https://www.pyimagesearch.com/2015/01/26/multi-scale-template-matching-using-python-opencv/
# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2
from take_screenshot import take_screenshot

template_page1 = cv2.imread('proceed_step2.png')
# print(template_page1)
template_page2 = cv2.imread('finish_enrolling.png')
template_page3 = cv2.imread('add_another_class.png')

templates = [template_page1, template_page2, template_page3]

for template in templates:
    print(1)
    (tH, tW) = template.shape[:2]
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)

    fname = take_screenshot()
    reference = cv2.imread(fname)
    reference_grey = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    found = None

    for scale in np.linspace(0.4, 1.5, 30)[::-1]:
        resized = imutils.resize(
            reference_grey, width=int(reference_grey.shape[1] * scale))
        r = reference_grey.shape[1] / float(resized.shape[1])
        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break

        # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        # if we have found a new maximum correlation value, then ipdate
        # the bookkeeping variable
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)

        # unpack the bookkeeping varaible and compute the (x, y) coordinates
    # of the bounding box based on the resized ratio
    (_, maxLoc, r) = found
    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
 
    # draw a bounding box around the detected result and display the image
    cv2.rectangle(reference, (startX, startY), (endX, endY), (0, 0, 255), 2)
    cv2.imshow("Image", reference)
    cv2.waitKey(0)