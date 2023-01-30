'''IMPORTING REQUIRED MODULES'''
from tkinter import *
from tkinter.ttk import Style, Button, Radiobutton, Entry
from tkinter import messagebox
import random as rand
import mysql.connector as conn

'''CONNECTING WITH MYSQL SERVER'''
connecting_with_mysql = conn.connect(host='localhost', user='root', password='ketan45@', database='bank_customer')
cursor = connecting_with_mysql.cursor()

'''CREATING HOME PAGE'''

def login_signup_exit():
    root = Tk()
    root.geometry('400x275')
    root.maxsize(width=400, height=275)
    root.minsize(width=400, height=275)
    root.title('WELCOME TO OUR BANK')
    root.config(bg='LightSteelBlue1')
    style2 = Style()
    style2.configure('TButton', bg='LightSkyBlue3', font=('Franklin Gothic Demi', 10, 'bold'))

    '''STYLING BUTTONS AND CREATING FRAMES'''

    frame1 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X)
    frame2 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=RIGHT)
    frame3 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X, side=BOTTOM)
    frame4 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=LEFT)

    '''CREATING FUNCTIONS FOR USE IN BUTTONS'''

    def exit():
        root.destroy()  # DESTROYING WINDOW

    def sign():
        root.destroy()  # DESTROYING WINDOW AND USING CREATED FUNCTION
        signup()

    def login1():
        root.destroy()
        login()

    '''CREATING BUTTONS'''
    login_button = Button(text='LOGIN', command=login1).place(relx=0.5, rely=0.3, anchor=CENTER)
    signup_button = Button(text='SIGNUP', command=sign).place(relx=0.5, rely=0.45, anchor=CENTER)
    exit_button = Button(text='EXIT', command=exit).place(relx=0.5, rely=0.60, anchor=CENTER)
    root.mainloop()  # EXITING A WINDOW


'''CREATING SIGNUP FUNCTON FOR CREATE AN ACCOUNT'''


