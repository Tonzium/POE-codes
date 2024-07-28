import keyboard
import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
import random

def activate_path_of_exile():
    # Find the Path of Exile window by its title
    poe_window = gw.getWindowsWithTitle('Path of Exile')

    if poe_window:
        # Activate the Path of Exile window
        poe_window[0].activate()
    else:
        print("No POE -window found")

def find_inventory_move_mouse_to_start():
    template_path = "Inventory.png"
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    #Matching
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if a match is found based on a threshold
    threshold = 0.8  # Adjust as needed
    if max_val >= threshold:
        print("Stash found at:", max_loc)
        stash = True
        # Perform further actions using max_loc
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 300, max_loc[1] + template.shape[0] // 2 + 540)
    else:
        stash = False
        print("Stash not found on the screen.")
    return template, max_loc, stash

def pickup_items():
    
    # main loop to pick up items
    for i in range(5):
        keyboard.press("ctrl")
        pyautogui.leftClick()
        # move down 50 pixels
        if i < 4:
            pyautogui.moveRel(0, 50)

        if keyboard.is_pressed('l'):
            keyboard.release("shift")
            break

    # release ctrl
    keyboard.release("ctrl")

    # move mouse to next starting position
    pyautogui.moveRel(54, -200)


######### Normal poe bag 5 x 12
take_items = True

pyautogui.PAUSE = 0.03

activate_path_of_exile()

while take_items:

    template, max_loc, stash = find_inventory_move_mouse_to_start()

    if stash == False:
        break

    for i in range(12):

        random_number = random.uniform(0.01, 0.03)

        pyautogui.PAUSE = random_number

        pickup_items()

        if keyboard.is_pressed('l'):
            print("L pressed. Exiting the loop.")
            keyboard.release("shift")
            # also make the second loop end by adding stash = False
            stash = False
            break

    take_items = False