import tkinter as tk
import random
import string

def generate_password():
    user_name = name_entry.get()
    password_length = int(length_entry.get())
    
    if password_length < len(user_name) + 1:
        result_label.config(text="Password length must be greater than name length + 1")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = user_name + ''.join(random.choice(characters) for _ in range(password_length - len(user_name)))
    password_display.config(text=password)


root = tk.Tk()
root.title("Password Generator")


name_label = tk.Label(root, text="Your Name:", background="lavender")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()


length_label = tk.Label(root, text="Password Length:",background="lavender")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()


generate_button = tk.Button(root, text="Generate Password",background="lavender", command=generate_password)
generate_button.pack()


password_display = tk.Label(root, text="", wraplength=300)
password_display.pack()


result_label = tk.Label(root, text="", fg="red")
result_label.pack()


root.mainloop()