def signup():
    '''SAME AS LOGIN_SIGNUP_EXIT CREATING WINDOW AND FRAMES'''
    root1 = Tk()
    root1.geometry('500x400')
    root1.maxsize(width=500, height=400)
    root1.minsize(width=500, height=400)
    root1.title('CREATE AN ACCOUNT')
    root1.config(bg='LightSteelBlue1')
    frame1 = Frame(root1, height=20, bg='LightSkyBlue3').pack(fill=X)
    frame2 = Frame(root1, width=20, bg='LightSkyBlue3').pack(fill=Y, side=RIGHT)
    frame3 = Frame(root1, height=20, bg='LightSkyBlue3').pack(fill=X, side=BOTTOM)
    frame4 = Frame(root1, width=20, bg='LightSkyBlue3').pack(fill=Y, side=LEFT)
    '''TAKING NAME INPUT IN THREE WAYS FNAME,MNAME,LNAME'''
    name = Label(text='NAME :', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.1, rely=0.1)

    def name_end(event):
        name_entry.delete(first=0, last=10)

    name_entry = Entry()
    name_entry.insert(10, 'Fname')
    name_entry.bind('<Button-1>', name_end)

    def name2_end(event):
        name_entry1.delete(first=0, last=10)

    name_entry1 = Entry()
    name_entry1.insert(10, 'Mname')
    name_entry1.bind('<Button-1>', name2_end)

    def name3_end(event):
        name_entry2.delete(first=0, last=10)

    name_entry2 = Entry()
    name_entry2.insert(10, 'Lname')
    name_entry2.bind('<Button-1>', name3_end)
    '''TAKING DOB ENTRIES'''
    dob = Label(text='DOB :', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.1, rely=0.2)

    def end(event):
        dob_entry.delete(first=0, last=20)

    def end1(event):
        dob_entry1.delete(first=0, last=20)

    def end2(event):
        dob_entry2.delete(first=0, last=20)

    dob_entry = Entry()
    dob_entry1 = Entry()
    dob_entry2 = Entry()
    dob_entry.insert(10, 'YYYY')
    dob_entry1.insert(10, 'MM')
    dob_entry2.insert(10, 'DD')
    dob_entry.bind('<Button-1>', end)
    dob_entry1.bind('<Button-1>', end1)
    dob_entry2.bind('<Button-1>', end2)
    '''TAKING EMAIL AND PHONE NUMBER'''
    email = Label(text='EMAIL :', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.1, rely=0.3)
    email_entry = Entry()
    phone_no = Label(text='PHONE :', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.1, rely=0.4)

    def end3(event):
        phone_entry.delete(first=0, last=10)

    phone_entry = Entry()
    phone_entry.insert(10, 'OPTIONAL')
    phone_entry.bind('<Button-1>', end3)

    def home():
        root1.destroy()
        login_signup_exit()

    '''CREATING EXIT AND HOME BUTTON'''
    exit2_button = Button(text='EXIT', command=root1.destroy).pack(anchor='ne', side=TOP)
    hone_button = Button(text='HOME', command=home).place(relx=0.65, rely=0.05)
    '''CREATING RADIBUTTONS FOR SELECT GENDER'''
    gender = Label(text='GENDER :', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.1, rely=0.5)
    gender_var = StringVar(root1)
    gender1 = Radiobutton(text='M', variable=gender_var, value='Male')
    gender2 = Radiobutton(text='F', variable=gender_var, value='Female')
    gender3 = Radiobutton(text='OTHER', variable=gender_var, value='Other')
    '''TAKING ACCOUNT BALANCE'''
    Label(text='ACCOUNT BALANCE :', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.1, rely=0.8)
    account_balance_entry = Entry()

    def message():
        if account_type.get() == 'saving':
            messagebox.showinfo(message='IT ZERO-BALANCE ACCOUNT')
        else:
            messagebox.showinfo(message=' IT IS MANDATORY TO ADD 500RS BALANCE')

    '''CREATING ACCOUNT TYPE RADIOBUTTONS'''
    account_type = StringVar(root1)
    account_button = Radiobutton(text='SAVING', variable=account_type, value='saving', command=message)
    Label(text='ZERO BALANCE ACCOUNT', bg='LightBlue1', font=('Century', 8, 'bold')).place(relx=0.50, rely=0.6)
    Label(text='MINIMUM 500RS REQUIRED', bg='LightBlue1', font=('Century', 8, 'bold')).place(relx=0.50, rely=0.7)
    account_button2 = Radiobutton(text='CURRENT', variable=account_type, value='current', command=message)
    '''CREATING FUNCTIO FOR CHECKING DATATYPES'''

    def get():
        '''CREATING ACCOUNT NUMBER AND PIN FOR ACCOUNT USING GETTING ACCOUNT NUMBER AND ACCOUNT PIN FROM MYSQL'''
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        account_number_str1 = ''
        account_pin_str2 = ''
        query = "select account_number,account_pin from customer_info"
        cursor.execute(query)
        data = cursor.fetchall()
        dict1 = {x[0]: x[1] for x in data}
        connecting_with_mysql.commit()
        while True:
            '''CREATING ACCOUNT NUMBER AND PIN USING RANDOM MODULE'''
            rand1 = rand.choices(list1, k=6)
            rand2 = rand.choices(list1, k=4)
            for i in rand1:
                account_number_str1 += str(i)
            for j in rand2:
                account_pin_str2 += str(j)
            if int(account_number_str1) in dict1.keys():
                continue
            else:
                break
        '''CHECKING ENTRIES INFO FOR TAKE CORRECT ENTRIES(CHECKING CONDITIONS)'''
        if not name_entry.get().strip().isalpha() or not name_entry1.get().strip().isalpha() or \
                not name_entry2.get().strip().isalpha():
            messagebox.showwarning(message='PLEASE GIVE NAME.\n DONT USE NUMBERS OR CHARACTERS.')

        elif name_entry.get().strip() == 'Fname' or name_entry1.get().strip() == 'Mname' or \
                name_entry2.get().strip() == 'Lname':
            messagebox.showwarning(message='PLEASE GIVE NAME.\n DONT USE NUMBERS OR CHARACTERS.')

        elif not dob_entry.get().strip().isnumeric() or not dob_entry1.get().strip().isnumeric() or\
                not dob_entry2.get().strip().isnumeric():
            messagebox.showwarning(message='PLEASE GIVE RIGHT DOB(IN NUMBERS)')

        elif int(dob_entry.get().strip()) < 1900 and int(dob_entry.get().strip()) > 2022:
            messagebox.showwarning(message='YOUR AGE CANT FIT IN OUR POLICIES')

        elif int(dob_entry1.get().strip()) > 12 or int(dob_entry1.get().strip()) == 0:
            messagebox.showwarning(message='YOUR ENTER WRONG MONTH')

        elif int(dob_entry2.get().strip()) > 31 or int(dob_entry2.get().strip()) == 0:
            messagebox.showwarning(message='YOUR ENTER WRONG DATE')

        elif int(dob_entry1.get().strip()) in [4, 6, 9, 11] and int(dob_entry2.get().strip()) > 30:
            messagebox.showwarning(message='YOUR ENTER WRONG DATE')

        elif (int(dob_entry.get().strip()) % 4 == 0 or int(dob_entry.get().strip()) % 400 == 0) and \
                int(dob_entry1.get().strip()) == 2 and int(dob_entry2.get().strip()) >= 30:
            messagebox.showwarning(message='YOUR ENTER WRONG DATE IT IS LEAP YEAR')

        elif int(dob_entry.get().strip()) % 4 != 0 and int(dob_entry1.get().strip()) == 2 and \
                int(dob_entry2.get().strip()) >= 29:
            messagebox.showwarning(message='YOUR ENTER WRONG DATE IT IS NOT LEAP YEAR')

        elif not email_entry.get().strip().endswith(('.com', '.in')):
            messagebox.showwarning(message='PLEASE GIVE PROPER EMAIL')

        elif not phone_entry.get().strip().isnumeric() and phone_entry.get() != 'OPTIONAL' and \
                phone_entry.get().strip() != '':
            messagebox.showwarning(message='PLEASE GIVE PHONE NUMBER OTHERWISE STAY IT BLANK')

        elif account_type.get() == 'saving' and account_balance_entry.get().strip() != '' and \
                not account_balance_entry.get().isnumeric():
            messagebox.showwarning(message='PLEASE GIVE NUMBERS FORMAT')

        elif account_type.get() == 'current' and not account_balance_entry.get().strip().isnumeric():
            messagebox.showwarning(message='PLEASE ADD 500 RS OR MORE AND NOT ALPHABETS')

        elif account_type.get() == 'current' and int(account_balance_entry.get().strip()) < 500:
            messagebox.showwarning(message='PLEASE ADD 500 RS OR MORE AND NOT ALPHABETS')

        elif name_entry.get() and dob_entry.get() and email_entry.get() and gender_var.get() and account_type.get():
            if account_type.get() == 'saving' and account_balance_entry.get().strip() == '':
                account_balance_entry.insert(0, '0')
            main_name = f'{name_entry.get().strip()} {name_entry1.get().strip()} {name_entry2.get().strip()}'
            main_dob = f'{dob_entry.get().strip()}-{dob_entry1.get().strip()}-{dob_entry2.get().strip()}'
            '''INSERTING SIGNUP ENTREIES IN MYSQL'''
            inserting_data = "INSERT INTO customer_info(account_number,account_pin,name,phone,email," \
                             "gender,account_type,account_balance,account_date)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            insert = (int(account_number_str1), int(account_pin_str2), str(main_name), str(phone_entry.get().strip()),
                      str(email_entry.get().strip()),
                      str(gender_var.get()), str(account_type.get()),
                      int(account_balance_entry.get().strip()), str(main_dob))
            cursor.execute(inserting_data, insert)
            connecting_with_mysql.commit()
            messagebox.showinfo(message=f'YOUR ACCOUNT IS SUCCESFULLY CREATED\n'
                                        f'YOUR ACCOUNT NUMBER IS: {int(account_number_str1)}\n'
                                        f'PASSWORD IS: {int(account_pin_str2)}')
            home()

        else:
            messagebox.showinfo(message='PLEASE GIVE ALL INFO')

    '''PLACEING ALL THE BUTTONS AND ENTRIES'''
    enter_button = Button(text='ENTER', command=get).place(relx=0.3, rely=0.87)
    name_entry.place(relx=0.3, rely=0.1, width=46)
    name_entry1.place(relx=0.4, rely=0.1, width=46)
    name_entry2.place(relx=0.5, rely=0.1, width=46)
    dob_entry.place(relx=0.3, rely=0.2, width=35)
    dob_entry1.place(relx=0.38, rely=0.2, width=30)
    dob_entry2.place(relx=0.46, rely=0.2, width=30)
    email_entry.place(relx=0.3, rely=0.3)
    phone_entry.place(relx=0.3, rely=0.4)
    gender1.place(relx=0.3, rely=0.5)
    gender2.place(relx=0.405, rely=0.5)
    gender3.place(relx=0.498, rely=0.5)
    account_button.place(relx=0.30, rely=0.6)
    account_button2.place(relx=0.30, rely=0.7)
    account_balance_entry.place(relx=0.5, rely=0.8)
    root1.mainloop()


