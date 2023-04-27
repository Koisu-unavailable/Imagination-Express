import tkinter as tk
import main
class todoBox:
    global toid

    todoBoxframe = tk.Frame(root, width = 100, height = 40, )
    toid = 0
    todolist = {0 : None}
    entry = tk.Entry(width=100)
    entry.pack()
    def create(text):
        toid += 1
        todolist.update({toid: text})
        print(todolist[toid])

