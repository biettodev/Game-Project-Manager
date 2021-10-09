import remi.gui as gui

def configContainer(container, padx, pady):
    container['padx'] = padx
    container['pady'] = pady
    container.pack()

def configTextBox(textbox, width=20):
    textbox['font'] = ('Calibri', '9', 'bold')
    textbox['width'] = width
    textbox.pack(side=LEFT)
       
def configButton(button, command, width=10):
    button['font'] = ('Verdana', 9)
    button['width'] = width
    button['command'] =  command
    button.pack(side=LEFT)

def configLabel(label):
    label['font'] = ('Calibri', 12)
    label.pack(side=LEFT)
    