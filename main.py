from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", font=("Arial", 12, "normal"))
label_website.grid(column=0, row=1)

input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)

label_email = Label(text="Email/Username:", font=("Arial", 12, "normal"))
label_email.grid(column=0, row=2)

input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)

label_pwd = Label(text="Password:", font=("Arial", 12, "normal"))
label_pwd.grid(column=0, row=3)

input_pwd = Entry(width=21)
input_pwd.grid(column=1, row=3)

btn_pwd = Button(text="Generate Password",font=("Arial", 12, "normal"))
btn_pwd.grid(column=2, row=3)

btn_add = Button(text="Add Password",font=("Arial", 12, "normal"),width=36)
btn_add.grid(column=1, row=4, columnspan=2)



window.mainloop()