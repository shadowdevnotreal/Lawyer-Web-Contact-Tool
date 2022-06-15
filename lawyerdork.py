# create google dork to look for attorneys in the US
# ask user what state they are looking for
# ask user what type of attorney they are looking for
# ask user what type of search they are looking for
# Open up a browser and search for the dork
# print out the results
# ask user if they want to search again
# if yes, go back to the beginning

import os
import sys
import time
import random
import webbrowser
import pipx
import pipx.colors as colors # pipx.colors.red("text")

print(pipx.colors.red("""
                                ####################################################
                                #     Welcome to the lawyer contact dork tool      #
                                #          Because looking a lawyers sucks!        #
                                # This will take you to most website contact forms #
                                #       Hopefully this will help your search!      #
                                ####################################################
"""))
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("Another Slow Production. ")
print()
print()
print()
print()


#Print word lawyers in Blue ascii terminal font.
print(""" \033[1;34;40m
                                   ░█░░░█▀█░█░█░█░█░█▀▀░█▀▄░█▀▀░░░█▀▀░█░█░█▀▀░█░█
                                   ░█░░░█▀█░█▄█░░█░░█▀▀░█▀▄░▀▀█░░░▀▀█░█░█░█░░░█▀▄
                                   ░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀
""")

#Create a menu in yellow Ascii.
print("\033[1;33;40m")

city = input("What city are you looking for? ")
state = input("What state are you looking for? ")
attorney_type = input("What type of attorney are you looking for? ")
contact = input("Type contact. ")

#dork = "site=lawyers+" + city + " " + state + "+" + attorney_type + "+" + contact_form
dork = "inurl=contact+" "site=lawyers+" + city + " " + state + "+" + attorney_type + "+" + contact
print(dork)
print("Here are the results: ")  # print out the results
ask = input("Would you like to open the dork in your browser? ")


def open_chrome():
    pass


if ask == "yes":
    open_chrome()
    webbrowser.open('https://www.google.com/search?q=' + dork)
    if ask == "no":
        print("Thank you for using the dork tool")
        os.system("exit")
