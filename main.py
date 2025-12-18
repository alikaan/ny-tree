import tkinter as tk
import random
import base64
from io import BytesIO
import platform

root = tk.Tk()

# ---- SET ICON ----
# Create a simple Christmas tree icon
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

# Size scale factor
scale_factor = 0.8
BASE_WIDTH, BASE_HEIGHT = 220, 320

def update_size():
    global scale_factor
    WIDTH = int(BASE_WIDTH * scale_factor)
    HEIGHT = int(BASE_HEIGHT * scale_factor)
    canvas.config(width=WIDTH, height=HEIGHT)
    redraw_tree()

def redraw_tree():
    global star, lights, snowflakes, scale_factor
    
    WIDTH = int(BASE_WIDTH * scale_factor)
    HEIGHT = int(BASE_HEIGHT * scale_factor)
    CENTER_X = WIDTH // 2
    
    # Clear canvas
    canvas.delete("all")
    
    # ---- STAR ----
    star = canvas.create_polygon(
        CENTER_X, int(20 * scale_factor),
        CENTER_X + int(6 * scale_factor), int(35 * scale_factor),
        CENTER_X + int(22 * scale_factor), int(35 * scale_factor),
        CENTER_X + int(10 * scale_factor), int(45 * scale_factor),
        CENTER_X + int(15 * scale_factor), int(60 * scale_factor),
        CENTER_X, int(50 * scale_factor),
        CENTER_X - int(15 * scale_factor), int(60 * scale_factor),
        CENTER_X - int(10 * scale_factor), int(45 * scale_factor),
        CENTER_X - int(22 * scale_factor), int(35 * scale_factor),
        CENTER_X - int(6 * scale_factor), int(35 * scale_factor),
        fill="gold", outline=""
    )
    
    # ---- TREE ----
    canvas.create_polygon(
        CENTER_X, int(50 * scale_factor),
        int(55 * scale_factor), int(150 * scale_factor),
        int(85 * scale_factor), int(150 * scale_factor),
        int(35 * scale_factor), int(270 * scale_factor),
        WIDTH - int(35 * scale_factor), int(270 * scale_factor),
        WIDTH - int(85 * scale_factor), int(150 * scale_factor),
        WIDTH - int(55 * scale_factor), int(150 * scale_factor),
        fill="#0b6623", outline=""
    )
    
    # ---- TRUNK ----
    canvas.create_rectangle(
        CENTER_X - int(15 * scale_factor), int(270 * scale_factor),
        CENTER_X + int(15 * scale_factor), int(300 * scale_factor),
        fill="#6f4e37", outline=""
    )
    
    # ---- ORNAMENTS ----
    ornament_colors = ["red", "gold", "blue", "pink", "silver", "purple"]
    
    ornament_positions = [
        (CENTER_X - int(15 * scale_factor), int(95 * scale_factor)),
        (CENTER_X + int(15 * scale_factor), int(95 * scale_factor)),
        (CENTER_X, int(110 * scale_factor)),
        (CENTER_X - int(25 * scale_factor), int(125 * scale_factor)),
        (CENTER_X + int(25 * scale_factor), int(125 * scale_factor)),
        (CENTER_X - int(35 * scale_factor), int(145 * scale_factor)),
        (CENTER_X + int(35 * scale_factor), int(145 * scale_factor)),
        (CENTER_X - int(20 * scale_factor), int(160 * scale_factor)),
        (CENTER_X + int(20 * scale_factor), int(160 * scale_factor)),
        (CENTER_X - int(45 * scale_factor), int(180 * scale_factor)),
        (CENTER_X + int(45 * scale_factor), int(180 * scale_factor)),
        (CENTER_X - int(30 * scale_factor), int(200 * scale_factor)),
        (CENTER_X + int(30 * scale_factor), int(200 * scale_factor)),
        (CENTER_X - int(50 * scale_factor), int(220 * scale_factor)),
        (CENTER_X + int(50 * scale_factor), int(220 * scale_factor)),
        (CENTER_X - int(25 * scale_factor), int(240 * scale_factor)),
        (CENTER_X + int(25 * scale_factor), int(240 * scale_factor)),
        (CENTER_X - int(40 * scale_factor), int(255 * scale_factor)),
        (CENTER_X + int(40 * scale_factor), int(255 * scale_factor))
    ]
    
    for x, y in ornament_positions:
        color = random.choice(ornament_colors)
        ornament_size = int(5 * scale_factor)
        
        canvas.create_oval(
            x - ornament_size, y - ornament_size, 
            x + ornament_size, y + ornament_size,
            fill=color, outline="", width=0
        )
        
        shine_size = int(3 * scale_factor)
        canvas.create_oval(
            x - shine_size, y - shine_size, 
            x - int(1 * scale_factor), y - int(1 * scale_factor),
            fill="white", outline="", stipple="gray50"
        )
        
        canvas.create_rectangle(
            x - int(1.5 * scale_factor), y - int(7 * scale_factor), 
            x + int(1.5 * scale_factor), y - int(5 * scale_factor),
            fill="#C0C0C0", outline=""
        )
    
    # ---- STAR ORNAMENTS ----
    star_positions = [
        (CENTER_X - int(10 * scale_factor), int(130 * scale_factor)),
        (CENTER_X + int(10 * scale_factor), int(175 * scale_factor)),
        (CENTER_X, int(210 * scale_factor))
    ]
    
    for x, y in star_positions:
        s = scale_factor
        canvas.create_polygon(
            x, y - int(3 * s),
            x + int(1 * s), y - int(1 * s),
            x + int(3 * s), y - int(1 * s),
            x + int(1.5 * s), y + int(0.5 * s),
            x + int(2 * s), y + int(3 * s),
            x, y + int(1.5 * s),
            x - int(2 * s), y + int(3 * s),
            x - int(1.5 * s), y + int(0.5 * s),
            x - int(3 * s), y - int(1 * s),
            x - int(1 * s), y - int(1 * s),
            fill=random.choice(["gold", "silver"]),
            outline="white", width=1
        )
    
    # ---- LIGHTS ----
    lights = []
    light_positions = [
        (CENTER_X, int(100 * scale_factor)), 
        (CENTER_X - int(40 * scale_factor), int(160 * scale_factor)), 
        (CENTER_X + int(40 * scale_factor), int(160 * scale_factor))
    ]
    for x, y in light_positions:
        light_size = int(3 * scale_factor)
        lights.append(
            canvas.create_oval(
                x - light_size, y - light_size, 
                x + light_size, y + light_size, 
                fill="yellow", outline=""
            )
        )
    
    # ---- TEXT ----
    if platform.system() == "Darwin":
        font_size = int(21 * scale_factor)
        text_font = ("Bradley Hand", font_size, "bold")
    else:
        font_size = int(21 * scale_factor)
        text_font = ("Segoe Script", font_size, "bold")
    
    canvas.create_text(
        CENTER_X, int(230 * scale_factor),
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
        size = int(random.randint(1, 3) * scale_factor)
        snowflakes.append(
            canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")
        )

WIDTH, HEIGHT = BASE_WIDTH, BASE_HEIGHT
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=canvas_bg, highlightthickness=0)
canvas.pack()

