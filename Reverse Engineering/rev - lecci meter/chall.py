#!/usr/bin/python3

import tkinter as tk
from tkinter import *
from Crypto.Util.number import *
from tkinter.messagebox import *
import random

# <============= Operational ==================>
def main():
	def validate(keys):
		if len(keys) != 24:
			return "wrong! don't you dare hacking us"
		else:
			key = [ord(i) for i in keys]
			if (key[12] == (key[2] * 2) - 3) and (key[3] == key[4]) and (key[0] == key[21] + 1) and (key[8] == key[12]) and (key[2] == key[5]) and (key[1] - 2 == key[6]) and (key[23] // 2 == key[22]) and ((key[18] * 2) + 2 == key[17]) and (key[16] == key[0] + 1) and (key[7] * 2 == key[11] + 107) and (key[2] == key[13]) and (key[15] == key[8]) and (key[8] == key[19]) and (key[7] + 7 == key[20] - 6) and (key[9] - 2 == key[14]) and (key[14] == 110) and (key[9] + 3 == key[0]) and (key[5] == (key[9] // 2) - 7) and (key[8] + 13 == key[4]) and (key[11] - 1 == key[13] * 2) and (key[5] + 2 == key[18]) and (key[23] == key[11]) and (key[1] == key[20] - 4) and (key[10] == key[0] + 6):
				return f"LKSJakpus{{{keys}}}"
			else:
				return "wrong! don't you dare hacking us"

	def submit():
		key = inp.get()
		res = validate(key)
		text = StringVar()
		text.set(res)
		textbox = Label(root, textvariable=text, justify='center')
		textbox.config(font=("Courier", 18	))
		textbox.grid(pady=5,row=2,sticky="w")


# <==============  Button Design Code ==============>
	def on_focus_in(entry):
		if entry.cget('state') == 'disabled':
			entry.configure(state='normal')
			entry.delete(0, 'end')


	def on_focus_out(entry, placeholder):
		if entry.get() == "":
			entry.insert(0, placeholder)
			entry.configure(state='disabled')

	root = tk.Tk()
	root.geometry("600x300")
	root.title("Kunci Pintu")
	root.maxsize(600,300)
	root.minsize(600,300)

	inp = Entry(root,width=70,borderwidth=3,relief=RIDGE)
	inp.grid(pady=5,row=0,sticky="w",padx=15)
	inp.insert(0, "Input Secret Key")
	inp.configure(state='disabled')
	x_focus_in = inp.bind('<Button-1>', lambda x: on_focus_in(inp))

	submitbutton = Button(root,text="submit",width=66,command=lambda :submit(),bg="red",fg="white",borderwidth=3,relief=RIDGE)
	submitbutton.grid(row=1,sticky="w",padx=15,pady=5)

	root.mainloop()

# <============ end code ==============>

if __name__ == "__main__":
	main()