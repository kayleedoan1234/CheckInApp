# Ngoc Doan CIS345 Tue Thur 12:00-1:15 Project

from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk
import time
import project_class
import string


# global list_of_transaction,
list_of_transaction =[]
t_number = 0

def show_notification(fname, cost):
    messagebox.showinfo("Polish and Pamper Nail", 'Thank you, ' + fname + '. Your total cost today is $' + str(cost))

def check_in():
    box1.grid_forget()
    welcome_lbl.grid_forget()
    order_frame.grid(column=0, row=1, columnspan=3)
    submit_button.grid(column=0, row=10, pady=15, padx=(35, 0), sticky=W)
    return_button.grid(column=1, row=10, pady=15, padx=(0, 35), sticky=W)


def return_checkin():
    hello_lbl.config(text='Welcome')
    order_frame.grid_forget()
    submit_button.grid_forget()
    return_button.grid_forget()
    box1.grid(row=4, column=0)
    box1.grid_propagate(False)
    welcome_lbl.grid(column=0, row=2, pady=20)
    clear_checkboxes()

def close():
    win.destroy()

def event_handler_key(event):
    invalid_key = [str(i) for i in range(10)]
    if len(name.get()) == 0:
        hello_lbl.config(text='Please enter your name')
    if event.char in invalid_key:
        return 'break'

def phone_entered(event):
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    if len(phone.get()) < 10:
        hello_lbl.config(text='Phone number needs to be 10 digits')
    if len(phone.get()) == 10:
        submit_button.config(state='normal')
    if event.char in alphabet_list or len(phone.get()) >= 10:
        return 'break'




def clear_checkboxes():
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()
    c6.deselect()
    c7.deselect()
    c8.deselect()
    name.set('')
    phone.set('')

def button_click():
    global fname, cost, transactions, datatime, logger, final_transactions, menu_list, t_number
    t_number +=1
    menu_list = ['Gel Manicure','Gel Pedicure','Full Set','Fill','Dipping Powder','Manicure','Pedicure','Kid service']
    datatime = time.ctime()
    print(checkval1.get(),checkval2.get())
    transactions = [checkval1.get(), checkval2.get(),checkval3.get(),checkval4.get(),checkval5.get(),checkval6.get(),checkval7.get(),checkval8.get() ]
    cost=0
    # transactions = list(filter(None, transactions))
    final_transactions = []
    for i, amount in enumerate(transactions):
        if amount !=0:
            cost += amount
            value = menu_list[i]
            final_transactions.append(value)
        else: pass

    cost = f'{cost:.2f}'
    fname = name.get().split(' ')
    fname = fname[0]
    show_notification(fname, cost)
    hello_lbl.config(text='Please tap the Return button')
    new_transaction = project_class.Transaction(t_number, fname,phone.get(), cost)
    list_of_transaction.append(new_transaction)
    final_transactions = ' ,'.join(str(transactions) for transactions in final_transactions)
    logger= [t_number,fname,phone.get(),datatime,final_transactions, str(cost)]
    new_transaction.log_transactions(logger)
    transactions=[]
    final_transactions = []
    clear_checkboxes()


#create main window
win = Tk()
win.title('Polish and Pamper Nail')
win.geometry('450x600')
win.columnconfigure(0, weight=1)
win.config(bg='white')

#for image
p1 = Image.open('Untitled design-2.png')
p1= ImageTk.PhotoImage(p1)
win.iconphoto(False,p1)


#Variable
checkval1 = IntVar()
checkval2 = IntVar()
checkval3 = IntVar()
checkval4 = IntVar()
checkval5 = IntVar()
checkval6 = IntVar()
checkval7 = IntVar()
checkval8 = IntVar()
surveyval = IntVar()
comment = StringVar()
name = StringVar()
phone= StringVar()

#create logo
logo = Image.open('logo.png')
new_width = 350
new_height = 150
img = logo.resize((new_width, new_height), Image.LANCZOS)
img.save('logo1.png')
logo = ImageTk.PhotoImage(img)
logo_label = Label(image=logo, bg='white')
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0, pady=10)

#contact_lbl
contact_lbl= Label(text='Contact: (480)-000-0000', fg="#19376D")
contact_lbl.place(x= 280, y=570)


#gui1: checkin and checkout screen: welcome_lbl, box1
welcome_lbl = Label(win, text='WELCOME', width=30, bg='white',
                 font=('Arial',25), fg='#0B2447')
welcome_lbl.grid(column=0, row=2, pady=20)

box1 = Frame(win, bg='#19376D',width=300, height=200, borderwidth=5,relief=RIDGE)
box1.grid(row=4, column=0)
box1.columnconfigure(0, weight=1)
box1.rowconfigure(0, weight=1)
box1.rowconfigure(1, weight=1)
box1.rowconfigure(2, weight=1)
box1.grid_propagate(False)

