from tkinter import Tk, Canvas, Label, Entry, Button, END
from PIL import ImageTk, Image
from tkinter import messagebox
import pyautogui
import string
from random import *
import pyperclip
import string
import json
import csv
import random
import pandas as pd

def generate_password():
    length = 15
    characters = string.ascii_letters
    numbers = string.digits
    symbols = '!@#$%^&*()_+'
    
    num_characters = length - random.randint(4, 6)
    num_numbers = random.randint(1, 3)
    num_symbols = length - num_characters - num_numbers

    password = ''.join(random.choice(characters) for _ in range(num_characters))
    password += ''.join(random.choice(numbers) for _ in range(num_numbers))
    password += ''.join(random.choice(symbols) for _ in range(num_symbols))
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    pas_e.delete(0, END)
    pas_e.insert(END, password)
    pas_e.clipboard_append(pas_e.get())
    pyperclip.copy(password)


def add_entry():
    website = w_e.get()
    email = em_e.get()
    password = pas_e.get()
    
    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        data = [
            ['Website','Username','Password'],
            [website,email,password]
        ]
        
        with open('\Password_Manager\Data.csv', mode='a', newline='') as file: # Update the file path according to the location of the CSV file.
            writer = csv.writer(file)
            writer.writerows(data)
        
        w_e.delete(0, END)
        em_e.delete(0,END)
        pas_e.delete(0, END)
        messagebox.showinfo(title='Password Manager', message="Successfully Saved")
    else:
        messagebox.showwarning(title="Oops", message="Don't leave any field empty!")


def find():
    website = w_e.get()
    
    if len(website) == 0:
        messagebox.showerror(title='Oops', message='Please fill the Website to find the Username and Password!')
        return
    
    try:
        with open('D:\Cybersecurity\Internships\LearnSmasher Projects\Password_Manager\Data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row['Website'] == website:
                    messagebox.showinfo(title=website, message=f'Username: {row["Username"]}\nPassword: {row["Password"]}')
                    return
            
            # If no matching record is found
            messagebox.showerror(title='Oops', message='Data not found!')
            
    except FileNotFoundError:
        messagebox.showerror(title='Oops', message='Data file not found!')

passw = ''    # Here you can have any password for your password manager
password = pyautogui.password('Enter your password: ',title = 'Password Manager Authentication')
if password == passw:
    w = Tk()
    w.title('Password Manager')
    w.config(pady=70, padx=70)

    fo = ('Merriweather', 14, 'normal')

    canv = Canvas(width=300, height=200)
    canv.grid(column=2, row=1)

    # Open the image file
    image = Image.open("Logo.png") # This needs to be updated according to the image file which will be used as a logo.
    # Resize the image if desired
    # image = image.resize((400, 100))
    # Create a Tkinter-compatible image object
    tk_image = ImageTk.PhotoImage(image)

    # Display the image on the canvas
    canv.create_image(100, 100, image=tk_image)

    web = Label(text='Website   :', font=fo)
    web.grid(column=1, row=2, sticky='e', padx=7)
    w_e = Entry(width=39, font=fo)
    w_e.grid(row=2, column=2, columnspan=2, pady=7)
    w_e.focus()

    em = Label(text='Email/Username   :', font=fo)
    em.grid(column=1, row=3, padx=7)
    em_e = Entry(width=39, font=fo)
    em_e.grid(column=2, row=3, columnspan=2, pady=7)
    em_e.insert(0, 'example@mail.com')

    pas = Label(text='Password:    :', font=fo)
    pas.grid(column=1, row=4, sticky='e', padx=7, pady=7)
    pas_e = Entry(width=30, font=fo)
    pas_e.place(x=186, y=302)

    gen = Button(text="Generate One", command=generate_password, font=('Merriweather', 10, 'normal'))
    gen.place(x=530, y=300)

    add = Button(text='Add', width=42, command=add_entry, font=('Merriweather', 10, 'normal'))
    add.grid(column=2, row=5, columnspan=1, pady=7, padx=5)
    re = Button(text='Retrieve', width=10, command=find, font=('Merriweather', 10, 'normal'))
    re.grid(column=3, row=5)

    w.mainloop()
else:
    messagebox.showerror("Authentication Failed ", "Incorrect Password")
