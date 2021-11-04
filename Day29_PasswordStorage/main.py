from tkinter import *
import random
from tkinter import messagebox
import json

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# --- Password Generator ---
def password_generator():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_upper = [x.upper() for x in letter]

    letter.extend(letter_upper)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letter) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    # Change below line to try.
    # Now if hit the "Generate Password" multiple times, will get longer password
    p_entry.insert(0, password)

# --- Save Data to Files ---


def save_data():
    w = w_entry.get()
    e = e_entry.get()
    p = p_entry.get()
    new_data = {
        w: {
            "email": e,
            "password": p,
        }
    }

    if len(w) == 0 or len(p) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=w, message=f"These are the details entered: \nEmail: {e} "
                                       f"\nPassword: {p}\nIs it ok to save?")

        if is_ok:
            try:
                with open("password.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("password.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("password.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                w_entry.delete(0, END)
                p_entry.delete(0, END)


def find_password():
    web = w_entry.get()
    try:
        with open("password.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found.")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists.")



w_label = Label(text="Website:")
w_label.grid(row=1, column=0)

e_label = Label(text="Email/Username:")
e_label.grid(row=2, column=0)

p_label = Label(text="Password:")
p_label.grid(row=3, column=0)

w_entry = Entry(width=21)
w_entry.grid(row=1, column=1, columnspan=1)
w_entry.focus()

e_entry = Entry(width=39)
e_entry.grid(row=2, column=1, columnspan=2)
e_entry.insert(END, "gwwill0922@gmail.com")

p_entry = Entry(width=21)
p_entry.grid(row=3, column=1)

s_button = Button(text='Search', command=find_password, width=14)
s_button.grid(row=1, column=2)

p_button = Button(text='Generate Password', command=password_generator)
p_button.grid(row=3, column=2)

add_button = Button(text='Add', width=33, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
