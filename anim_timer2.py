import tkinter as tk
import threading as th
 
class Main:
    def __init__(self, root):
        self.counter = 0
        self.after_id = None
        self.frame = tk.Frame(root)
        self.label = tk.Label(self.frame, text="0")
        self.label.pack()
 
        btn_start = tk.Button(self.frame, text="Check",
                              command=self.on_btn_start)
        btn_start.pack()
        btn_stop = tk.Button(self.frame, text="Stop",
                             command=self.on_btn_stop)
        btn_stop.pack()
        btn_reset = tk.Button(self.frame, text="Reset",
                              command=self.on_btn_reset)
        btn_reset.pack()
        self.frame.pack()
 
    def on_btn_start(self):
        if not self.after_id:
            self.increase_counter()
 
    def on_btn_stop(self):
        if self.after_id:
            self.frame.after_cancel(self.after_id)
            self.after_id = None
 
    def on_btn_reset(self):
        self.on_btn_stop()
        self.counter = 0
        self.display_counter()
 
    def increase_counter(self):
        self.counter += 30
        self.display_counter()
        self.after_id = self.frame.after(1, self.increase_counter)
        
    def display_counter(self):
        self.label['text'] = self.counter

 
 
root = tk.Tk()
main = Main(root)
