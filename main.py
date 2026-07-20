""" You will write a Python app called my-profile-card.py using Tkinter. By the end, 
they have a working 400x380 desktop window with a purple title banner, two labelled 
entry boxes for Name and Hobby, a framed multi-line About Me text area, and a Show My Card button — 
all arranged neatly using the grid layout manager."""

import tkinter as tk

window = tk.Tk()
window.geometry("400x380")
window.title("My Profile Card")

l1 = tk.Label(window, text="Name")
l1.pack()

e1 = tk.Entry(window)
e1.pack()

l2 = tk.Label(window, text="Hobby")
l2.pack()

e2 = tk.Entry(window)
e2.pack()

l3 = tk.Label(window, text="About Me")
l3.pack()

t = tk.Text(window)
t.pack()

button = tk.Button(window, text="Show My Card")
button.pack()

window.mainloop()