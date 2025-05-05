import pyfiglet 
from termcolor import colored

msg = input("What do you want to print? ")
color = input("What color? ")

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

if color not in valid_colors:
    color = "magenta"
    
art_msg = pyfiglet.figlet_format(msg)
colored_ascii = colored(art_msg, color=color)
print(colored_ascii)