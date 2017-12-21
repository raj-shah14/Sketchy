from tkinter import *
import pyautogui
from PIL import Image
import os
import io
import subprocess




def save():
    ps=canvas.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save('test.jpg')
    print("File Saved")
    root.destroy()
    
def close():
    root.destroy()

def clear():
    canvas.create_rectangle(5, 5, 700, 700, fill="white")

def paint(event):
    python_green = "#476042"
    x1, y1 = ( event.x ), ( event.y )
    x2, y2 = ( event.x ), ( event.y )
    canvas.create_oval( x1, y1, x2, y2, fill = python_green )

def erase():
    for x in xrange(event.x-5, event.x+5+1):
        for y in xrange(event.y-5, event.y+5+1):
            try:
                p = canvas.getpixel((x, y))
                canvas.putpixel((x, y), p)
            except IndexError:
                pass
    

root=Tk()
root.title('Scratchy!')
frame=Frame(root,width=700,height=700)
canvas=Canvas(frame,width=700,height=700)

canvas.create_rectangle(5, 5, 700, 700, fill="white")
canvas.bind("<B1-Motion>",paint)


buttonframe=Frame(root)
buttonframe.grid(row=2, column=0, columnspan=3)
Button(buttonframe,text="Save",command=save).grid(row=0,column=0)
Button(buttonframe,text="Clean",command=clear).grid(row=0,column=1)
Button(buttonframe,text="Exit",command=close).grid(row=0,column=2)
Button(buttonframe,text="Erase",command=erase).grid(row=0,column=3)
canvas.pack()
#button1.pack()
#button2.pack()
#button3.pack()
buttonframe.pack()
frame.pack()


root.mainloop()
