import tkinter
import math  

master = tkinter.Tk()
master.title("Calculator")
master.geometry("300x300")  

text_box = tkinter.Entry(master, justify="right", font=("Arial", 16), takefocus=0)
text_box.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

last_operation = None
last_operand = None

#Button register
def button_click(value):
    current_text = text_box.get()
    text_box.delete(0, tkinter.END)
    text_box.insert(0, current_text + value)

#Clear values
def clear_text(event=None):  
    global last_operation, last_operand
    text_box.delete(0, tkinter.END)
    last_operation = None
    last_operand = None

#Calculate result
def calculate_result(event=None):  
    global last_operation, last_operand
    try:
        current_text = text_box.get()
        result = eval(current_text)
        text_box.delete(0, tkinter.END)
        text_box.insert(0, str(result))
        
        last_operation = None
        last_operand = None
    except Exception:
        text_box.delete(0, tkinter.END)
        text_box.insert(0, "Error")

#Calculate square root
def calculate_square_root():
    try:
        current_text = text_box.get()
        result = math.sqrt(float(current_text))  
        text_box.delete(0, tkinter.END)
        text_box.insert(0, str(result))
    except Exception:
        text_box.delete(0, tkinter.END)
        text_box.insert(0, "Error")

#Toggle + or -
def toggle_sign():
    try:
        current_text = text_box.get()
        if current_text:
            result = float(current_text) * -1  
            text_box.delete(0, tkinter.END)
            text_box.insert(0, str(result))
    except Exception:
        text_box.delete(0, tkinter.END)
        text_box.insert(0, "Error")

#Calculate percentage
def calculate_percentage():
    try:
        current_text = text_box.get()
        if current_text:
            result = float(current_text) / 100  
            text_box.delete(0, tkinter.END)
            text_box.insert(0, str(result))
    except Exception:
        text_box.delete(0, tkinter.END)
        text_box.insert(0, "Error")

def key_pressed(event):
    if event.char and (event.char.isdigit() or event.char in "+-*/."):
        button_click(event.char)
        return "break"  
    elif event.keysym == "BackSpace":
        current_text = text_box.get()
        text_box.delete(0, tkinter.END)
        text_box.insert(0, current_text[:-1])
        return "break"  

master.bind("<Key>", key_pressed)
master.bind("<Return>", calculate_result)  
master.bind("<Escape>", clear_text)   
master.bind("<c>", clear_text)     

#Dictionary of buttons
buttons = [
    ("7", 2, 0, "white", "black"),
    ("8", 2, 1, "white", "black"),
    ("9", 2, 2, "white", "black"),
    ("/", 2, 3, "red", "white"),
    ("4", 3, 0, "white", "black"),
    ("5", 3, 1, "white", "black"),
    ("6", 3, 2, "white", "black"),
    ("*", 3, 3, "red", "white"),
    ("1", 4, 0, "white", "black"),
    ("2", 4, 1, "white", "black"),
    ("3", 4, 2, "white", "black"),
    ("-", 4, 3, "red", "white"),
    ("0", 5, 0, "white", "black"),
    (".", 5, 1, "white", "black"),
    ("=", 5, 2, "red", "white"),
    ("+", 5, 3, "red", "white"),
    ("C", 1, 0, "red", "white"),
    ("√", 1, 1, "red", "white"),
    ("+/-", 1, 2, "red", "white"),
    ("%", 1, 3, "red", "white")
]

#Color
for (text, row, col, bg_color, fg_color) in buttons:
    if text == "=":
        tkinter.Button(master, text=text, bg=bg_color, fg=fg_color, command=calculate_result).grid(row=row, column=col, sticky="nsew")
    elif text == "C":
        tkinter.Button(master, text=text, bg=bg_color, fg=fg_color, command=clear_text).grid(row=row, column=col, sticky="nsew")
    elif text == "√":
        tkinter.Button(master, text=text, bg=bg_color, fg=fg_color, command=calculate_square_root).grid(row=row, column=col, sticky="nsew")
    elif text == "+/-":
        tkinter.Button(master, text=text, bg=bg_color, fg=fg_color, command=toggle_sign).grid(row=row, column=col, sticky="nsew")
    elif text == "%":
        tkinter.Button(master, text=text, bg=bg_color, fg=fg_color, command=calculate_percentage).grid(row=row, column=col, sticky="nsew")
    else:
        tkinter.Button(master, text=text, bg=bg_color, fg=fg_color, command=lambda t=text: button_click(t)).grid(row=row, column=col, sticky="nsew")

# Configure rows and columns for resizing
for i in range(6):  # Total rows (0 to 5)
    master.grid_rowconfigure(i, weight=1)
for i in range(4):  # Total columns (0 to 3)
    master.grid_columnconfigure(i, weight=1)

master.mainloop()
