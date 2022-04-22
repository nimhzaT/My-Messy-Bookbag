import tkinter as tk
import cgitb

def counter_label(label, limit, rate=1):
    """Update counter display on label at given rate until it reaches limit."""
    counter = 0
    def count():
        nonlocal counter
        counter += rate
        label.config(text=str(counter))
        if counter < limit:
            label.after(1, count)
    count()  # Start counting.

root = tk.Tk()
root.title("Headquarters Count Recycled")
label= tk.Label(root, fg="dark green")
label.pack()
counter_label(label, 8454)
button = tk.Button(root, text="stop", width=40, command=root.destroy)
button.pack()
root.mainloop()
