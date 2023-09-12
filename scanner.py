from tkinter import *
from ttkbootstrap import *
import socket
import sys
import time
from threading import Thread


root=Window(themename="cyborg")
root.title("Scanner")
root.iconbitmap('icon.ico')
root.geometry("750x500")


lable1 = Label(root,text="Url : ", anchor="w")
lable1.grid(column=0, row=15, padx=10, pady=25)

#port scanner
def scanner():
        i=0
        for port in range(int(port1_input.get()),int(port2_input.get())+1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                cu_label = 'label' + str(i)
                cu_label = Label(root,text=f"scan {port}").grid(column=0,row=22+i)
                if not s.connect_ex((input.get(), port)):
                        cur_label = 'label' + str(i)
                        cur_label = Label(root,text=f"open : {port}").grid(column=1,row=23+i)
                i=i+1


#input field
input = Entry(root,width=50)
input.insert(0,"https://")
input.grid(column=1, row=15)

#Port
lable2 = Label(root,text="Port Range :")
lable2.grid(column=3,row=15,padx=15)

#Port Input1 first

port1_input = Entry(root,width=5)
port1_input.insert(0,"")
port1_input.grid(column=4, row=15)

#port input2 last
port2_input = Entry(root,width=5)
port2_input.insert(0,"")
port2_input.grid(column=5, row=15,padx=5)

var1 = IntVar()
sqtoggle = Checkbutton(bootstyle="success, square-toggle",
        text="TCP scan",
        variable=var1,
        onvalue=1,
        offvalue=0,
    
)
sqtoggle.grid(column=0,row=17)

var2 = IntVar()
sqtoggle = Checkbutton(bootstyle="success, square-toggle",
        text="UDP scan",
        variable=var2,
        onvalue=1,
        offvalue=0
)
sqtoggle.grid(column=1,row=17,pady=25)


button = Button(root,text=" scan ", bootstyle="primary, toolbutton", command=scanner)
button.grid(column=1, row=20 ,pady=10)


output_text = Label(root,text="")
output_text.grid(column=1, row=22)

root.mainloop()