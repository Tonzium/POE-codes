import keyboard
import pyautogui
import cv2
import numpy as np
import time
import pygetwindow as gw
import random


# constants
image_path = "Stash.png"



def find_stash_move_mouse_center():
    template_path = "Stash.png"
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Capture screenshot within the Path of Exile window
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
        # Perform further actions using max_loc
        # make sure currency tab selected
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 225, max_loc[1] + template.shape[0] // 2 + 35)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(0.1)
        # move mouse to center of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380) 
    else:
        print("Stash not found on the screen.")
    return template, max_loc


def make_screen_check_for_mods():
    template_path = "Two_additional_arrows.png"
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Capture screenshot within the Path of Exile window
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    #Matching
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if a match is found based on a threshold
    threshold = 0.8  # Adjust as needed
    if max_val >= threshold:
        result = True
    else:
        result = False
    return result

def activate_path_of_exile():
    # Find the Path of Exile window by its title
    poe_window = gw.getWindowsWithTitle('Path of Exile')

    if poe_window:
        # Activate first the Path of Exile window
        poe_window[0].activate()
    else:
        print("No POE -window found")



def setup_for_crafting():
    # move mouse to Orb of Alteration
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 220, max_loc[1] + template.shape[0] // 2 + 190)
    time.sleep(0.01)
    pyautogui.rightClick()
    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    time.sleep(0.01)

#Actions
activate_path_of_exile()
time.sleep(0.1)
template, max_loc = find_stash_move_mouse_center()

times_rolled = 0

setup_for_crafting()

keyboard.press('shift')
time.sleep(0.1)  # Adjust the delay if needed

# loop for craft
while True:
    
    random_number_1 = random.uniform(0.01, 0.03)
    random_number_2 = random.uniform(0.01, 0.05)

    pyautogui.PAUSE = random_number_1

    pyautogui.click(button='left')

    time.sleep(0.1) # Dont remove this so that it wont run OVER the RIGHT MOD

    times_rolled += 1

    result = make_screen_check_for_mods()

    time.sleep(random_number_2)

    if keyboard.is_pressed('l'):
        print("l pressed. Exiting the loop.")
        keyboard.release("shift")
        print("Rolled", times_rolled, "times!")
        break

    if result == True:
        keyboard.release("shift")
        print("Rolled", times_rolled, "times!")
        break
