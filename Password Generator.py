from tkinter import *
import pyperclip
import random

root = Tk()
root.geometry("600x400")
passstr = StringVar()
passlen = IntVar()
passlen.set(0)


class Generator:
    def __init__(self):
        self.total_pass = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                           'u', 'v', 'w', 'x', 'y', 'z']

    def initialize(self):
        self.pass_upper = ['A', 'B', 'C', 'D',
                           'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
                           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                           'Y', 'Z']
        self.pass_num = ['1', '2', '3', '4', '5', '6', '7', '8',
                         '9']
        self.pass_sym = ['!', '@', '#', '$', '%', '^', '&',
                         '*', '(', ')']
        self.pass_len = 0

# ----------------------------------------------------------------------------------------------------------------------
    def generate(self):
        password = ""
        for x in range(self.pass_len.get()):
            password = password + random.choice(self.total_pass)
        passstr.set(password)

    def write_pw(self):
        f = open('Saved_Passwords.txt', 'a')

# ----------------------------------------------------------------------------------------------------------------------
    def upper_chk(self):
        if upper_chk.get() == 1:
            self.add_upper()
        else:
            self.rem_upper()

    def add_upper(self):
        self.total_pass = self.total_pass + self.pass_upper

    def rem_upper(self):
        self.total_pass = [e for e in self.total_pass if e not in ('A', 'B', 'C', 'D',
                                                                   'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
                                                                   'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                                                                   'Y', 'Z')]

# ----------------------------------------------------------------------------------------------------------------------
    def num_chk(self):
        if num_chk.get() == 1:
            self.add_num()
        else:
            self.rem_num()

    def add_num(self):
        self.total_pass = self.total_pass + self.pass_num

    def rem_num(self):
        self.total_pass = [e for e in self.total_pass if e not in ('1', '2', '3', '4', '5', '6', '7', '8',
                                                                   '9')]

# ----------------------------------------------------------------------------------------------------------------------
    def sym_chk(self):
        if sym_chk.get() == 1:
            self.add_sym()
        else:
            self.rem_sym()

    def add_sym(self):
        self.total_pass = self.total_pass + self.pass_sym

    def rem_sym(self):
        self.total_pass = [e for e in self.total_pass if e not in ('!', '@', '#', '$', '%', '^', '&',
                                                                   '*', '(', ')')]

    # function to copy the password to the clipboard
    def copytoclipboard(self):
        random_password = passstr.get()
        pyperclip.copy(random_password)


pass_gen = Generator()
pass_gen.initialize()

Label(root, text="Password Generator and Storage Application", font="calibri 20 bold").pack()

Label(root, text="Enter password length").pack(pady=3)

Entry(root, textvariable=passlen).pack(pady=3)
pass_gen.pass_len = passlen
upper_chk = IntVar()
num_chk = IntVar()
sym_chk = IntVar()
Checkbutton(root, text="Include UpperCase?", onvalue=1, offvalue=0, variable=upper_chk,
            command=pass_gen.upper_chk).pack(pady=3)
Checkbutton(root, text="Include Numbers?", onvalue=1, offvalue=0, variable=num_chk,
            command=pass_gen.num_chk).pack(pady=3)
Checkbutton(root, text="Include Symbols?", onvalue=1, offvalue=0, variable=sym_chk,
            command=pass_gen.sym_chk).pack(pady=3)

Button(root, text="Generate Password", command=pass_gen.generate).pack(pady=7)

Entry(root, textvariable=passstr).pack(pady=3)

# add the following below:  ', command=pass_gen.write_pw'
Button(root, text="Copy to clipboard", command=pass_gen.copytoclipboard).pack()
# ----------------------------------------------------------------------------------------------------------------------
root.mainloop()
