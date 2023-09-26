from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
root = Tk()
root.title("Password manager")
root.config(padx=50, pady=50)
img = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)
web_label = Label(root, text="Website:", font=("Times New Roman", 15, "bold"))
web_label.grid(column=0, row=1)
web_entry = Entry(root,width=30)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
uname_label = Label(root, text="Email/Username:", font=("Times New Roman", 15, "bold"))
uname_label.grid(column=0, row=2)
uname_entry = Entry(root,width=45)
uname_entry.grid(column=1, row=2, columnspan=2)
uname_entry.insert(0, "achintyashah25@gmail.com")
pass_label = Label(root, text="Password:", font=("Times New Roman", 15, "bold"))
pass_label.grid(column=0, row=3)
pass_entry = Entry(root,width=30)
pass_entry.grid(column=1, row=3)


def new_pass():
    password = pass_entry.get()
    website = web_entry.get()
    username = uname_entry.get()
    new_dict = { website:{"email":username,"password":password}}
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror(title="Error", message="MessageBox Empty")
    else:
        affirmation = messagebox.askokcancel(title=website,message=f"Are you sure the data you entered is correct\n"
                                                                   f"Username:{username}\nWebsite:{website}"
                                                                   f"\nPassword:{password}")
        if affirmation:
            try:
                with open("password.json",mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("password.json",mode="w") as file:
                    json.dump(new_dict, file, indent=4)
            else:
                data.update(new_dict)
                with open("password.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0,END)
                pass_entry.delete(0,END)


def generation():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    final_pass = password_letters + password_number + password_symbol
    random.shuffle(final_pass)
    p = "".join(final_pass)
    pass_entry.insert(0, p)
    pyperclip.copy(p)


def searcher():
    website = web_entry.get()
    try:
        with open("password.json",mode="r") as file:
            reader = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error 404",message="File not found")
    else:
        if website in reader:
            web = reader[website]
            mail_id = web["email"]
            display_pass = web["password"]
            messagebox.showinfo(title=website,message=f"Email: {mail_id}\nPassword: {display_pass}")
        else:
            messagebox.showerror(title="Error 404",message="File not found")
    finally:
        web_entry.delete(0, END)


generate = Button(root, text="Generate",command=generation, width=10)
generate.grid(row=3,column=3)
add = Button(root, text="Add",command=new_pass, width=18)
add.grid(row=4, column=1, columnspan=2)
search = Button(root, text="Search",width=10,command=searcher)
search.grid(row=1, column=3)
root.mainloop()
