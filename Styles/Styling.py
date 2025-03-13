import tkinter as tk
from tkinter import ttk
import random

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



# Create widgets
sleep_time_label = tk.Label(root, text="Enter sleep time (HH:MM):", fg="black", font=("Arial", 14))
sleep_time_label.pack(pady=10)

sleep_time_entry = tk.Entry(root, font=("Arial", 14), fg="black", bg="lightgray")
sleep_time_entry.pack(pady=10)

wake_time_label = tk.Label(root, text="Enter wake-up time (HH:MM):", fg="black", font=("Arial", 14))
wake_time_label.pack(pady=10)

wake_time_entry = tk.Entry(root, font=("Arial", 14), fg="black", bg="lightgray")
wake_time_entry.pack(pady=10)

notes_label = tk.Label(root, text="Enter any notes:", fg="black", font=("Arial", 14))
notes_label.pack(pady=10)

notes_entry = tk.Text(root, height=4, width=40, font=("Arial", 14), fg="black", bg="lightgray")
notes_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_data, font=("Arial", 14), bg="yellow", fg="black")
submit_button.pack(pady=20)

message_label = tk.Label(root, text="", fg="white", font=("Arial", 14))
message_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
