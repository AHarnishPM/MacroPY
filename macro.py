from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Button, Controller as MouseController
from sys import argv
import time
import datetime




MOUSE = MouseController()
KEYBOARD = KeyController()

script, name, usage = argv


#Tracks when mouse moves
def on_move(x, y):
    a = "move"
    t = time.time()-ss
    db.append([t,a,x,y])

#Tracks when mouse clicks
def on_click(x, y, button, pressed):
    t = time.time()-ss
    if pressed:
        if "left" in str(button):
            a = "mouse_click_L"
        else:
            a = "mouse_click_R"
    else:
        if "left" in str(button):
            a = "mouse_release_L"
        else:
            a = "mouse_release_R"
    db.append([t,a,button,x,y])

#Tracks when mouse scrolls
def on_scroll(x, y, dx, dy):
    t = time.time()-ss
    a = "scroll"
    db.append([t,a,dx,dy])

###KEYBOARD HANDLING

def on_press(key):
    t = time.time()-ss
#    try:
    a = "press"
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    db.append([t,a,key])
#        print('alphanumeric key {0} pressed'.format(
#            key.char))


def on_release(key):
    t = time.time()-ss
    a = "release"
    db.append([t,a,key])
#    print('{0} released'.format(
#        key))

def run(rep):
    for n in range(rep):
        tprev = 0
        for i in lines:

            i = i[1:-1]
            x = i.split(", ")

            #time sleeping
            time.sleep(float(x[0])-tprev)
            tprev = float(x[0])

            if x[1] == '\'move\'':
                MOUSE.position = (int(x[2]),int(x[3]))

            elif x[1] == '\'mouse_click_L\'':
                MOUSE.press(Button.left)

            elif x[1] == '\'mouse_release_L\'':
                MOUSE.release(Button.left)

            elif x[1] == '\'mouse_click_R\'':
                MOUSE.press(Button.right)

            elif x[1] == '\'mouse_release_R\'':
                MOUSE.release(Button.right)

            elif x[1] == '\'scroll\'':
                MOUSE.scroll(int(x[2]),int(x[3]))

            elif x[1] == '\'press\'':
                try:
                    KEYBOARD.press(str(x[2][1:-1]))

                except ValueError:
                    v = x[2].find(":")
                    KEYBOARD.press(eval(x[2][1:v]))


            elif x[1] == '\'release\'':
                    try:
                        KEYBOARD.release(str(x[2][1:-1]))

                    except ValueError:
                        v = x[2].find(":")
                        KEYBOARD.release(eval(x[2][1:v]))




if usage == 'w':

    db = []

    #Initial time
    global ss
    ss = time.time()


    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as keylistener:
        keylistener.join()

    listener.stop()


    file = open(str(name+".txt"), "a")
    for i in db:
        file.write(str(i)+"\n")
    file.close()

    print(db)

elif 'r' in usage:

    file_obj = open(name+".txt", "r")
    file_data = file_obj.read()
    lines = file_data.splitlines()
    file_obj.close()

    rep = 1

    if len(usage) > 1:
        if usage[1:] == 'L':
            run(9999999999999)
        elif usage[1:] == 'S':
            wm = input("1: select days based on week\n2: select days based on day of the month\n> ")
            if wm == '1':
                days = input("\nEnter days of the week in this format:\n Sunday, Tuesday, and Wednesday = Sun,Tue,Wed\n\nSun: Sunday\nMon: Monday\nTue: Tuesday\nWed: Wednesday\nThu: Thursday\nFri: Friday\nSat: Saturday\nAll: ALL\n> ")
            else:
                days = input("Enter days in this format:\n1st, 3rd, and 6th day of every month = 1,3,6\n> ")
            times = input("Enter times in format HOUR:MINUTE:SECOND (military time) with commas separating each time\nEx: \'2:21 + 30 seconds PM and 8 AM\' = \'14:21:30,08:00:00\'\n> ")

            daylist = days.split(',')
            timelist = times.split(',')


            while True:
                for i in daylist:
                    time.sleep(1)
                    e = datetime.datetime.now()
                    if e.strftime("%a") == i or e.strftime("%d") == i:
                        for i in timelist:
                            if e.strftime("%H:%M:%S") == i:
                                run(1)



        else:
            run(int(usage[1:]))
    else:
        run(1)
