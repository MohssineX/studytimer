# mimi is a nice cat 🐱

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# import libraries

import time
import sys
from playsound3 import playsound

# color variables

color_red = "\033[31m"
color_green = "\033[32m"
color_orange = "\033[33m"
color_light_blue = "\033[94m"
color_pink = "\033[95m"
color_reset = "\033[0m"


# Enable ANSI escape codes on Windows (not needed on Linux/Mac)

if sys.platform == "win32":
    import os
    os.system("")
    
# title

title = "====================================studytimer===================================="


try : 

    print("\033c", end="")
    print(f"{color_light_blue}{title}{color_reset}")
    print("")

    while True :

        while True :

            try:

                study_minutes = int(input(f"{color_orange}Enter study time in minutes : {color_reset}"))
                break

            except ValueError :

                print("")
                print(f"{color_red}err : Invalid input. (Integer numbers only).{color_reset}")
                print("")

        print("\033c", end="")

        seconds = study_minutes * 60

        while seconds > 0:

            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            remaining_seconds = seconds % 60

            print("\033[H", end="")

            print(f"{color_light_blue}{title}{color_reset}")

            print(f"{color_green}{hours:02}:{minutes:02}:{remaining_seconds:02}{color_reset}                                        ")

            seconds -= 1
            time.sleep(1)

        print("")
        print(f"{color_pink}Take a break, you've worked well :){color_reset}")
        print("")
        print("Press Ctrl+C to stop the alarm")

        # Activate alarm

        while True :
            playsound("alarm.mp3")
        
# If the user presses Ctrl+C

except KeyboardInterrupt :

            print("")
            print(f"{color_orange}Thank you for using studytimer!{color_reset}")
            print(f"{color_orange}Author : https://github.com/MohssineX{color_reset}")
