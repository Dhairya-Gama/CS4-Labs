from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Connect 4')

#root.geometry("1200x710")



clicked = True
count = 0


# disable all the buttons
def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)


def b_click(b):
	pass

def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42
	global b43, b44, b45, b46, b47, b48, b49
	global list1, list2, list3, list4, list5, list6, list7
	global clicked, count
	clicked = True
	count = 0

	# Build our buttons
	b43 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b43))
	b44 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b44))
	b45 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b45))
	b46 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b46))
	b47 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b47))
	b48 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b48))
	b49 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b49))	





	b1 = Button(root, text="CLICK", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
	b2 = Button(root, text="CLICK", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
	b3 = Button(root, text="CLICK", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

	b4 = Button(root, text="CLICK", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
	b5 = Button(root, text="CLICK", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
	b6 = Button(root, text="CLICK", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
	b7 = Button(root, text="CLICK", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
	b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
	b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
	b10 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b10))
	b11 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b11))
	b12 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b12))
	b13 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b13))
	b14 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b14))
	b15 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b15))
	b16 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b16))
	b17 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b17))
	b18 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b18))
	b19 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b19))
	b20 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b20))
	b21 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b21))
	b22 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b22))
	b23 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b23))
	b24 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b24))
	b25 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b25))
	b26 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b26))
	b27 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b27))
	b28 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b28))
	b29 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b29))
	b30 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b30))
	b31 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b31))
	b32 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b32))
	b33 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b33))
	b34 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b34))
	b35 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b35))
	b36 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b36))
	b37 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b37))
	b38 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b38))
	b39 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b39))
	b40 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b40))
	b41 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b41))
	b42 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b42))






	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)
	b4.grid(row=0, column=3)
	b5.grid(row=0, column=4)
	b6.grid(row=0, column=5)
	b7.grid(row=0, column=6)
	b8.grid(row=1, column=0)
	b9.grid(row=1, column=1)
	b10.grid(row=1, column=2)
	b11.grid(row=1, column=3)
	b12.grid(row=1, column=4)
	b13.grid(row=1, column=5)
	b14.grid(row=1, column=6)
	b15.grid(row=2, column=0)
	b16.grid(row=2, column=1)
	b17.grid(row=2, column=2)
	b18.grid(row=2, column=3)
	b19.grid(row=2, column=4)
	b20.grid(row=2, column=5)
	b21.grid(row=2, column=6)
	b22.grid(row=3, column=0)
	b23.grid(row=3, column=1)
	b24.grid(row=3, column=2)
	b25.grid(row=3, column=3)
	b26.grid(row=3, column=4)
	b27.grid(row=3, column=5)
	b28.grid(row=3, column=6)
	b29.grid(row=4, column=0)
	b30.grid(row=4, column=1)
	b31.grid(row=4, column=2)
	b32.grid(row=4, column=3)
	b33.grid(row=4, column=4)
	b34.grid(row=4, column=5)
	b35.grid(row=4, column=6)
	b36.grid(row=5, column=0)
	b37.grid(row=5, column=1)
	b38.grid(row=5, column=2)
	b39.grid(row=5, column=3)
	b40.grid(row=5, column=4)
	b41.grid(row=5, column=5)
	b42.grid(row=5, column=6)
	b43.grid(row=6, column=0)
	b44.grid(row=6, column=1)
	b45.grid(row=6, column=2)
	b46.grid(row=6, column=3)
	b47.grid(row=6, column=4)
	b48.grid(row=6, column=5)
	b49.grid(row=6, column=6)

	list1 = [b1, b8, b15, b22, b29, b36, b43]
	list2 = [b2, b9, b16, b23, b30, b37, b44]
	list3 = [b3, b10, b17, b24, b31, b38, b45]
	list4 = [b4, b11, b18, b25, b32, b39, b46]
	list5 = [b5, b12, b19, b26, b33, b40, b47]
	list6 = [b6, b13, b20, b27, b34, b41, b48]
	list7 = [b7, b14, b21, b28, b35, b42, b49]



def getLowest(column):

	for a in range(1, len(column)):
		if column[a]["bg"] == "SystemButtonFace":
			lowest = column[a]
	return lowest


def isColumnFilled(col):
	bool = True
	for x in range(len(col)):
		if col[x]["bg"] == "SystemButtonFace":
			bool = False
	return bool



def checkifwon():
	pass

# Button clicked function
def b_click(b):
	global clicked, count




	if b["text"] == "CLICK" and clicked == True:
		if b in list1:
			if not (isColumnFilled(list1)):
				temp = getLowest(list1)
				temp["bg"] = "red"
				clicked = False
				count += 1
				checkifwon()


		elif b in list2:
			if not (isColumnFilled(list2)):
				temp = getLowest(list2)
				temp["bg"] = "red"
				clicked = False
				count += 1
				checkifwon()


		elif b in list3:
			if not (isColumnFilled(list3)):
				temp = getLowest(list3)
				temp["bg"] = "red"
				clicked = False
				count += 1
				checkifwon()


		elif b in list4:
			if not (isColumnFilled(list4)):
				temp = getLowest(list4)
				temp["bg"] = "red"
				clicked = False
				count += 1
				checkifwon()


		elif b in list5:
			if not (isColumnFilled(list5)):
				temp = getLowest(list5)
				temp["bg"] = "red"
				clicked = False
				count += 1
				checkifwon()


		elif b in list6:
			if not (isColumnFilled(list6)):
				temp = getLowest(list6)
				temp["bg"] = "red"
				clicked = False
				count += 1
				checkifwon()


		elif b in list7:
			if not (isColumnFilled(list7)):
				temp = getLowest(list7)
				temp["bg"] = "red"
				clicked = False
				count += 1
				checkifwon()


	elif b["text"] == "CLICK" and clicked == False:
		if b in list1:
			if not (isColumnFilled(list1)):
				temp = getLowest(list1)
				temp["bg"] = "blue"
				clicked = True
				count += 1
				checkifwon()


		elif b in list2:
			if not (isColumnFilled(list2)):
				temp = getLowest(list2)
				temp["bg"] = "blue"
				clicked = True
				count += 1
				checkifwon()


		elif b in list3:
			if not (isColumnFilled(list3)):
				temp = getLowest(list3)
				temp["bg"] = "blue"
				clicked = True
				count += 1
				checkifwon()


		elif b in list4:
			if not (isColumnFilled(list4)):
				temp = getLowest(list4)
				temp["bg"] = "blue"
				clicked = True
				count += 1
				checkifwon()


		elif b in list5:
			if not (isColumnFilled(list5)):
				temp = getLowest(list5)
				temp["bg"] = "blue"
				clicked = True
				count += 1
				checkifwon()


		elif b in list6:
			if not (isColumnFilled(list6)):
				temp = getLowest(list6)
				temp["bg"] = "blue"
				clicked = True
				count += 1
				checkifwon()


		elif b in list7:
			if not (isColumnFilled(list7)):
				temp = getLowest(list7)
				temp["bg"] = "blue"
				clicked = True
				count += 1
				checkifwon()
	else:
		messagebox.showerror("Not a valid Box" )

my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)

reset()

root.mainloop()