checkin_button = Button(box1, command= check_in, font=('Arial', 20), text='Check In')
checkin_button.grid(row=0 , columnspan=3, column=0)

exit_button = Button(box1, command= close, font=('Arial', 20), text='Exit')
exit_button.grid(row=1 , columnspan=3, column=0)
#gui2: box2, info_lbl, order_frame

#create 'Enter your name' label
#create entry box for it
order_frame = Frame(win, width=250, height=200, bg='#19376D')
order_frame.columnconfigure(0, weight=1)
order_frame.columnconfigure(1, weight=1)
order_frame.rowconfigure(0, weight=1)
order_frame.rowconfigure(1, weight=1)

name_lbl = Label(order_frame, text='Enter your name: ', bg='#19376D',
                 font=('Arial', 16), fg='white')
name_lbl.grid(column=0, row=0, pady=10, padx=(10,0))

name_entry = Entry(order_frame, textvariable=name, justify=CENTER,
                   font=('chalkboard', 14))
name_entry.grid(column=1, row=0,padx=10)
#Make sure name doesnt include numbers
name_entry.bind('<Key>', event_handler_key)


phone_lbl = Label(order_frame, text='Phone number: ', bg='#19376D',
                 font=('Arial', 16), fg='white')
phone_lbl.grid(column=0, row=1, pady=10)

phone_entry = Entry(order_frame, textvariable=phone, justify=CENTER,
                    font=('chalkboard', 14))
phone_entry.grid(column=1, row=1, padx=10)
phone_entry.bind('<Key>', phone_entered)

#create hello/totalcharge label
hello_lbl = Label(order_frame, text='Welcome!', width=30, bg='white',
                 font=('Arial', 16), fg='black')
hello_lbl.grid(columnspan=4, column=0, row=3, pady=10)

info_lbl = Label(order_frame, text='Please choose the service you would like today: ', bg='#19376D',
                 font=('Arial', 16,'bold'), fg='white')
info_lbl.grid(columnspan=4, column=0, row=4, pady=15)

#create a frame
box2 = Frame(order_frame, bg='white',width=320, height=120,relief=RIDGE)
box2.columnconfigure(0, weight=1)
box2.columnconfigure(1, weight=1)
box2.rowconfigure(0, weight=1)
# box2.rowconfigure(1, weight=1)

box2.grid(row=5, column=0, columnspan=4, pady=10)
box2.grid_propagate(False)

#create 8 checkboxes
c1 = Checkbutton(box2, text="Gel Manicure($35)", fg= '#6f4e37', bd=5, variable= checkval1, font=("Arial", 15), onvalue=35, offvalue =0)
c1.grid(row=0, column=0, sticky=NSEW)
c2 = Checkbutton(box2, text="Gel Pedicure($44)", fg= '#6f4e37', bd=5, variable= checkval2, font=("Arial", 15), onvalue=44, offvalue =0)
c2.grid(row=0, column=1, sticky=NSEW)
c3 = Checkbutton(box2, text="Full Set($50)", fg= '#6f4e37', bd=5, variable= checkval3, font=("Arial", 15), onvalue=50, offvalue =0)
c3.grid(row=1, column=0, sticky=NSEW)
c4 = Checkbutton(box2, text="Fill($40)", fg= '#6f4e37', bd=5, variable= checkval4, font=("Arial", 15), onvalue=40, offvalue =0)
c4.grid(row=1, column=1, sticky=NSEW)
c5 = Checkbutton(box2, text="Dipping Powder($40)", fg= '#6f4e37', bd=5, variable= checkval5, font=("Arial", 15), onvalue=40, offvalue =0)
c5.grid(row=2, column=0, sticky=NSEW)
c6 = Checkbutton(box2, text="Manicure($20)", fg= '#6f4e37', bd=5, variable= checkval6, font=("Arial", 15), onvalue=20, offvalue =0)
c6.grid(row=2, column=1, sticky=NSEW)
c7 = Checkbutton(box2, text="Pedicure($30)", fg= '#6f4e37', bd=5, variable= checkval7, font=("Arial", 15), onvalue=30, offvalue =0)
c7.grid(row=3, column=0, sticky=EW)
c8 = Checkbutton(box2, text="Kid service($20)", fg= '#6f4e37', bd=5, variable= checkval8, font=("Arial", 15), onvalue=20, offvalue =0)
c8.grid(row=3, column=1, sticky=EW)

#button
submit_button = Button(win, command=button_click, font=('Arial', 16), text='Check in', width=15)
return_button = Button(win, command=return_checkin, font=('Arial', 16), text='Return', width=15)

#error handling
if len(phone.get()) < 10 or len(name.get()) == 0:
    submit_button.config(state='disabled')

win.mainloop()