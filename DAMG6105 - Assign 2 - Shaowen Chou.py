print("Hello World")


# Assignment 2 
# 2. Dice simulator: Create a six and eight-sided dice simulator. Please make sure that it is a fair die. Cover it with a simple, easy to use GUI.

# import modules
#import GUI visualization model
from tkinter import *

# Python Imaging Library to perform operations on Images
# from PIL import ImageTk, Image
import PIL

import itertools

# import for Random capabaility
import random

background_color = "#0D865D"

root = Tk()

# GUI window size
root.geometry("960 x 720")

# Default image (just the dice, no values... i.e.: Square)
dice_one_image_path = "./0.png"
dice_two_image_path = "./0.png"



# 6 sided dice
dice_one_image = ImageTK.PhotoImage(Image.open(dice_one_image_path))
dice_one_label = Label(root, image = dice_one_image, bg = background_color)
dice_one_label.pack()


# 8 sided dice
dice_two_image = ImageTK.PhotoImage(Image.open(dice_two_image_path))
dice_two_label = Label(root, image = dice_two_image, bg = background_color)
dice_two_label.pack()


# Rolling the dice
def dice_roll():
    # returns a value from 1 through 6 (up to 7, not inclusive)
    dice_numbers = list(range(1,7))
    combinations = list(itertools.product(dice_numbers, repeat = 2))

    rolled_dice = random.choice(combinations)
    return rolled_dice


# Function that will update the dice image depending on the combination of dice rolled
def update_dice_image():
    rolled_dice = dice_roll()
    print(rolled_dice)

    new_first_image_path = "./().png".format(rolled_dice[0])
    new_second_image_path = "./().png".format(rolled_dice[1])

    new_first_dice_image = ImageTk.PhotoImage(Image.open(new_first_image_path))
    new_second_dice_image = ImageTk.PhotoImage(Image.open(new_second_image_path))

    first_dice_label.configure(Image = new_first_dice_image)
    second_dice_label.configure(Image = new_second_dice_image)

    dice_one_label.image = new_first_dice_image
    dice_two_label.image = new_second_dice_image
    
# Create a button to click to roll the dice
roll_button = Button(root, text = "Roll the dices!", command = update_roll_dice_image)
roll_button.pack(side = BOTTOM)

root.configure(bg = background_color)
root.mainloop()