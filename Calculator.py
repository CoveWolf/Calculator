import tkinter
import math  # Import math module for square root

master = tkinter.Tk()
master.title("Calculator")
master.geometry("300x300")  # Initial window size

# Textbox for displaying input and results
text_box = tkinter.Entry(master, justify="right", font=("Arial", 16), takefocus=0)
text_box.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Variables to store the last operation and operand
last_operation = None
last_operand = None

def button_click(value):
    current_text = text_box.get()
    text_box.delete(0, tkinter.END)
    text_box.insert(0, current_text + value)

def clear_text(event=None):  
    global last_operation, last_operand
    text_box.delete(0, tkinter.END)
    last_operation = None
    last_operand = None

def calculate_result(event=None):  
    global last_operation, last_operand
    try:
        current_text = text_box.get()
        if last_operation and last_operand is not None and current_text:
            # Perform repeated calculation
            current_text += f"{last_operation}{last_operand}"
        result = eval(current_text)
        text_box.delete(0, tkinter.END)
        text_box.insert(0, str(result))
        # Store last operation and operand
        if current_text and any(op in current_text for op in "+-*/"):
            for op in "+-*/":
                if op in current_text:
                    last_operation = op
                    last_operand = current_text.split(op)[-1]
                    break
    except Exception:
        text_box.delete(0, tkinter.END)
        text_box.insert(0, "Error")

def calculate_square_root():
    try:
        current_text = text_box.get()
        result = math.sqrt(float(current_text))  # Calculate square root
        text_box.delete(0, tkinter.END)
        text_box.insert(0, str(result))
    except Exception:
        text_box.delete(0, tkinter.END)
        text_box.insert(0, "Error")

def toggle_sign():
    try:
        current_text = text_box.get()
        if current_text:
            result = float(current_text) * -1  # Toggle the sign
            text_box.delete(0, tkinter.END)
            text_box.insert(0, str(result))
    except Exception:
        text_box.delete(0, tkinter.END)
        text_box.insert(0, "Error")

def calculate_percentage():
    try:
        current_text = text_box.get()
        if current_text:
            result = float(current_text) / 100  # Calculate percentage
            text_box.delete(0, tkinter.END)
            text_box.insert(0, str(result))
    except Exception:
        text_box.delete(0, tkinter.END)
        text_box.insert(0, "Error")

def key_pressed(event):
    if event.char and (event.char.isdigit() or event.char in "+-*/."):
        button_click(event.char)
        return "break"  # Prevent the default behavior
    elif event.keysym == "BackSpace":
        current_text = text_box.get()
        text_box.delete(0, tkinter.END)
        text_box.insert(0, current_text[:-1])
        return "break"  # Prevent the default behavior

# Bind the keyboard input to the text box
master.bind("<Key>", key_pressed)
master.bind("<Return>", calculate_result)  
master.bind("<Escape>", clear_text)   
master.bind("<c>", clear_text)     

# List of buttons with their labels and grid positions
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

# Create buttons dynamically
# Create buttons dynamically with color settings
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
