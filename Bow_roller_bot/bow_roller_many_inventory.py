import keyboard
import pyautogui
import cv2
import numpy as np
import time
import pygetwindow as gw
import random


# constants
image_path = "Stash.png"
max_items = 5000

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
def loop_for_craft_single(counter, counter_craft, max_items, times_rolled):
    while True:
        
        random_number_1 = random.uniform(0.01, 0.05)
        random_number_2 = random.uniform(0.01, 0.05)

        pyautogui.click(button='left')
        time.sleep(random_number_1)  # Adjust the delay if needed

        counter += 1
        counter_craft += 1
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

        # break the rolling if there is no more alts, 5000 alts used = max_items
        if counter >= max_items:
            keyboard.release("shift")
            counter = 0
            setup_for_crafting(counter_craft, max_items, max_loc, template)
            keyboard.press("shift")
            time.sleep(0.1)

    return counter, counter_craft, max_items


def change_mid_bow_to_inventory(max_loc, template):
    # just to be sure
    keyboard.release("shift")
    # take bow with u
    time.sleep(0.1)
    pyautogui.click(button="left")
    # move mouse to sell tab
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 175, max_loc[1] + template.shape[0] // 2 + 35)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to new bow position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 265, max_loc[1] + template.shape[0] // 2 + 125)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # change currency tab
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 225, max_loc[1] + template.shape[0] // 2 + 35)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)

    
def change_inventory_bows_to_stash(max_loc, template):
    # move mouse to sell tab
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 175, max_loc[1] + template.shape[0] // 2 + 35)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    ##### SECOND ROW IN THE SELL TAB STARTING FROM THE RIGHT ENDING TO LEFT
    # move mouse to bow_0 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 265, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_0 inventory position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1000, max_loc[1] + template.shape[0] // 2 + 600)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse BACK to bow_0 sell tab pos
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 265, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_1 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 165, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_1 inventory position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1100, max_loc[1] + template.shape[0] // 2 + 600)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse BACK to bow_1 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 165, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_2 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 65, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_2 inventory position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1200, max_loc[1] + template.shape[0] // 2 + 600)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse BACK to bow_2 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 65, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_3 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 35, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_3 inventory position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1300, max_loc[1] + template.shape[0] // 2 + 600)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse BACK to bow_3 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 35, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_4 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 135, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_4 inventory position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1400, max_loc[1] + template.shape[0] // 2 + 600)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse BACK to bow_4 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 135, max_loc[1] + template.shape[0] // 2 + 385)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    ##### THIRD ROW IN THE SELL TAB STARTING FROM THE RIGHT ENDING TO LEFT
    # move mouse to bow_5 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 265, max_loc[1] + template.shape[0] // 2 + 575)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_5 inventory position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 1530, max_loc[1] + template.shape[0] // 2 + 600)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse BACK to bow_5 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 265, max_loc[1] + template.shape[0] // 2 + 575)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_6 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 165, max_loc[1] + template.shape[0] // 2 + 575)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_6 inventory position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 750, max_loc[1] + template.shape[0] // 2 + 600)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse BACK to bow_6 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 165, max_loc[1] + template.shape[0] // 2 + 575)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_7 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 65, max_loc[1] + template.shape[0] // 2 + 575)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse to bow_7 inventory position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 850, max_loc[1] + template.shape[0] // 2 + 600)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)
    # move mouse BACK to bow_7 sell tab position
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 65, max_loc[1] + template.shape[0] // 2 + 575)
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)

    ### ENDING SEQ




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



############################ THESE BAG PLACES ONLY AFFLICATION LEAGUE ################################
    
def change_bow_place6():

    # move to inventorio place 5
    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 750, max_loc[1] + template.shape[0] // 2 + 600)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)


def change_bow_place7():

    # move to inventorio place 5
    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 850, max_loc[1] + template.shape[0] // 2 + 600)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)

    # move to middle of stash
    pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)

    time.sleep(0.1)

    pyautogui.leftClick()

    time.sleep(0.1)
