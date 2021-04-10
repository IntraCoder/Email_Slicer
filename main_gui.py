from tkinter import *


def validity(domain, username):
    conditions = ("." in domain), (domain[0] != "."), (domain[-1] != "."), \
                 (username != ''), ("." not in username)

    if any(conditions):
        return True
    else:
        return False


def slicer(mail):
    domain = mail.split("@")[-1]
    ind = mail.find(domain)
    username = mail[:ind - 1]

    if validity(domain, username):
        domain_val.set(domain)
        username_val.set(username)
    else:
        username_val.set("Invalid Email")
        domain_val.set("Invalid Email")


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300")
    root.config(bg="navy blue")
    Label(root, text="Enter Email :", font=("Bahnschrift Semilight Condensed", 21),
          bg="navy blue", fg="#ffee58").place(x=50, y=50)
    Label(root, text="Domain :", font=("Bahnschrift Semilight Condensed", 21),
          bg="navy blue", fg="#ffee58").place(x=50, y=120)
    Label(root, text="Username :", font=("Bahnschrift Semilight Condensed", 21),
          bg="navy blue", fg="#ffee58").place(x=50, y=190)

    mail_val = StringVar()
    domain_val = StringVar()
    username_val = StringVar()
    Entry(root, textvariable=mail_val, font=("Bahnschrift Semilight Condensed", 18),
          bd=4).place(x=190, y=50)
    Entry(root, textvariable=domain_val, font=("Bahnschrift Semilight Condensed", 18),
          state="readonly", bd=4).place(x=190, y=120)
    Entry(root, textvariable=username_val, font=("Bahnschrift Semilight Condensed", 18),
          state="readonly", bd=4).place(x=190, y=190)

    Button(root, text="Slice Mail", font=("Bahnschrift Semilight Condensed", 19),
           bg="#ffee58", fg="navy blue",
           command=lambda: slicer(mail_val.get().strip())).place(x=200, y=240)

    root.mainloop()
    
