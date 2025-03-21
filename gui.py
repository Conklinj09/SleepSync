import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from sleep_analysis import run_analysis
from styling import BACKGROUND_COLOR, TEXT_COLOR

# Run analysis to get data
avg, outliers = run_analysis()

# Create GUI window
root = tk.Tk()
root.title("SleepSync Dashboard 🌙")
root.geometry("900x600")
root.configure(bg=BACKGROUND_COLOR)

# Title label
title = tk.Label(root, text="✨ SleepSync Summary ✨", font=("Helvetica", 24, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
title.pack(pady=20)

# Show average sleep
avg_label = tk.Label(root, text=f"Average Sleep Duration: {avg:.2f} hours", font=("Helvetica", 16), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
avg_label.pack()

# Show outlier list
outlier_label = tk.Label(root, text="Inconsistent Sleep Days:", font=("Helvetica", 14, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
outlier_label.pack(pady=(20, 5))

outlier_box = tk.Text(root, height=5, width=60, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12), borderwidth=0)
outlier_box.pack()

if outliers.empty:
    outlier_box.insert(tk.END, "No major inconsistencies detected 🌈")
else:
    for index, row in outliers.iterrows():
        outlier_box.insert(tk.END, f"{row['Date'].strftime('%Y-%m-%d')} - {row['SleepHours']} hrs\n")

outlier_box.config(state='disabled')

# Load and show graph image
graph_img = Image.open("sleep_graph.png")
graph_img = graph_img.resize((800, 300))
graph_photo = ImageTk.PhotoImage(graph_img)

graph_label = tk.Label(root, image=graph_photo, bg=BACKGROUND_COLOR)
graph_label.pack(pady=20)

# Run the app
root.mainloop()
