import tkinter as tk

root = tk.Tk()

root.title("Графическая программа на Python")
root.geometry("800x600")

ww = 800
wh = 600

canvas = tk.Canvas(root, width=ww, height=wh)
canvas.pack()

canvas.create_oval(10, 10, 100, 100, fill="red")

class Aplication(tk.Frame):
    def __init__(self, mycanvas, master=None):
        tk.Frame.__init__(self, master)
        self.myroot =  master
        self.x = 50
        self.y = 50
        self.delta_base = 20
        self.delta = self.delta_base
        self.deltax = self.delta_base
        self.deltay = self.delta_base
        self.mycanvas = mycanvas
        master.bind('<Left>', self.leftKey)
        master.bind('<Right>', self.rightKey)
        master.bind("<Button-1>", self.mouseClick)
        self.pack()
        self.draw()
        self.onUpdate()

    def draw(self):
        self.mycanvas.create_oval(self.x, self.y, self.x+100, self.y+100, fill="green")
        self.myroot.update()

    def leftKey(self, event):
        self.x -= self.delta

    def rightKey(self, event):
        self.x += self.delta

    def mouseClick(self, event):
        self.mycanvas.create_oval(event.x-50, event.y-50 , event.x+50, event.y+50, fill="blue")
        self.myroot.update()

    def onUpdate(self):
        self.x += self.deltax
        if self.x > ww:
            self.deltax = -self.delta_base
        if self.x < 0:
            self.deltax = self.delta_base

        self.y += self.deltay
        if self.y > wh:
            self.deltay = -self.delta_base
        if self.y < 0:
            self.deltay = self.delta_base

        self.draw()
        self.after(200, self.onUpdate)

app = Aplication(canvas,root)

root.update()

root.mainloop()