from tkinter import *
# this only imports classes and constants, do not import like messagebox (other modulos)
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    p_entry.insert(0, password)
    # copy the text inside automatically
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = w_entry.get()
    email = u_entry.get()
    password = p_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops...", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:  # on read mode
                # 1-read old data
                data = json.load(data_file)  # loaded up into a python dictionary
        except FileNotFoundError:
            with open("data.json", "w") as data_file:  # on write mode
                # 3-saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # 2-updating old data with new data
            data.update(new_data)  # update dictionary
            with open("data.json", "w") as data_file:  # on write mode
                # 3-saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            w_entry.delete(0, END)
            p_entry.delete(0, END)


# ------------------------------- FIND PASSWORD -------------------------------------
def find_password():
    website = w_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops...", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\n Password: {data[website][
                "password"]}")
        else:
            messagebox.showinfo(title="Oops...", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", anchor="e", justify="right", width=12)
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", anchor="e", justify="right", width=12)
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", anchor="e", justify="right", width=12)
password_label.grid(column=0, row=3)

w_entry = Entry(width=21)
w_entry.grid(column=1, row=1)
w_entry.focus()

u_entry = Entry(width=37)
u_entry.grid(column=1, row=2, columnspan=2)
u_entry.insert(0, "elif@gmail.com")

p_entry = Entry(width=21)
p_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=12, command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