'''CREATING FUNCTION FOR USE IN LOGIN PAGE'''


def dashboard(number):
    root3 = Tk()
    root3.geometry('400x275')
    root3.maxsize(width=400, height=275)
    root3.minsize(width=400, height=275)
    root3.title('CUSTOMER DASHBOARD')
    root3.config(bg='LightSteelBlue1')

    '''STYLING BUTTONS AND CREATING FRAMES'''

    frame1 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X)
    frame2 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=RIGHT)
    frame3 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X, side=BOTTOM)
    frame4 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=LEFT)
    '''GETTING ALL INFO FROM MYSQL TO SHOW ON DASHBOARD'''
    query = f'select name,account_date,account_balance from customer_info where account_number = {number}'
    cursor.execute(query)
    info = cursor.fetchall()
    Label(text=f'INFORMATION OF ACCOUNT HOLDER :', bg='honeydew', font=('Century', 9, 'bold')).place(
        relx=0.15,
        rely=0.2)
    Label(text=f'NAME:  {info[0][0]}', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.2,
                                                                                           rely=0.3)
    Label(text=f'DATE OF BIRTH:  {info[0][1]}', bg='LightBlue1', font=('Century', 9, 'bold')).place(
        relx=0.2,
        rely=0.4)
    Label(text=f'AC NUMBER:  {number}', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.2,
                                                                                            rely=0.5)
    Label(text=f'BANKING SERVICES:', bg='honeydew', font=('Century', 9, 'bold')).place(
        relx=0.15,
        rely=0.6)
    '''FUNCTION FOR LOG OUT BUTTON'''

    def logout():
        root3.destroy()
        login()

    Button(text='LOG OUT', command=logout).pack(anchor='ne', side=TOP)
    '''FUNCTION FOR DEPOSIT BUTTON'''

    def credit_button1():
        root3.destroy()
        root4 = Tk()
        root4.geometry('300x200')
        root4.maxsize(width=300, height=200)
        root4.minsize(width=300, height=200)
        root4.title('DEPOSIT AMOUNT')
        root4.config(bg='LightSteelBlue1')

        '''STYLING BUTTONS AND CREATING FRAMES'''

        frame1 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X)
        frame2 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=RIGHT)
        frame3 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X, side=BOTTOM)
        frame4 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=LEFT)

        def enter(event):
            amount.delete(first=0, last=20)

        amount = Entry()
        amount.insert(20, 'Enter a amount')
        amount.bind('<Button-1>', enter)
        '''FUNCTION FOR ENTER BUTTON AND CHECKING CONDITIONS'''

        def enter1():
            if not amount.get().strip().isnumeric():
                messagebox.showwarning(message='PLEASE GIVE AMOUNT IN NUMBERS')
            elif len(amount.get().strip()) > 10:
                messagebox.showwarning(message='WE CAN NOT TAKE THAT MUCH INPUT')
            else:
                balance = int(amount.get().strip()) + info[0][2]
                query = f'update customer_info set account_balance = {balance} where account_number = {number}'
                cursor.execute(query)
                connecting_with_mysql.commit()
                messagebox.showinfo(message='SUCESSFULLY CREDITED')
                root4.destroy()
                dashboard(number)

        '''FUNCTION FOR CANCEL BUTTON'''

        def cancel1():
            root4.destroy()
            dashboard(number)

        amount.place(relx=0.3, rely=0.3)
        enter1 = Button(text='ENTER', command=enter1).place(relx=0.25, rely=0.5)
        cancel = Button(text='CANCEL', command=cancel1).place(relx=0.55, rely=0.5)
        root4.mainloop()

    '''CREATING FUNCTION FOR WITHDRAW MONEY'''

    def debit_button1():
        root3.destroy()
        root5 = Tk()
        root5.geometry('300x200')
        root5.maxsize(width=300, height=200)
        root5.minsize(width=300, height=200)
        root5.title('WITHDRAW AMOUNT')
        root5.config(bg='LightSteelBlue1')

        '''STYLING BUTTONS AND CREATING FRAMES'''

        frame1 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X)
        frame2 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=RIGHT)
        frame3 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X, side=BOTTOM)
        frame4 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=LEFT)

        def enter(event):
            amount.delete(first=0, last=20)

        amount = Entry()
        amount.insert(20, 'Enter a amount')
        amount.bind('<Button-1>', enter)
        '''CREATING FUNCTION FOR ENTER BUTTON'''

        def enter1():
            if not amount.get().strip().isnumeric():
                messagebox.showwarning(message='PLEASE GIVE AMOUNT IN NUMBERS')
            elif (info[0][2] - int(amount.get().strip())) < 0:
                messagebox.showwarning(message='INSUFFICIENT BALANCE')
            else:
                balance = info[0][2] - int(amount.get().strip())
                query = f"update customer_info set account_balance = {balance} where account_number = {number}"
                cursor.execute(query)
                connecting_with_mysql.commit()
                messagebox.showinfo(message='SUCESSFULLY DEBITED.')
                root5.destroy()
                dashboard(number)

        '''CREATING FUNCTION FOR CANCEL BUTTON'''

        def cancel1():
            root5.destroy()
            dashboard(number)

        amount.place(relx=0.3, rely=0.3)
        enter1 = Button(text='ENTER', command=enter1).place(relx=0.25, rely=0.5)
        cancel = Button(text='CANCEL', command=cancel1).place(relx=0.55, rely=0.5)
        root5.mainloop()

    '''CREATING FUNCTION FOR BALANCE CHECK BUTTON'''

    def check():
        messagebox.showinfo(message=f'YOUR ACCOUNT BALANCE IS {info[0][2]}')

    '''PLACING ALL THE BUTTONS AND ENTRIES'''
    a = Button(text='DEPOSIT', command=credit_button1)
    b = Button(text='WITHDRAW', command=debit_button1)
    c = Button(text='CHECK BALANCE', command=check)
    a.place(relx=0.3, rely=0.7)
    b.place(relx=0.5, rely=0.7)
    c.place(relx=0.38, rely=0.8)
    root3.mainloop()


