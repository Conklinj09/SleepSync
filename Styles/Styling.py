import tkinter as tk
from tkinter import ttk
import random

# styling.py
BACKGROUND_COLOR = "#0D1B2A"   # Dark blue
TEXT_COLOR = "#F5F5F5"         # Soft white
GRAPH_LINE_COLOR = "#A288E3"   # Purple-violet



# Function to create twinkling stars effect
def create_stars(canvas, num_stars=100):
    for _ in range(num_stars):
        x = random.randint(0, 800)  # Width of the canvas
        y = random.randint(0, 600)  # Height of the canvas
        size = random.randint(1, 3)
        color = random.choice(["white", "yellow"])
        canvas.create_oval(x, y, x + size, y + size, fill=color, outline=color)

def submit_data():
    sleep_time = sleep_time_entry.get()
    wake_time = wake_time_entry.get()
    notes = notes_entry.get("1.0", tk.END).strip()

    # You can add the code to send data to Flask here

    # Display a confirmation message
    message_label.config(text="Data submitted successfully!")

# Tkinter setup (UI part)
root = tk.Tk()
root.title("SleepSync - Log Your Sleep")

# Create a Canvas widget for the galaxy background
canvas = tk.Canvas(root, width=800, height=600, bg="darkblue")
canvas.pack(fill="both", expand=True)

# Create the galaxy-themed stars
create_stars(canvas)


from tkinter import PhotoImage

def add_background_image():
    img = PhotoImage(file="galaxy_background.png")  # Path to your image
    canvas.create_image(0, 0, anchor="nw", image=img)
    canvas.image = img  # Keep a reference to avoid garbage collection

# Add this call inside the `root` setup to display the image
add_background_image()


# Function to make the stars twinkle
def twinkle_stars(canvas, stars):
    for star in stars:
        if random.random() > 0.5:
            canvas.itemconfig(star, state="hidden")
        else:
            canvas.itemconfig(star, state="normal")
    
    # Continue the animation
    canvas.after(100, twinkle_stars, canvas, stars)

def submit_data():
    sleep_time = sleep_time_entry.get()
    wake_time = wake_time_entry.get()
    notes = notes_entry.get("1.0", tk.END).strip()
    

    # Display a confirmation message
    message_label.config(text="Data submitted successfully!")

# Tkinter setup (UI part)
root = tk.Tk()
root.title("SleepSync - Log Your Sleep")

# Create a Canvas widget for the galaxy background
canvas = tk.Canvas(root, width=800, height=600, bg="darkblue")
canvas.pack(fill="both", expand=True)

# Create the galaxy-themed stars and add twinkling effect
stars = create_stars(canvas)
twinkle_stars(canvas, stars)

# Create widgets
sleep_time_label = tk.Label(root, text="Enter sleep time (HH:MM):", fg="black", font=("Comic Sans MS", 16))
sleep_time_label.pack(pady=10)

sleep_time_entry = ttk.Entry(root, font=("Comic Sans MS", 16), foreground="black", background="lightgray")
sleep_time_entry.pack(pady=10, padx=20)

wake_time_label = tk.Label(root, text="Enter wake-up time (HH:MM):", fg="black", font=("Comic Sans MS", 16))
wake_time_label.pack(pady=10)

wake_time_entry = ttk.Entry(root, font=("Comic Sans MS", 16), foreground="black", background="lightgray")
wake_time_entry.pack(pady=10, padx=20)

notes_label = tk.Label(root, text="Enter any notes:", fg="black", font=("Comic Sans MS", 16))
notes_label.pack(pady=10)

notes_entry = tk.Text(root, height=4, width=40, font=("Comic Sans MS", 16), fg="black", bg="lightgray")
notes_entry.pack(pady=10)

submit_button = ttk.Button(root, text="Submit", command=submit_data, style="TButton")
submit_button.pack(pady=20)

message_label = tk.Label(root, text="", fg="white", font=("Comic Sans MS", 16))
message_label.pack(pady=10)

# Style the button to look rounded
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="yellow", font=("Comic Sans MS", 16))
style.map("TButton", background=[("active", "lightyellow")])

# Run the Tkinter event loop
root.mainloop()