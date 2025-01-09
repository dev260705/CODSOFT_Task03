import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        
        password_display.config(state='normal')
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state='readonly')
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")


app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")
app.configure(bg="#4B0082")  


title_label = tk.Label(
    app,
    text="Secure Password Generator",
    font=("Arial", 18, "bold"),
    bg="#4B0082",
    fg="white"
)
title_label.pack(pady=10)


input_frame = tk.Frame(app, bg="#4B0082")
input_frame.pack(pady=20)

length_label = tk.Label(
    input_frame,
    text="Password Length:",
    font=("Arial", 12),
    bg="#4B0082",
    fg="white"
)
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
length_entry.grid(row=0, column=1, padx=5, pady=5)


def on_hover(event):
    generate_button["bg"] = "#FF69B4"

def on_leave(event):
    generate_button["bg"] = "#1E90FF"

generate_button = tk.Button(
    app,
    text="Generate Password",
    font=("Arial", 14, "bold"),
    bg="#1E90FF",
    fg="white",
    activebackground="#FF69B4",
    activeforeground="white",
    command=generate_password
)
generate_button.pack(pady=10)

generate_button.bind("<Enter>", on_hover)
generate_button.bind("<Leave>", on_leave)


password_display = tk.Entry(app, font=("Arial", 14), justify="center", state="readonly")
password_display.pack(pady=20)


app.mainloop()
