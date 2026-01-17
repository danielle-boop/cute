import tkinter as tk
import random

# Create window
root = tk.Tk()
root.title("Kawaii Calculator 💕")
root.geometry("320x460")
root.configure(bg="#ffe6f0")
root.resizable(False, False)

expression = ""

# Floating hearts function
def get_hearts():
    return "💖"*random.randint(1,3)

# Functions
def press(key):
    global expression
    expression += str(key)
    display.set(expression + " 😺 " + get_hearts())

def clear():
    global expression
    expression = ""
    display.set("😺 " + get_hearts())

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.set(result + " 😸 " + get_hearts())
        expression = result
    except:
        display.set("Error 😿")
        expression = ""

# Display
display = tk.StringVar()
display.set("😺 " + get_hearts())
entry = tk.Entry(
    root,
    textvariable=display,
    font=("Comic Sans MS", 20, "bold"),
    bd=0,
    justify="right",
    bg="#fff0f6",
    relief="ridge",
    highlightthickness=2,
    highlightbackground="#ffb6c1"
)
entry.pack(fill="both", padx=15, pady=15, ipady=12)

# Button style
btn_style = {
    "font": ("Comic Sans MS", 16, "bold"),
    "bg": "#ffb6c1",
    "fg": "white",
    "bd": 0,
    "width": 5,
    "height": 2,
    "activebackground": "#ff8fc1",
    "relief": "ridge",
    "overrelief": "groove",
    "highlightthickness": 0,
}

# Buttons
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("➗",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("✖",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("➖",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("➕",4,3)
]

frame = tk.Frame(root, bg="#ffe6f0")
frame.pack(pady=10)

for (text, r, c) in buttons:
    if text == "=":
        action = calculate
    else:
        action = lambda x=text: press(x.replace("➗","/").replace("✖","*").replace("➖","-").replace("➕","+"))
    btn = tk.Button(frame, text=text, command=action, **btn_style)
    btn.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")

# Make grid cells expand evenly
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

# Clear button
tk.Button(
    root,
    text="Clear 💖",
    command=clear,
    font=("Comic Sans MS", 16, "bold"),
    bg="#ff69b4",
    fg="white",
    bd=0,
    activebackground="#ff4f91",
    height=2
).pack(fill="x", padx=20, pady=10)

root.mainloop()

