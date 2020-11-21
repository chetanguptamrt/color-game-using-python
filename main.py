from tkinter import *
import random

class App():
    def __init__(self):

        self.color=('Brown','Blue','Black','Yellow','White','Orange','Pink','Purple','Green','Red')
        self.root =Tk()
        self.root.title('Color game - chetanguptamrt')
        self.root.geometry('500x600+200+50')
        self.root.configure(bg='#EAF0F1')
        self.root.resizable(False,False)
        self.score=IntVar()
        self.x=0
        self.y=0

        self.image=PhotoImage(file='photos\\logo.png')
        self.lbl1=Label(image=self.image,fg='black',bd=0)
        self.lbl1.pack()
        self.lbl1=Label(text='Game',font='arial 32 bold',fg='black',bg='#EAF0F1')
        self.lbl1.pack()

        self.lbl2=Label(text='Type the colour of the words\nAnd not the word text!',font='arial 18 bold',fg='#25CCF7',bg='#EAF0F1')
        self.lbl2.pack(pady=(10,5))

        self.frame_1=Frame(self.root)
        self.frame_1.pack(pady=10)
        self.lbl4=Label(self.frame_1,text='Time remaining :',font='arial 24 bold',fg='red',bg='#EAF0F1')
        self.lbl4.grid(row=0,column=0)
        self.lbl5=Label(self.frame_1,text='00',font='arial 24 bold',fg='blue',bg='#EAF0F1')
        self.lbl5.grid(row=0,column=1)
        self.lbl6=Label(self.frame_1,text='Score :',font='arial 20 bold',fg='red',bg='#EAF0F1')
        self.lbl6.grid(row=1,column=0)
        self.lbl7=Label(self.frame_1,textvariable=self.score,font='arial 20 bold',fg='blue',bg='#EAF0F1')
        self.lbl7.grid(row=1,column=1)
        self.timer=60

        self.lbl8=Label(text='',font=('cooper black',32,'bold'))
        self.lbl8.pack()

        self.lbl9=Label(text='Enter colour below :',font='arial 16',fg='black',bg='#EAF0F1')
        self.lbl9.pack(pady=(10,5))

        self.entry=Entry(font='arial 16',fg='black',relief='solid')
        self.entry.bind('<Return>',self.check)
        self.entry.config(state='disabled')
        self.entry.pack()

        self.lbl3=Label(text='',font='arial 12 bold',fg='red',bg='#EAF0F1')
        self.lbl3.pack(pady=2)

        self.button=Button(text='Start',padx=8,font='lucida 16',bg='#25CCF7',fg='#000000',command=self.run)
        self.button.pack()

        self.root.mainloop()

    def update_timer(self):
        if self.timer<0:
            self.button.config(state='normal')
            self.entry.delete(0,END)
            self.entry.config(state='disabled')
            self.timer=60
            self.lbl8.config(text='')
        else:
            self.lbl5.configure(text=self.timer)
            self.timer-=1
            self.root.after(1000,self.update_timer)

    def run(self):
        self.update_timer()
        self.get_random()
        self.button.config(state='disabled')
        self.entry.config(state='normal')
        self.score.set(0)
    
    def get_random(self):
        self.x=random.randint(0,9)
        self.y=random.randint(0,9)
        self.lbl8.config(text=self.color[self.x],fg=self.color[self.y])
        

    def check(self,event=0):

        if (self.entry.get()).lower()==self.color[self.y].lower():
            self.score.set(self.score.get()+1)
            self.entry.delete(0,END)
            self.get_random()

app=App()