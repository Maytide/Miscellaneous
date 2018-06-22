import pyautogui
import cv2


def display_found_image(name, reference, startX, startY, endX, endY):
    cv2.rectangle(reference, (startX, startY), (endX, endY), (0, 0, 255), 2)
    cv2.imshow("Image", reference)
    cv2.waitKey(0)

def write_found_image(name, reference, startX, startY, endX, endY):
    cv2.rectangle(reference, (startX, startY), (endX, endY), (0, 0, 255), 2)
    cv2.imwrite('%s_%s' % ('result', name), reference)

def take_screenshot(fname='screenshot.png'):
    # Take screenshot
    pic = pyautogui.screenshot()

    # Save the image
    pic.save(fname)
    return fname

def click_roughly(startX, startY, endX, endY):
    midpoint = ((endX + startX)/2, (endY + startY)/2)
    
    pyautogui.click(*midpoint)

def scroll(mode):
    print('[Scroll] Scrolling for mode:', mode)
    if mode == 'proceed_step2.png':
        amt = -700
    elif mode == 'finish_enrolling.png':
        amt = -700
    elif mode == 'add_another_class.png':
        amt = -700
    else: ValueError('Invalid mode:', mode)
    pyautogui.scroll(amt)