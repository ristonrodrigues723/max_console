#!/usr/bin/env python3 
#needs to added to raspi aftr retropie inatallation for getiing  to work 
# not tested tryar your own risk

import RPi.GPIO as GPIO
from evdev import UInput, ecodes
import time


GPIO.setmode(GPIO.BCM)



GPIO_MAPPING = {
    # D-Pad buttons for up down
    20: ecodes.KEY_DOWN,    # D-PadDown (gge8)- mapping i pcb and netizt
    21: ecodes.KEY_LEFT,    # D-PadLeft (gge9)
    24: ecodes.KEY_RIGHT,   # D-PadRight (gge7)
    16: ecodes.KEY_UP,      # D-PadUp (gge6)
    
    # Face buttons (Triangle, Circle, Cross, Square)
    19: ecodes.KEY_X,       # FaceButton△ (gge2) -> Mapped to 'X' key
    26: ecodes.KEY_A,       # FaceButton◯ (gge5) -> Mapped to 'A' key
 # thers a sort so 2-3 buttons will need canging
    0: ecodes.KEY_Z,        # FaceButton× (gge4) -> Mapped to 'Z' key
    
    6: ecodes.KEY_S,       # FaceButton□ (gge3) -> Mapped to 'S' key
    
   

    # Extra buttons - for psp emulation as per my pcb
    15: ecodes.KEY_E,       # Vol+ (gge15_3) -> Mapped to 'E' key
    22: ecodes.KEY_Q,       # Hold/Brightness (gge15_1) -> Mapped to 'Q' key
    23: ecodes.KEY_P,       # Vol- (gge15_2) -> Mapped to 'P' key
    14: ecodes.KEY_H,       # HOME (gge15_4) -> Mapped to 'H' key

    # Placeholder for Start & Select buttons_ the pcb gas errors these are reserved nned to be changed

    1: ecodes.KEY_ENTER,    # Start (gge14) -> Mapped to 'Enter' key
    2: ecodes.KEY_SPACE,    # Select (gge15) -> Mapped to 'Space' key
}

# gpo setup with pullup resistors
GPIO.setup(list(GPIO_MAPPING.keys()), GPIO.IN, pull_up_down=GPIO.PUD_UP)

 #virtauo keybard creattn and button mapping
capabilities = {ecodes.EV_KEY: list(GPIO_MAPPING.values())}
ui = UInput(capabilities, name="Pi Zero Gamepad")

# A function that handels presses releases
def handle_button_event(channel):
    key_code = GPIO_MAPPING.get(channel)
    if key_code:
        if GPIO.input(channel) == GPIO.LOW:  # Button press  gpio to gnd state
            ui.write(ecodes.EV_KEY, key_code, 1)  
            ui.syn()
        else:  # Button relesa dont mess 
            ui.write(ecodes.EV_KEY, key_code, 0)  
            ui.syn()

# Add event detection to all pins
for pin in GPIO_MAPPING.keys():
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=handle_button_event, bouncetime=50)

try:
    print("GPIO button mapper script is running...")
   #loop that runs continusly
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nExiting script.") #script exits
finally:
    ui.close()
    GPIO.cleanup()
