# mimi is a nice cat 🐱

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# import libraries

import sys
import time
import os
import shutil
from playsound3 import playsound

# terminal size

last_size = shutil.get_terminal_size()

# alarm path

alarm_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alarm.mp3")

# color variables

color_red = "\033[31m"
color_green = "\033[32m"
color_yellow = "\033[33m"
color_light_blue = "\033[94m"
color_pink = "\033[95m"
color_orange = "\033[38;2;255;165;0m"
color_reset = "\033[0m"


# Enable ANSI escape codes on Windows (not needed on Linux/Mac)

if sys.platform == "win32":
    os.system("")
    
# title

title = "====================================studytimer======================================="


try : 

    while True :

        print("\033c", end="")
        print(f"{color_light_blue}{title}{color_reset}")
        print("")
        input(f"{color_pink}Welcome to studytimer Press Enter to start using studytimer : {color_reset}")
        print("")



        while True :

            try:

                study_minutes = int(input(f"{color_yellow}Enter study time in minutes : {color_reset}"))
                
                if study_minutes <= 1440 :

                    break

                else :

                    print("")
                    print(f"{color_red}err101 : Invalid timer. (Maximum allowed is 1440 minutes (24 hours)).{color_reset}")
                    print("")

            except ValueError :

                print("")
                print(f"{color_red}err102 : Invalid input. (Integer numbers only).{color_reset}")
                print("")

        print("\033c", end="")

        seconds = study_minutes * 60

        while seconds > 0:

            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            remaining_seconds = seconds % 60
            timer = f"{color_green}{hours:02}:{minutes:02}:{remaining_seconds:02}{color_reset}"

            print("\033[H", end="")

            print(f"{color_light_blue}{title}{color_reset}")
            print("")
            print(f"+------------------------------------------------------------------------------------+")
            print(f"|                                                                                    |")
            print(f"|                                {color_orange}Timer :{color_reset}                                             |")
            print(f"|                                                                                    |")
            print(f"|                                {timer}                                            |")
            print(f"|                                                                                    |")
            print(f"+------------------------------------------------------------------------------------+")

            current_size = shutil.get_terminal_size()
            if current_size != last_size:
                print("\033c", end="") 
                last_size = current_size

            seconds -= 1
            time.sleep(1)

        print("")
        print(f"{color_pink}Take a break, you've worked well :){color_reset}")
        print("")
        print("Press'Ctrl+C'to stop alarm.")

        # Activate alarm

        while True :

            playsound(alarm_path)


# If the user presses Ctrl+C

except KeyboardInterrupt :

            print("\n")
            print(f"{color_yellow}Thank you for using studytimer!{color_reset}")
            print(f"{color_yellow}Author : https://github.com/MohssineX{color_reset}")
