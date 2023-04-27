#-------------------------------------------------------------------------------
# Name:        Imagination Express
# Purpose:     Make To DO lists organize your day, and feel motivated doing it
#
# Author:      Jamil Alausa
#
# Created:     26-04-2023
# Copyright:   (c) jalau 2023
# Licence:     I don't have a license, yet.
#-------------------------------------------------------------------------------

import tkinter as tk
from bob import *


class app:
#__init__ the app
    global root
    root = tk.Tk()
    root.geometry("1280x720")
    root["bg"] ="black"






enter = tk.Button(root, text = "Create a new task", command = todoBox.create(todoBox.entry.get()))
enter.pack()

class TopBar:
    TopFrame = tk.LabelFrame(width = 1280, height = 50, bg = "white", text = "Imagination Express", fg = "black", bd = "0", font = 100)
    TopFrame.pack(side = "top")




def __innit__():
    TopBar()



if __name__ == '__main__':
    __innit__()
    root.mainloop()

