import tkinter as tk
from tkinter import messagebox
import random

# ------------------ GAME STATE ------------------
money = 50
level = 1
achievements = []

facilities = {
    "Room Upgrade": {"level": 0, "cost": 10},
    "Dining Hall": {"level": 0, "cost": 15},
    "Tea Garden": {"level": 0, "cost": 20},
    "Panda Spa": {"level": 0, "cost": 25},
    "Souvenir Shop": {"level": 0, "cost": 30}
}

pandas = [{"x": 50, "y": 300, "dir": 1}, {"x": 400, "y": 350, "dir": -1}]

# ------------------ FUNCTIONS ------------------
def update_status():
    status_label.config(text=f"Money: ${money} | Level: {level}")
    for name, btn in facility_buttons.items():
        f = facilities[name]
        btn.config(text=f"{name}\nLevel {f['level']}\nCost: ${f['cost']}")

def ask_question():
    global money, level
    x = random.randint(1, level+5)
    y = random.randint(1, level+5)
    answer = tk.simpledialog.askinteger("🎯 Math Challenge", f"Solve: {x} × {y} = ?")
    if answer == x*y:
        messagebox.showinfo("Correct!", "✅ You got it right!")
        return x*y
    else:
        messagebox.showwarning("Wrong", f"❌ Wrong! The correct answer was {x*y}")
        return 0

def upgrade_facility(name):
    global money, level
    f = facilities[name]
    if money >= f['cost']:
        reward = ask_question()
        money += reward - f['cost']
        f['level'] += 1
        level += 1
        if f['level'] == 5:
            achievements.append(f"{name} Master!")
            messagebox.showinfo("Achievement!", f"You unlocked achievement: {name} Master!")
        update_status()
    else:
        messagebox.showwarning("Not enough money", "You cannot afford this upgrade!")

def work():
    global money, level
    reward = ask_question()
    money += reward
    level += 1
    update_status()

def random_event():
    global money
    events = ["A guest tipped you $10!", "A guest spilled tea! -$5", "Bonus panda appeared! +$20"]
    e = random.choice(events)
    messagebox.showinfo("Random Event", e)
    if "+$" in e:
        money += int(e.split("+$")[1])
    if "-$" in e:
        money -= int(e.split("-$")[1])
    update_status()

def move_pandas():
    for p in pandas:
        p["x"] += p["dir"] * 5
        if p["x"] < 0 or p["x"] > 550:
            p["dir"] *= -1
    draw_canvas()
    root.after(500, move_pandas)  # animation every 0.5s

def draw_canvas():
    canvas.delete("all")
    # Draw pandas
    for p in pandas:
        canvas.create_oval(p["x"], p["y"], p["x"]+30, p["y"]+30, fill="black")
        canvas.create_oval(p["x"]+5, p["y"]+5, p["x"]+10, p["y"]+10, fill="white")
        canvas.create_oval(p["x"]+15, p["y"]+5, p["x"]+20, p["y"]+10, fill="white")
    # Draw facilities
    for i, (name, f) in enumerate(facilities.items()):
        canvas.create_rectangle(50+i*110, 50, 130+i*110, 130, fill="#ffcc99")
        canvas.create_text(90+i*110, 90, text=f"{name}\nL{f['level']}", font=("Comic Sans MS", 10))

# ------------------ GUI ------------------
root = tk.Tk()
root.title("🐼 Panda Resort Deluxe 🌴")
root.geometry("700x500")
root.configure(bg="#c8f7c5")

status_label = tk.Label(root, text="", font=("Comic Sans MS", 16), bg="#c8f7c5")
status_label.pack(pady=10)

canvas = tk.Canvas(root, width=600, height=300, bg="#a3d9a5")
canvas.pack(pady=10)

facility_frame = tk.Frame(root, bg="#c8f7c5")
facility_frame.pack(pady=5)

facility_buttons = {}
for i, name in enumerate(facilities.keys()):
    btn = tk.Button(facility_frame, text="", width=18, height=3,
                    command=lambda n=name: upgrade_facility(n), bg="#ffcc99", font=("Comic Sans MS", 12))
    btn.grid(row=i//2, column=i%2, padx=10, pady=10)
    facility_buttons[name] = btn

work_btn = tk.Button(root, text="Work to earn money", command=work, bg="#ffb6c1", font=("Comic Sans MS", 14))
work_btn.pack(pady=5)

event_btn = tk.Button(root, text="Random Event", command=random_event, bg="#87cefa", font=("Comic Sans MS", 14))
event_btn.pack(pady=5)

update_status()
draw_canvas()
move_pandas()  # start animation
root.mainloop()
