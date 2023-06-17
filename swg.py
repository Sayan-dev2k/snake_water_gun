from tkinter import *
import random
from PIL import Image,ImageTk

root=Tk()
root.geometry("1400x1000")
root.title("Snake Water Gun")
root.config(bg='#EADDCA')
title=Label(root,text='SNAKE WATER GUN GAME',font=('times new roman',40,'bold'),bg='green',fg='white',bd=5,relief='solid').place(x=0,y=20,relwidth=1)
disp=Label(root,text='YOUR CHOICE',font=('times new roman',30,'bold'),bg='red',fg='white')
disp.place(x=450,y=110)
r=['snake.png','water.png','gun.png']
image1=ImageTk.PhotoImage(Image.open(random.choice(r)))
lbl=Label(root,image=image1)
lbl.image=image1
lbl.place(x=550,y=420)
s=PhotoImage(file='snake.png')
w=PhotoImage(file='water.png')
g=PhotoImage(file='gun.png')
def fun2():
    global c
    global y
    global ro
    if(c>y):
        lbl3.destroy()
    elif(c<y):
        lbl4.destroy()
    else:
        lbl5.destroy()
    c=0
    y=0
    ro=0
    yscore.config(text='0')
    cscore.config(text='0')
    lbl2.config(text='0')
    trybut.destroy()
    exitbut.destroy()


def fun():
    if(ro==10):
        if(c>y):
            # lbl3=Label(root,text='COMPUTER WIN',font=('times new roman',30,'bold'),bg='orange',fg='white')
            lbl3.place(x=1060,y=520)
           
        elif(c<y):
            # lbl3=Label(root,text='YOU WIN',font=('times new roman',30,'bold'),bg='orange',fg='white')
            lbl4.place(x=1060,y=520)
            
        else:
            # lbl3=Label(root,text='MATCH TIED',font=('times new roman',30,'bold'),bg='orange',fg='white')
            lbl5.place(x=1060,y=520)
        trybut.place(x=760,y=700)
        exitbut.place(x=900,y=700)
        # trybut=Button(root,text='Play again',font=('times new roman',15,'bold'),fg='black',command=fun2)
        # exitbut=Button(root,text='Exit',font=('times new roman',15,'bold'),fg='black',command=root.destroy)
        
c=0
y=0
ro=0 
def sfun():
    
    img=random.choice(r)
    image1=ImageTk.PhotoImage(Image.open(img))
    lbl.config(image=image1)
    lbl.image=image1
    global c
    global y 
    global ro
    if(img=='water.png'):
        y=y+1
        yscore.config(text=y)
    elif(img=='gun.png'):
        c=c+1
        cscore.config(text=c)
    else:
        pass
    ro=ro+1
    lbl2.config(text=ro)
    fun()
    # return image1
def wfun():
    img2=random.choice(r)
    # img1=fun()
    image1=ImageTk.PhotoImage(Image.open(img2))
    lbl.config(image=image1)
    lbl.image=image1
    global c
    global y
    global ro 
    if(img2=='gun.png'):
        y=y+1
        yscore.config(text=y)
    elif(img2=='snake.png'):
        c=c+1
        cscore.config(text=c)
    else:
        pass
    ro=ro+1
    lbl2.config(text=ro)
    fun()
def gfun():
    
    img3=random.choice(r)
    # img1=fun()
    image1=ImageTk.PhotoImage(file=img3)
    lbl.config(image=image1)
    lbl.image=image1
    global c
    global y
    global ro 
    if(img3=='snake.png'):
        y=y+1
        yscore.config(text=y)
    elif(img3=='water.png'):
        c=c+1
        cscore.config(text=c)
    else:
        pass
    ro=ro+1
    lbl2.config(text=ro)
    fun()
but1=Button(root,text='snake',image=s,command=sfun)
but1.place(x=350,y=200)
but2=Button(root,text='water',image=w,command=wfun)
but2.place(x=550,y=200)
but3=Button(root,text='gun',image=g,command=gfun)
but3.place(x=750,y=200)
disp1=Label(root,text='COMPUTER CHOICE',font=('times new roman',30,'bold'),bg='red',fg='white')
disp1.place(x=450,y=320)
# image1=ImageTk.PhotoImage(file='snake.png')
# 
# if()
round=Label(root,text='ROUND',font=('times new roman',30,'bold'),bg='blue',fg='white')
round.place(x=1050,y=320)
lbl2=Label(root,text='0',font=('times new roman',25,'bold'),fg='black')
lbl2.place(x=1060,y=420)
you=Label(root,text='YOUR SCORE',font=('times new roman',30,'bold'),bg='#8B8000',fg='white')
you.place(x=300,y=600)
comp=Label(root,text='COMPUTER SCORE',font=('times new roman',30,'bold'),bg='#8B8000',fg='white')
comp.place(x=600,y=600)
yscore=Label(root,text='0',font=('times new roman',25,'bold'),fg='black')
yscore.place(x=360,y=700)
cscore=Label(root,text='0',font=('times new roman',25,'bold'),fg='black')
cscore.place(x=660,y=700)
lbl3=Label(root,text='COMPUTER WIN',font=('times new roman',30,'bold'),bg='orange',fg='white')
lbl4=Label(root,text='YOU WIN',font=('times new roman',30,'bold'),bg='orange',fg='white')
lbl5=Label(root,text='MATCH TIED',font=('times new roman',30,'bold'),bg='orange',fg='white')
trybut=Button(root,text='Play again',font=('times new roman',15,'bold'),fg='black',command=fun2)
exitbut=Button(root,text='Exit',font=('times new roman',15,'bold'),fg='black',command=root.destroy)

root.mainloop()
# if(ro==10):
#     if(c>y):
#         lbl3=Label(root,text='COMPUTER WIN',font=('times new roman',30,'bold'),bg='orange',fg='white')
#         lbl3.place(x=1060,y=520)
#     elif(c<y):
#         lbl3=Label(root,text='YOU WIN',font=('times new roman',30,'bold'),bg='orange',fg='white')
#         lbl3.place(x=1060,y=520)
#     else:
#         lbl3=Label(root,text='GAME TIED',font=('times new roman',30,'bold'),bg='orange',fg='white')
#         lbl3.place(x=1060,y=520)


