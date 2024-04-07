import keyboard
import pyautogui
import pyperclip
import cv2
import numpy as np
import time
import pygetwindow as gw
import re
import random

# constants
image_path = "Stash.png"
#two_additional_arrows = "Two_additional_arrows.png"

# copy clipboard data
def get_clipboard_data():
    return pyperclip.paste()

def find_stash_move_mouse_center():
    template_path = "Stash.png"
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
        print("Template found at:", max_loc)
        # Perform further actions using max_loc
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    else:
        print("Template not found on the screen.")
    return template, max_loc


def activate_path_of_exile():
    # Find the Path of Exile window by its title
    poe_window = gw.getWindowsWithTitle('Path of Exile')

    if poe_window:
        # Activate the Path of Exile window
        poe_window[0].activate()
    else:
        print("no poe found")



#Actions
activate_path_of_exile()
time.sleep(0.1)
template, max_loc = find_stash_move_mouse_center()

times_rolled = 0

# loop for craft
while True:

    # move mouse to Orb of Alteration
    random_number_alts_y = random.randint(185, 195)
    random_number_alts_x = random.randint(215, 225)
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - random_number_alts_x, max_loc[1] + template.shape[0] // 2 + random_number_alts_y)
    pyautogui.rightClick()
    time.sleep(0.1)
    # move to middle
    random_number_middle_y = random.randint(350, 410)
    random_number_middle_x = random.randint(-20, 20)
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + random_number_middle_x, max_loc[1] + template.shape[0] // 2 + random_number_middle_y)
    pyautogui.leftClick()
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+c')

    # Data
    time.sleep(0.5) # This is necessary because clipboard is slow
    clipboard_data = get_clipboard_data()
    
    pattern = re.compile(r'Bow Attacks fire 2 additional Arrows|\+1 to Level of all Skill Gems|\+1 to Level of all Spell Skill Gems|\+19% chance to Suppress Spell Damage|\+2[0-3]% chance to Suppress Spell Damage|\+21% chance to Suppress Spell Damage|\+22% chance to Suppress Spell Damage|\+23% chance to Suppress Spell Damage|Enemies you Kill have a [3][0-5]% chance to Explode, dealing a tenth of their maximum Life as Physical Damage|Gain [1-3] Charges when you are Hit by an Enemy|[0-25]% increased Attack Speed during Effect')
    matches = pattern.findall(clipboard_data)

    times_rolled += 1

    if keyboard.is_pressed('l'):
        print("l pressed. Exiting the loop.")
        print(matches)
        print("Rolled", times_rolled, "times!")
        break
    if matches:
        print("breaking..")
        print(matches)
        print("Rolled", times_rolled, "times!")
        break
