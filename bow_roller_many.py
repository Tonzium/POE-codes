import keyboard
import pyautogui
import cv2
import numpy as np
import time
import pygetwindow as gw
import random


# constants
image_path = "Stash.png"

# Time start
start_time = time.time()


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
        print("Stash found at:", max_loc)
        # Perform further actions using max_loc
        # make sure Currency tab selected
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 225, max_loc[1] + template.shape[0] // 2 + 35)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(0.1)
        # Currency "General" Tab
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 100, max_loc[1] + template.shape[0] // 2 + 75)
        pyautogui.leftClick()
        time.sleep(0.1)
        # Move mouse to center of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    else:
        print("Stash not found on the screen.")
    return template, max_loc


def make_screen_check_for_mods():
    template_path = "Two_additional_arrows.png"
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
        result = True
    else:
        result = False
    return result

def activate_path_of_exile():
    # Find the Path of Exile window by its title
    poe_window = gw.getWindowsWithTitle('Path of Exile')

    if poe_window:
        # Activate the Path of Exile window
        poe_window[0].activate()
    else:
        print("No POE -window found")


# loop for craft
def loop_for_craft_single(times_rolled):
    while True:
        
        random_number_1 = random.uniform(0.01, 0.05)
        random_number_2 = random.uniform(0.01, 0.05)

        pyautogui.click(button='left')
        time.sleep(random_number_1)  # Adjust the delay if needed

        times_rolled += 1

        result = make_screen_check_for_mods()

        time.sleep(random_number_2)

        if keyboard.is_pressed('l'):
            keyboard.release("shift")
            print("Cancelled. Rolled", times_rolled, "times!")
            break

        if result == True:
            keyboard.release("shift")
            print("Succeed. Rolled", times_rolled, "times!")
            break

def change_bow_place_zero():

    # move to inventorio place 1
    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1000, max_loc[1] + template.shape[0] // 2 + 600)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)



def change_bow_place1():

    # move to inventorio place 1
    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1100, max_loc[1] + template.shape[0] // 2 + 600)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

def change_bow_place2():

    # move to inventorio place 2
    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1200, max_loc[1] + template.shape[0] // 2 + 600)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

def change_bow_place3():

    # move to inventorio place 3
    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1300, max_loc[1] + template.shape[0] // 2 + 600)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

def change_bow_place4():

    # move to inventorio place 4
    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1400, max_loc[1] + template.shape[0] // 2 + 600)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

def change_bow_place5():

    # move to inventorio place 5
    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1530, max_loc[1] + template.shape[0] // 2 + 600)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

def setup_for_crafting():

    # move mouse to Orb of Alteration
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 220, max_loc[1] + template.shape[0] // 2 + 190)

    time.sleep(0.1)

    pyautogui.rightClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)



#Actions
    
# Running this one time
six_bow_run = True
pyautogui.PAUSE = 0.1

while six_bow_run:

    activate_path_of_exile()
    time.sleep(0.1)
    template, max_loc = find_stash_move_mouse_center()

    ### Craft BOW IN THE CURRENCY TAB
    setup_for_crafting()

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    loop_for_craft_single(times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 0    
    change_bow_place_zero()

    setup_for_crafting()

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    loop_for_craft_single(times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break


### Craft THE BOW IN POSITION 1
    change_bow_place1()

    setup_for_crafting()

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    loop_for_craft_single(times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 2
    change_bow_place2()

    setup_for_crafting()

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    loop_for_craft_single(times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 3
    change_bow_place3()

    setup_for_crafting()

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    loop_for_craft_single(times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 4
    change_bow_place4()

    setup_for_crafting()

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    loop_for_craft_single(times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 5
    change_bow_place5()

    setup_for_crafting()

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    loop_for_craft_single(times_rolled=0)

    # Always end the loop
    six_bow_run = False


# Time end
    
end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")