import tkinter as tk
import random
import base64
from io import BytesIO
import platform

root = tk.Tk()

# ---- SET ICON ----
try:
    # Create a small PhotoImage for the icon (32x32)
    icon = tk.PhotoImage(width=32, height=32)
    
    # Draw a simple tree shape with pixels
    # Green tree
    for y in range(8, 28):
        width = int((y - 8) * 0.6) + 1
        for x in range(16 - width, 16 + width):
            icon.put("#0b6623", (x, y))
    
    # Brown trunk
    for y in range(28, 32):
        for x in range(14, 18):
            icon.put("#6f4e37", (x, y))
    
    # Yellow star on top
    icon.put("#ffd700", (16, 6))
    icon.put("#ffd700", (15, 7))
    icon.put("#ffd700", (16, 7))
    icon.put("#ffd700", (17, 7))
    
    root.iconphoto(True, icon)
except Exception as e:
    print(f"Could not set icon: {e}")

root.overrideredirect(True)
root.attributes("-topmost", True)

# Platform-specific transparency handling
if platform.system() == "Darwin":  # macOS
    root.attributes("-transparent", True)
    root.config(bg='systemTransparent')
    canvas_bg = 'systemTransparent'
elif platform.system() == "Windows":
    root.attributes("-transparentcolor", "black")
    canvas_bg = "black"
else:  # Linux
    root.attributes("-transparentcolor", "black")
    canvas_bg = "black"

WIDTH, HEIGHT = 220, 320
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=canvas_bg, highlightthickness=0)
canvas.pack()

CENTER_X = WIDTH // 2

# ---- STAR ----
star = canvas.create_polygon(
    CENTER_X, 20,
    CENTER_X + 6, 35,
    CENTER_X + 22, 35,
    CENTER_X + 10, 45,
    CENTER_X + 15, 60,
    CENTER_X, 50,
    CENTER_X - 15, 60,
    CENTER_X - 10, 45,
    CENTER_X - 22, 35,
    CENTER_X - 6, 35,
    fill="gold", outline=""
)

star_glow = True
def glow_star():
    global star_glow
    canvas.itemconfig(
        star,
        fill="gold" if star_glow else "#fff1a8"
    )
    star_glow = not star_glow
    root.after(600, glow_star)

glow_star()

# ---- TREE ----
canvas.create_polygon(
    CENTER_X, 50,
    55, 150,
    85, 150,
    35, 270,
    WIDTH - 35, 270,
    WIDTH - 85, 150,
    WIDTH - 55, 150,
    fill="#0b6623", outline=""
)

# ---- TRUNK ----
canvas.create_rectangle(
    CENTER_X - 15, 270,
    CENTER_X + 15, 300,
    fill="#6f4e37", outline=""
)

# ---- ORNAMENTS ----
ornament_colors = ["red", "gold", "blue", "pink", "silver", "purple"]

# Better positioned ornaments that stay within tree boundaries
ornament_positions = [
    # Top section (narrow)
    (CENTER_X - 15, 95),
    (CENTER_X + 15, 95),
    (CENTER_X, 110),
    
    # Upper-middle section
    (CENTER_X - 25, 125),
    (CENTER_X + 25, 125),
    (CENTER_X - 35, 145),
    (CENTER_X + 35, 145),
    
    # Middle section
    (CENTER_X - 20, 160),
    (CENTER_X + 20, 160),
    (CENTER_X - 45, 180),
    (CENTER_X + 45, 180),
    
    # Lower-middle section
    (CENTER_X - 30, 200),
    (CENTER_X + 30, 200),
    (CENTER_X - 50, 220),
    (CENTER_X + 50, 220),
    
    # Bottom section (widest)
    (CENTER_X - 25, 240),
    (CENTER_X + 25, 240),
    (CENTER_X - 40, 255),
    (CENTER_X + 40, 255)
]

