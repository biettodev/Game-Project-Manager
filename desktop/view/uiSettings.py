import tkinter

from view.widgetConfigs import *

def Layout(boxes):
    for box in boxes:
        configContainer(box, 20, 10)
               
            
def Form(labels, inputs):
    for i in range(len(labels)):
        configLabel(labels[i])
        configTextBox(inputs[i])
        
def Header(label, input, button, command):
    configLabel(label)
    configTextBox(input)
    configButton(button, command)
 
def Menu(buttons):
    for i in range(len(buttons)):
        print(i)
        # print(key.text)
        # configButton(buttons[i], print('Olá'))
    