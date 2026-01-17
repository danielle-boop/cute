import turtle
import time
import math
import random

# =======================
# Screen setup
# =======================
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Mini Movie: Multiplication + Power Series 🎬✨")
screen.setup(width=1200, height=800)

# =======================
# Turtle for text
# =======================
text = turtle.Turtle()
text.hideturtle()
text.penup()

# =======================
# Utility Functions
# =======================
def show_text(message, x, y, color="black", size=18, wait=2):
    text.goto(x, y)
    text.color(color)
    text.write(message, align="center", font=("Arial", size, "bold"))
    time.sleep(wait)
    text.clear()

def bounce_number(num, x, y):
    number = turtle.Turtle()
    number.hideturtle()
    number.penup()
    number.color(random.choice(["purple", "pink", "orange", "green", "red"]))
    for _ in range(6):
        number.goto(x, y + 10)
        number.write(num, align="center", font=("Arial", 20, "bold"))
        time.sleep(0.2)
        number.clear()
        y += 2
    number.goto(x, y)
    number.write(num, align="center", font=("Arial", 20, "bold"))

def draw_circle(radius, color="yellow"):
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.penup()
    circle.goto(0, -radius)
    circle.pendown()
    circle.color(color)
    circle.pensize(3)
    circle.circle(radius)
    time.sleep(2)
    circle.clear()

# =======================
# Scene 1: Welcome
# =======================
show_text("🎬 Welcome! Learn Multiplication & Power Series!", 0, 300, "red", 24)
show_text("Let's make learning fun and cute! ✨", 0, 250, "blue", 20)

# =======================
# Scene 2: Multiplication Basics
# =======================
show_text("Multiplication = Repeated Addition!", 0, 200, "green", 22)
numbers = ["2", "2", "2"]
x_pos = -50
for n in numbers:
    bounce_number(n, x_pos, 150)
    x_pos += 50
show_text("3 × 2 = 2 + 2 + 2 = 6 ✅", 0, 100, "purple", 20)

# =======================
# Scene 3: Multiplication Powers
# =======================
show_text("Multiplication Powers", 0, 50, "orange", 20)
show_text("2 x 4 = 8, 6 x 4  = 24", 0, 0, "pink", 18)
powers = ["x", "x", "x"]
x_pos = -200
for p in powers:
    bounce_number(5, x, 4)
    x_pos += 200

# =======================
# Scene 4: Power Series Introduction
# =======================
show_text("Power Series General Form", 0, -120, "purple", 22)
series_numbers = ["5", "x", "4567", "=", "22835"]
x_pos = -180
for n in series_numbers:
    bounce_number(n, x_pos, -220)
    x_pos += 90

# =======================
# Scene 5: Examples
# =======================
# Exponential Series
show_text("Example: 67 x 5 = 335", 0, -280, "blue", 18)
exp_numbers = ["1", "x", "2", "= 2",]
x_pos = -200
for n in exp_numbers:
    x_pos += 90

# Sine Series
show_text("Example: sin(x) = x - x³/3! + x⁵/5! - ...", 0, -380, "pink", 18)
sine_numbers = ["x", "- x³/3!", "x⁵/5!", "- x⁷/7!", "..."]
x_pos = -200
for n in sine_numbers:
    bounce_number(n, x_pos, -420)
    x_pos += 90

# =======================
# Scene 6: Applications
# =======================
show_text("Applications 💻🔧", 0, -480, "orange", 22)
apps = ["Calculator", "Science", "Engineering", "Algorithms"]
x_pos = -300
for app in apps:
    x_pos += 200

# =======================
# Scene 7: Python Simulation of e^x
# =======================
show_text("Python Simulation of e^x 🐍", 0, -580, "red", 20)

def power_series_exp(x, terms=6):
    total = 0
    for n in range(terms):
        term = (x**n)/math.factorial(n)
        # Animate multiplication inside term
        show_text(f"{x}^{n}/{n}! = {round(term,4)}", 0, -620, "purple", 18, wait=0.5)
        total += term
    return total

x_val = 1
result = power_series_exp(x_val)
show_text(f"e^{x_val} ≈ {round(result,5)}", 0, -660, "green", 20)

# =======================
# Scene 8: Fun & Conclusion
# =======================
show_text("✨ Multiplication + Power Series is Fun! ✨", 0, -700, "red", 24, wait=3)
show_text("🎉 Thank you for watching! 🎉", 0, -740, "blue", 22, wait=3)

turtle.done()