'''CREATING LOGIN PAGE'''


def login():
    root2 = Tk()
    root2.geometry('400x275')
    root2.maxsize(width=400, height=275)
    root2.minsize(width=400, height=275)
    root2.title('LOGIN')
    root2.config(bg='LightSteelBlue1')

    '''STYLING BUTTONS AND CREATING FRAMES'''

    frame1 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X)
    frame2 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=RIGHT)
    frame3 = Frame(height=20, bg='LightSkyBlue3').pack(fill=X, side=BOTTOM)
    frame4 = Frame(width=20, bg='LightSkyBlue3').pack(fill=Y, side=LEFT)
    '''CREATING ACCOUNT NUMBER AND PIN BUTTONS'''
    Label(text='AC_NUMBER:', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.19, rely=0.30)
    Label(text='PASSWORD:', bg='LightBlue1', font=('Century', 9, 'bold')).place(relx=0.19, rely=0.45)

    account_number_entry = Entry()
    account_pin_entry = Entry()
    '''GETTING INFO FROM MYSQL FOR CHECKING ACCOUNT NUMBER AND PIN'''
    query = "select account_number,account_pin from customer_info"
    cursor.execute(query)
    data = cursor.fetchall()
    dict2 = {x[0]: x[1] for x in data}
    connecting_with_mysql.commit()

    def home():
        root2.destroy()
        login_signup_exit()

    '''ENTER BUTTON FUNCTION TO GO CHECK ACCOUNT NUMBER AND PIN GET IN DASHBOARD SECTION'''

    def enter_button1():
        if not account_number_entry.get().strip().isnumeric() or not account_pin_entry.get().strip().isnumeric():
            messagebox.showwarning(message='PLEASE ENTER NUMBERS')
        elif int(account_number_entry.get().strip()) not in dict2.keys():
            messagebox.showwarning(message='INVALID ACCOUNT NUMBER')
        elif int(account_pin_entry.get().strip()) != dict2.get(int(account_number_entry.get().strip())):
            messagebox.showwarning(message='INVALID PASSWORD')
        else:
            number = account_number_entry.get()  # variable for give in dashboard function
            root2.destroy()
            dashboard(number)  # function for deposit,withdraw and balance check

    '''PLACING ALL THE BUTTONS'''
    exit2_button = Button(text='EXIT', command=root2.destroy).pack(anchor='ne', side=TOP)
    home_button = Button(text='HOME', command=home).place(relx=0.56, rely=0.074)
    enter_button = Button(text='ENTER', command=enter_button1).place(relx=0.36, rely=0.60)
    account_number_entry.place(relx=0.47, rely=0.30)
    account_pin_entry.place(relx=0.47, rely=0.45)
    root2.mainloop()


if __name__ == '__main__':
    login_signup_exit()
    connecting_with_mysql.close()  # closing the mysqlserver