###########################################################################################################

def setup_for_crafting(counter_craft, max_items, max_loc, template):

    if counter_craft < max_items:
        # move mouse to Orb of Alteration (left, TOP corner)
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 220, max_loc[1] + template.shape[0] // 2 + 190)

        time.sleep(0.1)

        pyautogui.rightClick()

        time.sleep(0.1)

        # move to middle of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    elif counter_craft < 2 * max_items:
        # move mouse to Orb of Alteration (left, BOTTOM corner, slot1)
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 170, max_loc[1] + template.shape[0] // 2 + 530)

        time.sleep(0.1)

        pyautogui.rightClick()

        time.sleep(0.1)

        # move to middle of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    elif counter_craft < 3 * max_items:
        # move mouse to Orb of Alteration (left, BOTTOM corner, slot2)
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 115, max_loc[1] + template.shape[0] // 2 + 540)

        time.sleep(0.1)

        pyautogui.rightClick()

        time.sleep(0.1)

        # move to middle of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    elif counter_craft < 4 * max_items:
        # move mouse to Orb of Alteration (left, BOTTOM corner, slot2)
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 60, max_loc[1] + template.shape[0] // 2 + 540)

        time.sleep(0.1)

        pyautogui.rightClick()

        time.sleep(0.1)

        # move to middle of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    elif counter_craft < 5 * max_items:
        # move mouse to Orb of Alteration (left, BOTTOM corner, slot2)
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 5, max_loc[1] + template.shape[0] // 2 + 540)

        time.sleep(0.1)

        pyautogui.rightClick()

        time.sleep(0.1)

        # move to middle of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    elif counter_craft < 6 * max_items:
        # move mouse to Orb of Alteration (left, BOTTOM corner, slot3)
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 + 50, max_loc[1] + template.shape[0] // 2 + 540)

        time.sleep(0.1)

        pyautogui.rightClick()

        time.sleep(0.1)

        # move to middle of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)
    else:
        # move mouse to Orb of Alteration (left, BOTTOM corner, slot4)
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2 - 110, max_loc[1] + template.shape[0] // 2 + 550)

        time.sleep(0.1)

        pyautogui.rightClick()

        time.sleep(0.1)

        # move to middle of stash
        pyautogui.moveTo(max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2 + 380)




#Actions
    
# Running this one time
counter = 0
counter_craft = 0
looper_count = 0

while True:

    activate_path_of_exile()
    time.sleep(0.1)
    template, max_loc = find_stash_move_mouse_center()

    ### Craft BOW IN THE CURRENCY TAB
    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 0
    change_bow_place_zero()

    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break


### Craft THE BOW IN POSITION 1
    change_bow_place1()

    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 2
    change_bow_place2()

    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 3
    change_bow_place3()

    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 4
    change_bow_place4()

    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)

    if keyboard.is_pressed('l'):
        print("L pressed. Exiting the script.")
        break

### Craft THE BOW IN POSITION 5
    change_bow_place5()

    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)


######### POSITIONS 6 and 7 ONLY AFFLICATION LEAGUE #################################################################
    
    change_bow_place6()

    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)

    change_bow_place7()

    setup_for_crafting(counter_craft, max_items, max_loc, template)

    keyboard.press('shift')
    time.sleep(0.1)  # Adjust the delay if needed

    counter, counter_craft, max_items = loop_for_craft_single(counter, counter_craft, max_items, times_rolled=0)


######################################################################################################################

############ AT THIS POINT ALL BOWS AT INVENTORY ARE READY #################
    
#### NEXT WE WILL CHANGE FRESH BOWS TO INVENTORY AND START THE LOOP AGAIN IF IT WAS FIRST ROUND ######
    
    if looper_count > 0:
        # Always ends the loop on second round
        break

    change_mid_bow_to_inventory(max_loc, template)

    change_inventory_bows_to_stash(max_loc, template)

    # making sure that it will only do two rounds.
    looper_count += 1


#################################################################

# Time end
end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")