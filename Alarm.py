import time
# from datetime import datetime: Imports only the datetime class from the module, (not the entire module)
# allowing you to refer to it directly as datetime
from datetime import datetime

# lets learn some new things about this time 
new_time=datetime.now()
print(new_time)  #the output is displayed in integer format

# so we use the strftime method to format this datetime object into a human-readable string.

time=new_time.strftime("%H:%M:%S")

# and to directly use it this is the syntax
time=datetime.now().strftime("%H:%M:%S")
print(time)



# -------sound-------------------------

import winsound
# (Frequency,Time)

winsound.Beep(3000,2000)

# -----------------------------Time---------------------
import time

print("This message appears first.")
time.sleep(1)  # Pauses execution for 1 second
print("This message appears after a 1-second delay.")

# ---------------------------------Now using this concept we are gonna build a alarm clock----------------


import time
from datetime import datetime
import winsound

def alaram():
    user=(input("Enter the alarm time in (HH:MM) format...\n"))
    current=datetime.now().strftime("%H:%M")
    
    if current==user:
        print("Wake uPPPppp ")

        winsound.Beep(3000,2000)
    else:
        print("You dont even know what HH:MM format is???/")

    time.sleep(1)

def again():
    while True:

        user=(input("Now U know the format want to try again??\n")).strip().lower()

        if user=="yes":
            alaram()
        elif user=="no":
            print("Great Go and sleep without my enchanted and magical alarm ")
        else:
            print("Do you even knwo how precious time is")
            break

alaram()
again()
    


