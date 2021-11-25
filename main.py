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
        current_time = get_current_time()
        print("Current Time =", current_time)
        print("The error on click_exit function")
        exit() 

def check_overload():
    overload_pos = pyautogui.locateOnScreen('overloaderror.png')
    if overload_pos != None:
        click_exit()
        
def click_heros2work():
    time.sleep(5)
    pyautogui.moveTo(890, 760, duration=1)
    for i in range(25):
        pyautogui.scroll(-1000)

    while True:
        check_overload()

        unwork_btn_pos = pyautogui.locateOnScreen('unwork_btn.png')
        # print(pyautogui.center(unwork_btn_pos))
        if unwork_btn_pos != None:
            pyautogui.click(pyautogui.center(unwork_btn_pos), duration=1)
        else:
            break
        time.sleep(3)
    ## enter the hunt game
    click_exit()
    click_pos = pyautogui.locateOnScreen('hunt_game.png')
    if click_pos != None:
        pyautogui.click(pyautogui.center(click_pos), duration=1)
    else:
        current_time = get_current_time()
        print("Current Time =", current_time)
        print("The error on enter the hunt_game")

def login():
    Connect_pos = pyautogui.locateOnScreen('Connect_wallet.png')
    # print (Connect_pos)
    if Connect_pos != None :
        Connect_point = pyautogui.center(Connect_pos)
        print (Connect_point)
        pyautogui.moveTo(Connect_point.x, Connect_point.y, duration=3)

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

current_time = get_current_time()
print("Start Time =", current_time)

time.sleep(2)
width, height = pyautogui.size()
check_overload()
while True:
    # for i in range(10):
    #     pyautogui.click(x=width/2, y=height/2)
    #     time.sleep(60)
    time.sleep(1200)
    click_pos = pyautogui.locateOnScreen('back2menu_btn.png')
    if click_pos != None:
        pyautogui.click(pyautogui.center(click_pos), duration=1)
        time.sleep(5)

        check_menu_pos = pyautogui.locateOnScreen('menu.png')
        if check_menu_pos != None:
            pyautogui.click(1383, 789, duration=3)
            click_heros2work()
            print("succeccful")
        else:
            current_time = get_current_time()
            print("Current Time =", current_time)
            print("The error on check menu")
            exit() 
    else:
        current_time = get_current_time()
        print("Current Time =", current_time)
        print("The error on back2menu_btn")
        exit()