import pyautogui


def take_screenshot(fname='screenshot.png'):
    # Take screenshot
    pic = pyautogui.screenshot()

    # Save the image
    pic.save(fname)
    return fname