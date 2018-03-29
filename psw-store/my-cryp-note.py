#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Text, Scrollbar, Menu, messagebox, filedialog, BooleanVar, Checkbutton, Label, Entry, StringVar, Grid, Frame
import os, subprocess, json, string
from datetime import datetime

import areditor

class ArFile:
    fpath = "./in.txt2"

    def check(self):
        return os.path.exists(self.fpath)

class ArCryptor:
    def __init__(self):
        a = 1

if __name__ == "__main__":
    arFile = ArFile()
    root = Tk()
    root.wm_state('normal')
    editor = areditor.Editor(root)
    editor.file_path = arFile.fpath
    editor.set_title()
    editor.main()

    if not arFile.check():
        dt = datetime.now()
        with open(ArFile.fpath, 'a') as the_file:
            the_file.write('Initial:' + str(datetime.now()) + '\n')

    editor.file_open(filepath=ArFile.fpath)
    root.mainloop()
