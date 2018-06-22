# Source:
# https://www.pyimagesearch.com/2015/01/26/multi-scale-template-matching-using-python-opencv/
# import the necessary packages
import time
import numpy as np
import argparse
import imutils
import cv2
from action_utils import *

def update_mode(current_mode):
    if current_mode == 'proceed_step2.png':
        return 'finish_enrolling.png'
    elif current_mode == 'finish_enrolling.png':
        return 'add_another_class.png'
    elif current_mode == 'add_another_class.png' or current_mode == 'init':
        return 'proceed_step2.png'
    else: raise ValueError('Invalid mode:', current_mode)

def try_enroll():
    keep_trying = True

    template_page1 = cv2.imread('proceed_step2.png')
    # print(template_page1)
    template_page2 = cv2.imread('finish_enrolling.png')
    template_page3 = cv2.imread('add_another_class.png')

    templates = {
        'proceed_step2.png': template_page1,
        'finish_enrolling.png': template_page2,
        'add_another_class.png': template_page3
    }
    mode = 'init'
   

    while keep_trying:
        if mode != 'finish_enrolling.png':
            time.sleep(4)
        else:
            time.sleep(10)
        # Had to move this block above time.sleep to take screenshot properly???
        # for template in templates:
        mode = update_mode(mode)
        scroll(mode)

        # Sleep 10 seconds before continuing
        time.sleep(4)

        template = templates[mode]
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
    
        print(startX, startY, endX, endY)
        click_roughly(startX, startY, endX, endY)

        # draw a bounding box around the detected result and display the image
        # display_found_image(mode, reference, startX, startY, endX, endY)
        write_found_image(mode, reference, startX, startY, endX, endY)
        # keep_trying = False

if __name__ == '__main__':
    try_enroll()