# Create ornaments with gradient effect
for x, y in ornament_positions:
    color = random.choice(ornament_colors)
    
    # Main ornament ball
    ornament = canvas.create_oval(
        x - 5, y - 5, x + 5, y + 5,
        fill=color,
        outline="",
        width=0
    )
    
    # Add shine/highlight effect (smaller white circle on top-left)
    shine = canvas.create_oval(
        x - 3, y - 3, x - 1, y - 1,
        fill="white",
        outline="",
        stipple="gray50"  # Semi-transparent effect
    )
    
    # Add ornament cap/hook at top
    cap = canvas.create_rectangle(
        x - 1.5, y - 7, x + 1.5, y - 5,
        fill="#C0C0C0",  # Silver color
        outline=""
    )

# Add some star-shaped ornaments inside the tree
star_positions = [
    (CENTER_X - 10, 130),
    (CENTER_X + 10, 175),
    (CENTER_X, 210)
]

for x, y in star_positions:
    # Create small star ornament
    star_ornament = canvas.create_polygon(
        x, y - 3,
        x + 1, y - 1,
        x + 3, y - 1,
        x + 1.5, y + 0.5,
        x + 2, y + 3,
        x, y + 1.5,
        x - 2, y + 3,
        x - 1.5, y + 0.5,
        x - 3, y - 1,
        x - 1, y - 1,
        fill=random.choice(["gold", "silver"]),
        outline="white",
        width=1
    )

# ---- LIGHTS ----
lights = []
for x, y in [(CENTER_X, 100), (CENTER_X - 40, 160), (CENTER_X + 40, 160)]:
    lights.append(
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="yellow", outline="")
    )

def blink_lights():
    for light in lights:
        canvas.itemconfig(
            light,
            fill=random.choice(["yellow", "orange", "white"])
        )
    root.after(450, blink_lights)

blink_lights()

# ---- TEXT ----

# Platform-specific font selection
if platform.system() == "Darwin":  # macOS
    text_font = ("Bradley Hand", 21, "bold")  # Or "Chalkboard SE", "Marker Felt"
else:  # Windows/Linux
    text_font = ("Segoe Script", 21, "bold")

canvas.create_text(
    CENTER_X, 230,
    text="Happy\nNew Year",
    fill="#ffd700",
    font=text_font,
    justify="center"
)

# ---- SNOW ----
snowflakes = []

for _ in range(30):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(1, 3)
    snowflakes.append(
        canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")
    )

def snowfall():
    for flake in snowflakes:
        canvas.move(flake, 0, random.randint(1, 3))
        if canvas.coords(flake)[1] > HEIGHT:
            x = random.randint(0, WIDTH)
            canvas.coords(flake, x, 0, x + 2, 2)
    root.after(50, snowfall)

snowfall()

# ---- DRAGGING ----
def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = root.winfo_x() + event.x - root.x
    y = root.winfo_y() + event.y - root.y
    root.geometry(f"+{x}+{y}")

canvas.bind("<Button-1>", start_move)
canvas.bind("<B1-Motion>", do_move)

# ---- RIGHT CLICK MENU ----
def toggle_topmost():
    current = root.attributes("-topmost")
    root.attributes("-topmost", not current)

def show_menu(event):
    menu = tk.Menu(root, tearoff=0)

    if root.attributes("-topmost"):
        menu.add_command(label="Disable Always on Top", command=toggle_topmost)
    else:
        menu.add_command(label="Enable Always on Top", command=toggle_topmost)
    
    menu.add_separator()
    menu.add_command(label="Close", command=root.destroy)
    menu.post(event.x_root, event.y_root)

# Bind for both macOS and other platforms
if platform.system() == "Darwin":  # macOS
    canvas.bind("<Button-2>", show_menu)  # Right-click on macOS
    canvas.bind("<Control-Button-1>", show_menu)  # Control+Click on macOS
else:
    canvas.bind("<Button-3>", show_menu)  # Right-click on Windows/Linux

root.mainloop()