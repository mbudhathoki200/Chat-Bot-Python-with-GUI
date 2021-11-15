from tkinter import *
import cv2
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
import os, json
from PIL import ImageTk, Image
import os
import csv

def searchByques(question):
    ansArr = []
    csv_file=csv.reader(open("ChatBot.csv",'r'));
    count = 0;
    for row in csv_file:
        if question=="":
            ansArr.append(str("Please Enter something!!!"))
            break;
        elif question in row[0]:
            print("The answer is: {}".format(row[1]));
            ansArr.append(str(row[1]))
            count+=1;

    else:
        if count == 0:
            print("Sorry!!!No answer!!");
            ansArr.append(str("Result Not Found!"))
    return ansArr

def img_src(src, imgsize):
    try:
        openimg = ImageTk.Image.open(src)
        w, h = openimg.size
        if sum(imgsize) > 1:
            openimg = openimg.resize(imgsize, Image.CUBIC)
        timg = ImageTk.PhotoImage(openimg)
        return timg
    except Exception as e:
        showerror("Error", str(e))

root = Tk()
root.geometry('700x800')
root.title('Chat-Bot')
root.wm_resizable(height=False,width=False)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
ans = []



def switch_scrn(frame):
    if str(frame) == ".!frame2":
        r_f = Frame(root,bg='#363636',height=800,width=800)
        r_f.place(x=0,y=0)
        answer(r_f)
        frame = r_f
    frame.tkraise()



def search(searchdata):
    global ans
    ans = searchByques(str(searchdata))
    switch_scrn(fanswer)


def home(frame):
    Button(frame,text='Search',fg='white',bg='#43B379',border=5,font=('arial',15,'bold'),command = lambda : search(homeEntry.get())).place(x=288,y=502,height=60,width=120)
    Label(frame,text='Chat-Bot',fg='White',bg='#363636',font=('arial',35,'bold')).place(x=45,y=138,height=50,width=600)
    homeEntry = Entry(frame,fg='white',bg='grey',border=1,font=('arial',15,'normal'))
    homeEntry.place(x=107,y=396,height=50,width=500)
    Label(frame,text='How can i help you?',fg='white',bg='#363636',border=0,font=('arial',15,'normal')).place(x=77,y=307,height=50,width=300)
    Label(frame,text='Hello!! I am your Bot.',fg='White',bg='#363636',font=('arial',15,'normal')).place(x=84,y=236,height=50,width=300)


def answer(frame):
    global ans
    yinc=0
    Label(frame, text='Your Answer is', fg='white', bg='#363636', font=('arial', 40, 'bold')).place(x=105, y=92,
                                                                                                    height=50,
                                                                                          width=500)
    Button(frame, text='Ask Again?', fg='White', bg='#43B379', border=3, font=('arial', 15, 'normal'),command = lambda : switch_scrn(fhome)).place(x=269,y = 619,
                                                                                                         width=150)
    Label(frame, fg='black', bg='grey').place(x=10, y=252, height=300, width=680)

    text = Text(frame,fg="white",bg="grey",border=0,state="normal")


    for a in ans:
        if a != 'Result Not Found!':
            a = f"{a}"

        # Label(frame,text=a, fg='white', bg='grey').place(x=0,height=100,y=252+yinc,width=700)
        text.insert(INSERT,a+"\n\n")

        yinc+=60
    text.configure(state="disabled")
    text.place(x=25,y=252, height=300, width=650);


    print("sdasd",ans)

fhome=Frame(root,bg='#363636',height=800,width=700)
fhome.place(x=0,y=0)
fanswer=Frame(root,bg='#363636',height=800,width=700)
fanswer.place(x=0,y=0)


home(fhome)
answer(fanswer)

switch_scrn(fhome)
root.mainloop()