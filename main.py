from tkinter import*




root=Tk()
root.geometry("440x610")

root.resizable(0,0)


root.title('calculator')
root.configure(background="light green")
root.iconbitmap('C:/Users/ACER/Desktop/cal.ico')
e=Entry(root,text='',width=27,borderwidth=10,font='lucid 20 bold',bg='blue',fg='white')
e.grid(row=0,column=0,columnspan=3,pady=10,padx=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_number= e.get()
    global f_num
    global math
    math='addition'
    f_num = int(first_number)
    e.delete(0,END)
def button_sub():
    first_number= e.get()
    global f_num
    global math
    math='subtraction'
    f_num = int(first_number)
    e.delete(0,END)

def button_mul():
    first_number= e.get()
    global f_num
    global math
    math='multiplication'
    f_num = int(first_number)
    e.delete(0,END)
def button_div():
    first_number= e.get()
    global f_num
    global math
    math='division'
    f_num = int(first_number)
    e.delete(0,END)
def button_floor():
    first_number= e.get()
    global f_num
    global math
    math='floordivision'
    f_num = int(first_number)
    e.delete(0,END)
def button_equal():

    second_number = e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,f_num + int(second_number))
    elif math=='subtraction':
        e.insert(0, f_num - int(second_number))
    elif math=='multiplication':
        e.insert(0, f_num * int(second_number))
    elif math=='division':
        e.insert(0, f_num / int(second_number))
    elif math=='floordivision':
        e.insert(0, f_num // int(second_number))





b1=Button(root,text='9',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(9))
b2=Button(root,text='8',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(8))
b3=Button(root,text='7',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(7))
b4=Button(root,text='6',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(6))
b5=Button(root,text='5',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(5))
b6=Button(root,text='4',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(4))
b7=Button(root,text='3',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(3))
b8=Button(root,text='2',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(2))
b9=Button(root,text='1',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(1))
b10=Button(root,text='+',font='lucid 20 bold',fg='red',bg='black',command= button_add)
b11=Button(root,text='0',font='lucid 20 bold',fg='white',bg='black',command=lambda :button_click(0))
b12=Button(root,text='-',font='lucid 20 bold',fg='red',bg='black',command= button_sub)
b13=Button(root,text='*',font='lucid 20 bold',fg='red',bg='black',command= button_mul)
b14=Button(root,text='//',font='lucid 20 bold',fg='red',bg='black',command=button_floor)


b15=Button(root,text='=',font='lucid 20 bold',fg='red',bg='black',command=button_equal)
b16=Button(root,text='/',font='lucid 20 bold',fg='red',bg='black',command= button_div)
b17=Button(root,text='clear',font='lucid 20 bold',fg='red',bg='black',command=button_clear)

b1.grid(column=0,row=1,pady=10,padx=10,ipadx=20,ipady=7)
b2.grid(column=1,row=1,pady=10,padx=10,ipadx=20,ipady=7)
b3.grid(column=2,row=1,pady=10,padx=10,ipadx=20,ipady=7)
b4.grid(column=0,row=2,pady=10,padx=10,ipadx=20,ipady=7)
b5.grid(column=1,row=2,pady=10,padx=10,ipadx=20,ipady=7)
b6.grid(column=2,row=2,pady=10,padx=10,ipadx=20,ipady=7)
b7.grid(column=0,row=3,pady=10,padx=10,ipadx=20,ipady=7)
b8.grid(column=1,row=3,pady=10,padx=10,ipadx=20,ipady=7)
b9.grid(column=2,row=3,pady=10,padx=10,ipadx=20,ipady=7)
b10.grid(column=0,row=4,pady=10,padx=10,ipadx=20,ipady=7)
b11.grid(column=1,row=4,pady=10,padx=10,ipadx=20,ipady=7)
b12.grid(column=2,row=4,pady=10,padx=10,ipadx=20,ipady=7)
b13.grid(column=0,row=5,pady=10,padx=10,ipadx=30,ipady=7)
b14.grid(column=1,row=5,pady=10,padx=10,ipadx=30,ipady=7)

b15.grid(column=2,row=5,pady=10,padx=10,ipadx=20,ipady=7)
b16.grid(column=0,row=6,pady=10,padx=10,ipadx=30 , ipady=7 )
b17.grid(column=1,row=6,columnspan=3,pady=10,padx=10,ipadx=30,ipady=7)






root.mainloop()