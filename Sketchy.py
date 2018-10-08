import Tkinter as tk
import subprocess
import os
import io
from PIL import Image

class App():
    def __init__(self):
        #tk.Tk.__init__(self)
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="white")
        self.canvas.bind("<B1-Motion>",self.draw)# lambda e: self.draw(e.x, e.y))
        self.button1 = tk.Button(self.root, text="save",command=self.save)
        self.button2 = tk.Button(self.root,text="Clean",command=self.clear)
        self.button3 = tk.Button(self.root,text="Exit",command=self.close)
        self.canvas.pack()
        self.button1.pack(padx= 10,side=tk.LEFT)
        self.button2.pack(padx=10,side=tk.LEFT)
        self.button3.pack(padx=10,side=tk.LEFT)
        self.root.mainloop()

    def draw(self,event):
        python_green = "#476042"
        self.x1, self.y1 = ( event.x ), ( event.y )
        self.x2, self.y2 = ( event.x +0.5), ( event.y+0.5 )
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2,fill=python_green,width=10)
        
    def close(self):
        self.root.destroy()

    def clear(self):
        self.canvas.delete("all")
        self.canvas.bind("<B1-Motion>",self.draw)
        

    def save(self):
        ps = self.canvas.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img.save('test.jpg')

app = App()
#app.mainloop()