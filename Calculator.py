import tkinter
import math  # Import math module for square root

master = tkinter.Tk()
master.title("Calculator")
master.geometry("300x300")  # Initial window size

# Create a styled text box
text_box = tkinter.Entry(
    master,
    justify="right",
    font=("Arial", 16),
    state="readonly",
    takefocus=0,
    bg="black",  # Background color for visibility
    fg="white",      # Text color
    highlightthickness=2,  # Thickness of border
    highlightbackground="black",  # Border color
    highlightcolor="blue"  # Border color when focused
)
text_box.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Function to update text box safely
def update_text_box(value):
    text_box.config(state="normal")  # Temporarily enable editing
    text_box.delete(0, tkinter.END)
    text_box.insert(0, value)
    text_box.config(state="readonly")  # Make it readonly again

def button_click(value):
    current_text = text_box.get()
    update_text_box(current_text + value)

def clear_text(event=None):  
    update_text_box("")

def calculate_result(event=None):  
    try:
        result = eval(text_box.get())
        update_text_box(str(result))
    except Exception:
        update_text_box("Error")

def calculate_square_root():
    try:
        current_text = text_box.get()
        result = math.sqrt(float(current_text))  # Calculate square root
        update_text_box(str(result))
    except Exception:
        update_text_box("Error")

def toggle_sign():
    try:
        current_text = text_box.get()
        if current_text:
            result = float(current_text) * -1  # Toggle the sign
            update_text_box(str(result))
    except Exception:
        update_text_box("Error")

def calculate_percentage():
    try:
        current_text = text_box.get()
        if current_text:
            result = float(current_text) / 100  # Calculate percentage
            update_text_box(str(result))
    except Exception:
        update_text_box("Error")

def key_pressed(event):
    if event.char and (event.char.isdigit() or event.char in "+-*/."):
        button_click(event.char)
    elif event.keysym == "BackSpace":
        current_text = text_box.get()
        update_text_box(current_text[:-1])  

master.bind("<Key>", key_pressed)
master.bind("<Return>", calculate_result)  
master.bind("<Escape>", clear_text)   
master.bind("<c>", clear_text)     

# List of buttons with their labels and grid positions
buttons = [
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("/", 2, 3),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("*", 3, 3),
    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("-", 4, 3),
    ("0", 5, 0),
    (".", 5, 1),
    ("=", 5, 2),
    ("+", 5, 3),
    ("C", 1, 0),
    ("√", 1, 1),
    ("+/-", 1, 2),
    ("%", 1, 3)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        tkinter.Button(master, text=text, command=calculate_result).grid(row=row, column=col, sticky="nsew")
    elif text == "C":
        tkinter.Button(master, text=text, command=clear_text).grid(row=row, column=col, sticky="nsew")
    elif text == "√":
        tkinter.Button(master, text=text, command=calculate_square_root).grid(row=row, column=col, sticky="nsew")
    elif text == "+/-":
        tkinter.Button(master, text=text, command=toggle_sign).grid(row=row, column=col, sticky="nsew")
    elif text == "%":
        tkinter.Button(master, text=text, command=calculate_percentage).grid(row=row, column=col, sticky="nsew")
    else:
        tkinter.Button(master, text=text, command=lambda t=text: button_click(t)).grid(row=row, column=col, sticky="nsew")

# Configure rows and columns for resizing
for i in range(6):  # Total rows (0 to 5)
    master.grid_rowconfigure(i, weight=1)
for i in range(4):  # Total columns (0 to 3)
    master.grid_columnconfigure(i, weight=1)

master.mainloop()
