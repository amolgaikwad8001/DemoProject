import tkinter as tk
from datetime import datetime

from tkinter import messagebox
from time import gmtime, strftime
current_time = datetime.now()


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0


def check_acc_nmb(num):
    try:
        fpin = open(num + ".txt", 'r')
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid Credentials!\nTry Again!")
        return 0
    fpin.close()
    return


def home_return(master):
    master.destroy()
    Main_Menu()


def write(master, name, oc, pin):
    if ((is_number(name)) and (is_number(oc) == 0) and (is_number(pin) == 0) and name == ""):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    f1 = open("Accnt_Record.txt", 'r')
    accnt_no = int(f1.readline())
    accnt_no += 1
    f1.close()

    f1 = open("Accnt_Record.txt", 'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet = open(str(accnt_no) + ".txt", "w")
    fdet.write(pin + "\n")
    fdet.write(oc + "\n")
    fdet.write(str(accnt_no) + "\n")
    fdet.write(name + "\n")
    fdet.close()

    frec = open(str(accnt_no) + "-rec.txt", 'w')
    frec.write("Date                                     Credit                       Debit                         Balance in Rs.\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]     ", gmtime())) + "        " + oc + "                           " + oc + "      \n")
    frec.close()

    messagebox.showinfo("Details", "Your Account Number is:" + str(accnt_no))
    master.destroy()
    return

#amount credit write
def crdt_write(master, amt, accnt, name):
    if (is_number(amt) == 0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    fdet = open(accnt + ".txt", 'r')
    pin = fdet.readline()
    camt = int(fdet.readline())
    fdet.close()
    amti = int(amt)
    cb = amti + camt
    fdet = open(accnt + ".txt", 'w')
    fdet.write(pin)
    fdet.write(str(cb) + "\n")
    fdet.write(accnt + "\n")
    fdet.write(name + "\n")
    fdet.close()
    frec = open(str(accnt) + "-rec.txt", 'a+')
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + str(amti) + "                "+"                " + str(cb) + "\n")
    frec.close()
    messagebox.showinfo("Operation Successfull!!", "Amount Credited Successfully!!")
    master.destroy()
    return

#amount dbit write
def debit_write(master, amt, accnt, name):
    if (is_number(amt) == 0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    fdet = open(accnt + ".txt", 'r')
    pin = fdet.readline()
    camt = int(fdet.readline())
    fdet.close()
    if (int(amt) > camt):
        messagebox.showinfo("Error!!", "You dont have that amount left in your account\nPlease try again.")
    else:
        amti = int(amt)
        cb = camt - amti
        fdet = open(accnt + ".txt", 'w')
        fdet.write(pin)
        fdet.write(str(cb) + "\n")
        fdet.write(accnt + "\n")
        fdet.write(name + "\n")
        fdet.close()
        frec = open(str(accnt) + "-rec.txt", 'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime())) + "              " + "              " + str(
            amti) + "              " + str(cb) + "\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!", "Amount Debited Successfully!!")
        master.destroy()
        return
#Amount Credit

