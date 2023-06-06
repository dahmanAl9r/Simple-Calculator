import colorama
intr = '''

       Hey Evryone ^_^
        
       Made By Dahman && Zaki <3

  '''
print(intr)

from tkinter import *
#app conf
root = Tk()
root.title("البرنامج الثالث")
root.geometry("600x450")
root.config(bg="white")
root.resizable(False,False)
root.iconbitmap("icon.ico")
#options
#defs
def op1():
    num1 = en_one_Value.get()
    num2 = en_two_Value.get()
    op_view.config(text='= {} + {}'.format(str(num1),str(num2)))
    def report():
        new_num1 = en_one_Value.get()
        new_num2 = en_two_Value.get()
        new_soll = round(new_num1+new_num2,6)
        en_one_Value.set(new_soll)
        report_value.config(text='{}'.format(new_soll))
        op_view.config(text='= {} + {}'.format(str(new_num1),str(new_num2)))
    Button_five.config(command=report)

def op2():
    num1 = en_one_Value.get()
    num2 = en_two_Value.get()
    op_view.config(text='= {} - {}'.format(str(num1),str(num2)))
    def report():
        new_num1 = en_one_Value.get()
        new_num2 = en_two_Value.get()
        new_soll2 = round(new_num1-new_num2,6)
        en_one_Value.set(new_soll2)
        report_value.config(text=new_soll2)
        op_view.config(text='= {} - {}'.format(str(new_num1),str(new_num2)))
        pass
    Button_five.config(command=report)

def op3():
    num1 = en_one_Value.get()
    num2 = en_two_Value.get()
    op_view.config(text='= {} * {}'.format(str(num1),str(num2)))
    def report():
        new_num1 = en_one_Value.get()
        new_num2 = en_two_Value.get()
        op_view.config(text='= {} * {}'.format(str(new_num1),str(new_num2)))
        new_soll3 = round(new_num1*new_num2,6)
        en_one_Value.set(new_soll3)
        report_value.config(text=new_soll3)
    Button_five.config(command=report)
    pass
def op4():
    num1 = en_one_Value.get()
    num2 = en_two_Value.get()
    if num2 == 0:
        report_value.config(text="Error !",fg='red')
    else:
        op_view.config(text='= {} / {}'.format(str(num1),str(num2)))
        def report():
            new_num1 = en_one_Value.get()
            new_num2 = en_two_Value.get()
            op_view.config(text='= {} / {}'.format(str(new_num1),str(new_num2)))
            new_soll4 = round(new_num1/new_num2,6)
            en_one_Value.set(new_soll4)
            report_value.config(text=new_soll4,fg='white')
        Button_five.config(command=report)

#title
title = Label(root,text='الة حاسبة',bg='#333',fg='white',font=("Courier",18))
title.pack(fill=X)
#Entries_texts
#ent1
entry_text_one = Label(root,text="الرقم الاول",fg="red",bg="white",font=("Andalus",15))
entry_text_one.place(x=90,y=50)
#ent2
entry_text_two = Label(root,text="الرقم الثاني",fg="red",bg="white",font=("Andalus",15))
entry_text_two.place(x=430,y=50)
#Entries
#en1
en_one_Value = DoubleVar()
entry_one = Entry(root,textvariable=en_one_Value,relief=SOLID,bd=1,justify="center")
entry_one.place(x=10,y=90,width=240,height=30)
en_one_Value.set(0)
#en2
en_two_Value = DoubleVar()
entry_two = Entry(root,textvariable=en_two_Value,relief=SOLID,bd=1,justify="center")
entry_two.place(x=350,y=90,width=240,height=30)
en_two_Value.set(0)
####buttons
#bt1
Button_one = Button(root,text="+",bg="#165F65",fg="white",relief=SOLID,bd=1,font=("Andalus",18),command=op1,cursor='hand2')
Button_one.place(x=70,y=160,width=110,height=50)
#bt2
Button_two = Button(root,text="-",bg="#165F65",fg="white",relief=SOLID,bd=1,font=("Andalus",18),command=op2,cursor='hand2')
Button_two.place(x=190,y=160,width=110,height=50)
#bt3
Button_three = Button(root,text="x",bg="#165F65",fg="white",relief=SOLID,bd=1,font=("Andalus",18),command=op3,cursor='hand2')
Button_three.place(x=310,y=160,width=110,height=50)
#bt4
Button_four = Button(root,text="/",bg="#165F65",fg="white",relief=SOLID,bd=1,font=("Andalus",18),command=op4,cursor='hand2')
Button_four.place(x=430,y=160,width=110,height=50)
#bt5
Button_five = Button(root,text="=",fg="white",bg="#568F45",font=("Calibri",16),relief=SOLID,bd=1,cursor='hand2')
Button_five.place(x=210,y=260,width=190,height=40)
#report_text
report_value = Label(root,text='',anchor=CENTER,bg="#165F65",fg="white",font=("Calibri",16),relief="sunken",bd=1)
report_value.pack(fill=X,side=BOTTOM)
op_view = Label(root,text='',height=3,anchor='w',bg="white",fg="black",font=("Calibri",16))
op_view.place(x=5,y=330)
root.mainloop()
