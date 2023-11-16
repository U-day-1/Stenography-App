from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb 

root=Tk()
root.title("Steganography")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#618264")

#commands for OS
def openimg():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                    title='Select Image File')
    '''                                       ,
                                    filetype=(("PNG File","*.png"),
                                              ("JPG File","*.jpg"),
                                              ("All File","*.txt")))'''
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    print(filename)
    

def Encode():
    global secret
    global filename
    message=txt.get(1.0,END)
    secret=lsb.hide(str(filename),message)
    print("Message Encoded")
    
def Decode():
    clear_message = lsb.reveal(filename)
    txt.delete(1.0,END)
    txt.insert(END,clear_message)

def saveimg():
    global secret
    global filename,name
    name=fname.get(1.0, "end-1c")
    secret.save("C:\\Users\\uday8\\Documents\\Projects\\Stetography\\"+name+".png")
    print("Image Saved")
    

image_icon=PhotoImage(file="C:\\Users\\uday8\\Documents\\Projects\\Stetography\\L1.png")
root.iconphoto(False,image_icon)


Label(root,text="Stenography App",bg="#618264",fg="white",font="arial 25 bold").place(x=200,y=10)

f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)
   
lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

f2=Frame(root,bd=3,width=340,height=280,bg="#D0E7D2",relief=GROOVE)
f2.place(x=350,y=80)

txt=Text(f2,font="Robote 20",bg="#D0E7D2",fg="black",relief=GROOVE,wrap=WORD)
txt.place(x=0,y=0,width=320,height=230)

fname=Text(f2,font="Robote 15",bg="lightgray",fg="black",relief=GROOVE,wrap=WORD)
fname.place(x=130,y=238,width=200,height=30)
Label(f2,text="File name: ",width=10,height=2,font="arial 14 bold",bg="#D0E7D2").place(x=0,y=230)

sc=Scrollbar(f2)
sc.place(x=320,y=0,height=300)

sc.configure(command=txt.yview)
txt.configure(yscrollcommand=sc.set)

f3=Frame(root,bd=3,bg="#B0D9B1",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)

Button(f3,text="Open Image",width=10,height=2,font="arial 14 bold",command=openimg).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",command=saveimg).place(x=180,y=30)
Label(f3,text=".png .jpeg . jpg etc",bg="#B0D9B1",fg="black").place(x=20,y=5)

f4=Frame(root,bd=3,bg="#B0D9B1",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)

Button(f4,text="Encode",width=10,height=2,font="arial 14 bold",command=Encode).place(x=20,y=30)
Button(f4,text="Decode",width=10,height=2,font="arial 14 bold",command=Decode).place(x=180,y=30)
Label(f4,text=".png .jpeg . jpg etc",bg="#B0D9B1",fg="black").place(x=20,y=5)


root.mainloop()