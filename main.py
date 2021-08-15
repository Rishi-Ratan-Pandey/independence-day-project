from tkinter import*;import time;import threading;import random
root=Tk()
root.title('Independence Day With Python!!!!!!!!!!!!!!!')
root.geometry('400x600')
break_or_not=True
length=24
l=0
full_wishing_string='Happy Independence Day!!'
string=''
colors_=['orange','white','blue','green']
def change_color():
    random_colors_=random.choice(colors_)
    wishing_label['fg']=random_colors_
def animation():
    global l,length,string
    while True:
        time.sleep(0.100)
        try:
            string+=full_wishing_string[l]
            change_color()
        except:
            l-=24
            string=''
            change_color()
            continue
        l+=1
        wishing_label.config(text=string)
wishing_label=Label(root,text='',font=('Arial Rounded MT bold',20,'bold'))
flag=PhotoImage(file='image.png')
flag_label=Label(root,image=flag)
flag_label.pack()
flag_label.place(x=1)
wishing_label.place(x=1,y=550)
threading.Thread(target=animation).start()
mainloop()
########
