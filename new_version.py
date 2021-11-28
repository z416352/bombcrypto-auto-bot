from typing import Deque
import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True

## check mouse position
def mouse_pos():
    last_pos = pyautogui.position()
    try:
        while True :
            new_pos = pyautogui.position()
            if new_pos != last_pos:
                print (new_pos)
                last_pos = new_pos
    except KeyboardInterrupt: 
        print("/nEXIT")

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)
    return current_time

def click_exit():
    time.sleep(2)
    exit_pos = pyautogui.locateOnScreen('exit_btn.png')
    if exit_pos != None:
        pyautogui.click(pyautogui.center(exit_pos), duration=1)
        time.sleep(3)
    else:
        error_quit("click_exit function")

def click_ok():
    ok_pos = pyautogui.locateOnScreen('ok_btn.png')
    if ok_pos != None:
        pyautogui.click(pyautogui.center(ok_pos), duration=1)
    else:
        error_quit("click ok")

def check_overload():
    overload_pos = pyautogui.locateOnScreen('overloaderror.png')
    if overload_pos != None:
        click_exit()
        
def check_unknow():
    error_pos = pyautogui.locateOnScreen('unknow_btn.png')
    if error_pos != None:
        # click_ok()
        # time.sleep(20)
        # login_absolute()
        return True
    return False

def check_newMap():
    check_pos = pyautogui.locateOnScreen('newmap_btn.png')
    if check_pos != None:
        pyautogui.click(pyautogui.center(check_pos), duration=1)

def error_quit(event):
    current_time = get_current_time()
    print("End Time =", current_time)
    print("The error on", event)
    exit()

def click_heros2work():
    time.sleep(5)
    pyautogui.moveTo(890, 760, duration=1)
    for i in range(25):
        pyautogui.scroll(-1000)
    for j in range(20):
        time.sleep(2)
        check_overload()
        pyautogui.click(890, 760, duration=1)
        
    time.sleep(3)
        
    ## enter the hunt game
    click_exit()
    click_pos = pyautogui.locateOnScreen('hunt_game.png')
    if click_pos != None:
        pyautogui.click(pyautogui.center(click_pos), duration=1)
    else:
        error_quit("enter the hunt_game")

def login():
    Connect_pos = pyautogui.locateOnScreen('Connect_wallet.png')
    # print (Connect_pos)
    if Connect_pos != None :
        pyautogui.click(pyautogui.center(Connect_pos), duration=1)
        time.sleep(3)
        matamask_pos = pyautogui.locateOnScreen('Connect_metamask.png')
        if matamask_pos != None:
            pyautogui.click(pyautogui.center(matamask_pos), duration=1)
            time.sleep(3)
            sign_pos = pyautogui.locateOnScreen('Sign.png')
            if sign_pos != None:
                pyautogui.click(pyautogui.center(sign_pos), duration=1)
            else:
                error_quit("login (Sign)")
        else:
            error_quit("login (click metamask)")
    else:
        error_quit("login (connect wallet)")

def login_absolute():
    pyautogui.click(970, 740, duration=1)
    time.sleep(3)
    pyautogui.click(970, 600, duration=1)
    time.sleep(5)
    pyautogui.click(1820, 550, duration=1)
    time.sleep(60)

    click_pos = pyautogui.locateOnScreen('hunt_game.png')
    if click_pos != None:
        pyautogui.click(pyautogui.center(click_pos), duration=1)
    else:
        error_quit("enter the hunt_game after login")

# def check_manual():
#     manual_pos = pyautogui.locateOnScreen('manual.png')
#     if manual_pos != None:
        # ok_pos = pyautogui.locateOnScreen('ok.png')
        # pyautogui.click(pyautogui.center(ok_pos), duration=1)


# while True:
#     check_menu_pos = pyautogui.locateOnScreen('menu.png')

#     if check_menu_pos != None:
#         pyautogui.click(1383, 789, duration=3)
#     else:
#         print("no menu")
    
#     time.sleep(3)

time.sleep(2)

current_time = get_current_time()
print("Start Time =", current_time)


while True:
    for i in range(25):
        time.sleep(60)
    check_newMap()

    time.sleep(10)
    pyautogui.click(970, 840, duration=1)
    time.sleep(3)
    pyautogui.click(970, 815, duration=1)
    time.sleep(3)

    for i in range(25):
        pyautogui.moveTo(890, 760, duration=1)
        pyautogui.scroll(-1000)
    for i in range(15):
        pyautogui.click(890, 760, duration=1)
        time.sleep(1)

    pyautogui.click(1030, 370, duration=1)
    time.sleep(1)
    pyautogui.click(1030, 370, duration=1)
    
    if check_unknow() == True:
        current_time = get_current_time()
        print("End Time =", current_time)
        break
