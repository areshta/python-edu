#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Text, Scrollbar, Menu, messagebox, filedialog, BooleanVar, Checkbutton, Label, Entry, StringVar, Grid, Frame, Button, Toplevel
import os, subprocess, json, string
from datetime import datetime
from Crypto.Cipher import AES

import areditor

class ArFile:
    def __init__(self, fpath):
        self.fpath = fpath

    def check(self):
        return os.path.exists(self.fpath)

class ArCrypt:
    def __init__(self, psw):
        #print( psw)
        self.skey = psw * 3
        print(self.skey[0:16])
        self.key = str.encode(self.skey[0:16])

    def encrypt(self,txt):
        self.cipher = AES.new(self.key, AES.MODE_CFB, self.key)
        self.msg = self.cipher.encrypt(str.encode(txt))
        return self.msg


class PswDialog:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Password: ").pack()

        self.e = Entry(top, show = '*')
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        #print ("value is", self.e.get())
        self.psw = self.e.get();

        self.top.destroy()

if __name__ == "__main__":

    arFile = ArFile("./my1.bin")

    root = Tk()
    d = PswDialog(root)
    root.wait_window(d.top)

    crypt = ArCrypt(d.psw)

    root.wm_state('normal')

    editor = areditor.Editor(root)
    editor.file_path = arFile.fpath
    editor.set_title()
    editor.main()

    #Button(root, text="Hello!").pack()
    #root.update()

    if not arFile.check():
        dt = datetime.now()
        with open(arFile.fpath, 'ab') as the_file:
            msg = 'Initial:' + str(datetime.now()) + '\n';
            crMsg = crypt.encrypt(msg)
            #print(crMsg)
            the_file.write(bytearray(crMsg))

    editor.file_open(filepath=arFile.fpath)
    root.mainloop()
