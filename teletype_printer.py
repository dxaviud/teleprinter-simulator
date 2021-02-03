import time
import random

time_delay = 0.04
program_info = "This program simulates a teleprinter. It looks cool, but that's pretty much it."

def teletype_print(what_to_print):
    for character in what_to_print:
        print(character, end = "")
        if (character == " "):
            time.sleep(time_delay)
        else:
            time.sleep(time_delay + random.randint(0, 20)/100)
    print()

while (True):
    user_input = input("Enter some text to print ('i' for info, 'q' for quit): ")
    if user_input == "q":
        break
    elif user_input == "i":
        teletype_print(program_info)
    else:
        teletype_print(user_input)