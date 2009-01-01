from tkinter import *

def configContainer(container, padx, pady):
    container['padx'] = padx
    container['pady'] = pady
    container.pack()

def configTextBox(textbox, width, font):
    textbox['width'] = width
    textbox['font'] = font
    textbox.pack(side=LEFT)
       
def configButton(button, text, command):
    button['width'] = 12 
    button['text'] = text
    button['command'] =  command
    button.pack(side=LEFT)