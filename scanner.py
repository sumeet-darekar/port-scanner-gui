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
        service="tcp"
        Label(root,text=f"Url: {input.get()}").grid(column=1,row=22)
        for port in range(int(port1_input.get()),int(port2_input.get())+1):
                root.update()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                output_text.config(text=f"Scanning tcp port :{port}\n")
                if not s.connect_ex((input.get(), port)):
                        cur_label = 'label' + str(i)
                        cur_label = Label(root,text=f"Open Port: {port}  |  Service: {socket.getservbyport(port, service)}").grid(column=1,row=24+i,padx=30)
                i=i+1

def udp_scanner():
        for port in range(int(port1_input.get()),int(port2_input.get())+1):
                try:
                        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
                                udp_socket.settimeout(1)  # Set a timeout for the receive operation
                                udp_socket.sendto(b'', (input.get(), port))
                                response, _ = udp_socket.recvfrom(1024)
                                cur_label = 'label' + str(i)
                                cur_label = Label(root,text=f"Open Port: {port}").grid(column=1,row=28+i,padx=30)
                                return True
                except (socket.timeout, ConnectionRefusedError):
                        return False



def option():
        if(var1.get()==1):
                scanner()
        elif(var2.get()==1):
                if(udp_scanner()):
                        udp_scanner()
                else:
                        Label(root,text="Udp ports are closed").grid(column=0,row=24)
                        
        else:
                output_text.config(text="Failed to check... Specify tcp or udp check")

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
        #command=option
    
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


button = Button(root,text=" scan ", bootstyle="primary, toolbutton", command=option)
button.grid(column=1, row=20 ,pady=10)


output_text = Label(root,text="")
output_text.grid(column=1, row=23)


output_text2 = Label(root,text="")
output_text2.grid(column=1, row=23)


root.mainloop()