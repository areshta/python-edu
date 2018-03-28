import os
from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import askopenfilename

def openfile():

   filename = askopenfilename(parent=root)
   f = open(filename)
   print (">>>>>>>>>>>>>>>> " + filename) 
   f.read()
   f.close()

root = Tk()

openfile()