def Cr_Amt(accnt, name):
    creditwn = tk.Tk()
    creditwn.geometry("600x300")
    creditwn.title("Credit Amount")
    creditwn.configure(bg="aqua")
    fr1 = tk.Frame(creditwn, bg="blue")
    l_title = tk.Message(creditwn, text="STATE BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(creditwn, relief="raised", text="Enter Amount to be credited: ")
    e1 = tk.Entry(creditwn, relief="raised")
    l1.place(x=130, y=100)
    e1.place(x=300, y=100)
    b = tk.Button(creditwn, text="Credit", relief="raised", command=lambda: crdt_write(creditwn, e1.get(), accnt, name))
    b.place(x=250, y=150)
    creditwn.bind("<Return>", lambda x: crdt_write(creditwn, e1.get(), accnt, name))

#amount debit
def De_Amt(accnt, name):
    debitwn = tk.Tk()
    debitwn.geometry("600x300")
    debitwn.title("Debit Amount")
    debitwn.configure(bg="palegreen1")
    fr1 = tk.Frame(debitwn, bg="sky blue")
    l_title = tk.Message(debitwn, text="STATE BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(debitwn, relief="raised", text="Enter Amount to be debited: ")
    e1 = tk.Entry(debitwn, relief="raised")
    l1.place(x=130, y=100)
    e1.place(x=300, y=100)
    b = tk.Button(debitwn, text="Debit", relief="raised", command=lambda: debit_write(debitwn, e1.get(), accnt, name))
    b.place(x=250, y=150)
    debitwn.bind("<Return>", lambda x: debit_write(debitwn, e1.get(), accnt, name))

  # Balance Check
def disp_bal(accnt):
    fdet = open(accnt + ".txt", 'r')
    fdet.readline()
    bal = fdet.readline()
    fdet.close()
    messagebox.showinfo("Balance","Your Balance fetched successfully !! \n\n Rs."+str(bal))
    
#Transition History
def disp_tr_hist(accnt):
    disp_wn = tk.Tk()
    disp_wn.geometry("900x600")
    disp_wn.title("Transaction History")
    disp_wn.configure(bg="#76EEC6")
    fr1 = tk.Frame(disp_wn, bg="sky blue")
    l_title = tk.Message(disp_wn, text="STATE BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="gray", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    fr1 = tk.Frame(disp_wn)
    fr1.pack(side="top")
    l1 = tk.Message(disp_wn, text="Your Transaction History:", padx=100, pady=20, width=1000, bg="red", fg="green",
                    relief="raised")
    l1.pack(side="top")
    fr2 = tk.Frame(disp_wn)
    fr2.pack(side="top")
    frec = open(accnt + "-rec.txt", 'r')
    for line in frec:
        l = tk.Message(disp_wn, anchor="w", text=line, relief="raised", width=2000)
        l.pack(side="top")
    b = tk.Button(disp_wn, text="Quit", relief="raised", command=disp_wn.destroy)
    b.pack(side="top")
    frec.close()

#After Login Menu
def logged_in_menu(accnt, name):
    rootwn = tk.Tk()
    rootwn.geometry("1600x800")
    rootwn.title("STATE BANK-" + name)
    rootwn.configure(background='olivedrab1')
    
    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")
    l_title = tk.Message(rootwn, text="SIMPLE BANKING\n SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                         fg="white", bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    label = tk.Label(text="Logged in as: " + name, relief="raised", bg="black", fg="white", anchor="center",
                     justify="center")
    label.pack(side="top")
    img2 = tk.PhotoImage(file="credit.gif")
    myimg2 = img2.subsample(2, 2)
    img3 = tk.PhotoImage(file="debit.gif")
    myimg3 = img3.subsample(2, 2)
    img4 = tk.PhotoImage(file="balance1.gif")
    myimg4 = img4.subsample(2, 2)
    img5 = tk.PhotoImage(file="transaction.gif")
    myimg5 = img5.subsample(2, 2)
    b2 = tk.Button(image=myimg2, command=lambda: Cr_Amt(accnt, name))
    b2.image = myimg2
    b3 = tk.Button(image=myimg3, command=lambda: De_Amt(accnt, name))
    b3.image = myimg3
    b4 = tk.Button(image=myimg4, command=lambda: disp_bal(accnt))
    b4.image = myimg4
    b5 = tk.Button(image=myimg5, command=lambda: disp_tr_hist(accnt))
    b5.image = myimg5

    img6 = tk.PhotoImage(file="logout.gif")
    myimg6 = img6.subsample(2, 2)
    b6 = tk.Button(image=myimg6, relief="raised", command=lambda: logout(rootwn))
    b6.image = myimg6

    b2.place(x=110, y=160)
    b3.place(x=110, y=280)
    b4.place(x=900, y=160)
    b5.place(x=900, y=280)
    b6.place(x=500, y=400)

#logout
def logout(master):
    messagebox.showinfo("Logged Out", "You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()


def check_log_in(master, name, acc_num, pin):
    if (check_acc_nmb(acc_num) == 0):
        master.destroy()
        Main_Menu()
        return

    if ((is_number(name)) and (is_number(pin) == 0)):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        Main_Menu()
    else:
        master.destroy()
        logged_in_menu(acc_num, name)

#login
def log_in(master):
    master.destroy()
    loginwn = tk.Tk()
    loginwn.geometry("600x400")
    loginwn.title("Log in")
    loginwn.configure(bg="sky blue")
    fr1 = tk.Frame(loginwn, bg="blue")
    l_title = tk.Message(loginwn, text="STATE BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(loginwn, text=" Enter Name :", relief="raised")
    l1.place(x=180, y=100)

    e1 = tk.Entry(loginwn)
    e1.place(x=270, y=100)
    l2 = tk.Label(loginwn, text="Enter Account Number :", relief="raised")
    l2.place(x=130, y=140)
    e2 = tk.Entry(loginwn)
    e2.place(x=270, y=140)
    l3 = tk.Label(loginwn, text=" Enter your PIN :", relief="raised")
    l3.place(x=160, y=190)
    e3 = tk.Entry(loginwn, show="*")
    e3.place(x=270, y=190)
    b = tk.Button(loginwn, text="LOGIN",
                  command=lambda: check_log_in(loginwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    b.place(x=230, y=250)
    b1 = tk.Button(text="HOME", relief="raised", bg="aqua", fg="red", command=lambda: home_return(loginwn))
    b1.place(x=330, y=250)
    loginwn.bind("<Return>", lambda x: check_log_in(loginwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))

#create new account 
def Create():
    crwn = tk.Tk()
    crwn.geometry("600x400")
    crwn.title("Create new Account")
    crwn.configure(bg="pink")
    fr1 = tk.Frame(crwn, bg="blue")
    l_title = tk.Message(crwn, text="STATE BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    print('\n')
    l1 = tk.Label(crwn, text=" Enter Name :", relief="raised")
    l1.place(x=180, y=100)
    e1 = tk.Entry(crwn)
    e1.place(x=270, y=100)
    l2 = tk.Label(crwn, text=" Enter opening credit :", relief="raised")
    l2.place(x=140, y=140)
    e2 = tk.Entry(crwn)
    e2.place(x=270, y=140)
    l3 = tk.Label(crwn, text=" Enter desired PIN : ", relief="raised")
    l3.place(x=150, y=190)
    e3 = tk.Entry(crwn, show="*")
    e3.place(x=270, y=190)
    b = tk.Button(crwn, text="Submit",
                  command=lambda: write(crwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    b.place(x=280, y=230)
    
    return
#home Page

def Main_Menu():
    rootwn = tk.Tk()
    rootwn.geometry("1600x800")
    rootwn.title("STATE BANK")
    rootwn.configure(background='sky blue')
    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file="pile1.gif")
    x = tk.Label(image=bg_image)
    x.place(y=-400)
    l_title = tk.Message(text="SIMPLE BANKING\n SYSTEM", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    imgc1 = tk.PhotoImage(file="new.gif")
    imglo = tk.PhotoImage(file="login.gif")
    imgc = imgc1.subsample(2, 2)
    imglog = imglo.subsample(2, 2)

    b1 = tk.Button(image=imgc, command=Create)
    b1.image = imgc
    b2 = tk.Button(image=imglog, command=lambda: log_in(rootwn))
    b2.image = imglog
    img6 = tk.PhotoImage(file="quit.gif")
    myimg6 = img6.subsample(2, 2)

    b6 = tk.Button(image=myimg6, command=rootwn.destroy)
    b6.image = myimg6
    b1.place(x=800, y=300)
    b2.place(x=800, y=200)
    b6.place(x=920, y=400)

    rootwn.mainloop()


Main_Menu()