CENTER_X = WIDTH // 2

# Initial draw
star = None
lights = []
snowflakes = []
redraw_tree()

# Position window at bottom-left corner of screen
root.update_idletasks()  # Update to get accurate window size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_height = root.winfo_height()

# Position: x=0 (left), y=screen_height - window_height (bottom)
root.geometry(f"+0+{screen_height - window_height}")

star_glow = True
def glow_star():
    global star_glow
    if star:
        canvas.itemconfig(
            star,
            fill="gold" if star_glow else "#fff1a8"
        )
        star_glow = not star_glow
    root.after(600, glow_star)

glow_star()

def blink_lights():
    for light in lights:
        canvas.itemconfig(
            light,
            fill=random.choice(["yellow", "orange", "white"])
        )
    root.after(450, blink_lights)

blink_lights()

def snowfall():
    HEIGHT = int(BASE_HEIGHT * scale_factor)
    WIDTH = int(BASE_WIDTH * scale_factor)
    for flake in snowflakes:
        canvas.move(flake, 0, random.randint(1, 3))
        coords = canvas.coords(flake)
        if coords and coords[1] > HEIGHT:
            x = random.randint(0, WIDTH)
            size = int(2 * scale_factor)
            canvas.coords(flake, x, 0, x + size, size)
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

# ---- SIZE CONTROLS ----
def increase_size():
    global scale_factor
    if scale_factor < 2.0:  # Maximum 200%
        scale_factor += 0.1
        update_size()

def decrease_size():
    global scale_factor
    if scale_factor > 0.5:  # Minimum 50%
        scale_factor -= 0.1
        update_size()

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
    menu.add_command(label="Increase Size", command=increase_size)
    menu.add_command(label="Decrease Size", command=decrease_size)
    
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