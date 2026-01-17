import turtle
import random
import time
import winsound  # for Windows sounds, skip if on another OS

# ------------------ Screen Setup ------------------
screen = turtle.Screen()
screen.title("🌸 Kawaii Natural Numbers Adventure 🌸")
screen.bgcolor("#ffe6f0")
screen.setup(width=800, height=600)

# ------------------ Main Turtles ------------------
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

num_turtle = turtle.Turtle()
num_turtle.hideturtle()
num_turtle.penup()
num_turtle.color("#ff69b4")

msg = turtle.Turtle()
msg.hideturtle()
msg.penup()

heart_turtle = turtle.Turtle()
heart_turtle.hideturtle()
heart_turtle.penup()

cloud_turtle = turtle.Turtle()
cloud_turtle.hideturtle()
cloud_turtle.penup()
cloud_turtle.color("#ffffff")

# ------------------ Variables ------------------
score = 0
current_number = 1
level = 1

# ------------------ Animations ------------------
def pop_animation():
    for size in range(20, 41, 4):
        num_turtle.clear()
        num_turtle.write(current_number, align="center",
                         font=("Comic Sans MS", size, "bold"))
        time.sleep(0.05)

def happy_animation():
    msg.clear()
    msg.color("#ff1493")
    msg.goto(0, -200)
    msg.write("🎉 YAY! SO CUTE! 🎉",
              align="center", font=("Comic Sans MS", 24, "bold"))
    # Play sound (Windows only)
    try:
        winsound.Beep(800, 150)
    except:
        pass
    float_hearts()
    time.sleep(1)
    msg.clear()

def sad_animation():
    msg.clear()
    msg.color("#ff69b4")
    msg.goto(0, -200)
    msg.write("😿 Oops! Try again 💔",
              align="center", font=("Comic Sans MS", 22, "bold"))
    try:
        winsound.Beep(400, 200)
    except:
        pass
    time.sleep(1)
    msg.clear()

def float_hearts():
    heart_turtle.clear()
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        heart_turtle.goto(x, y)
        heart_turtle.write("💖", align="center", font=("Arial", 24, "bold"))
        time.sleep(0.1)
    heart_turtle.clear()

def moving_clouds():
    cloud_turtle.clear()
    for _ in range(5):
        x = random.randint(-400, 400)
        y = random.randint(100, 250)
        cloud_turtle.goto(x, y)
        cloud_turtle.write("☁️", align="center", font=("Arial", 36, "bold"))
    screen.update()

# ------------------ Levels ------------------
def level_up():
    global level
    level += 1
    msg.clear()
    msg.goto(0, -250)
    msg.color("#ff69b4")
    msg.write(f"🌟 Level {level}! 🌟", align="center", font=("Comic Sans MS", 28, "bold"))
    time.sleep(1)
    msg.clear()

# ------------------ Game Loop ------------------
while True:
    moving_clouds()
    num_turtle.goto(0, 0)
    pop_animation()
    
    answer = screen.textinput(
        "🌼 Kawaii Question 🌼",
        f"What comes after {current_number - 1}? (Level {level})")

    if answer is None:
        break

    if answer.isdigit() and int(answer) == current_number:
        happy_animation()
        current_number += 1
        score += 1
        if score % 5 == 0:  # every 5 correct answers → level up
            level_up()
    else:
        sad_animation()

# ------------------ Game Over ------------------
pen.goto(0, 0)
pen.color("#ff1493")
pen.write(f"🌈 Game Over!\nYour Score: {score}\nLevel Reached: {level}",
          align="center", font=("Comic Sans MS", 28, "bold"))

screen.mainloop()
