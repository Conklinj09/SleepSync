import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from sleep_analysis import run_analysis
from styling import BACKGROUND_COLOR, TEXT_COLOR
from generate_report import generate_weekly_report
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("SleepSync")

# Load background image
bg_image = Image.open("starry_bg.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create canvas and set image
canvas = Canvas(root, width=bg_image.width, height=bg_image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Add your widgets here on top of the background

root.mainloop()








# Create main window
root = tk.Tk()
root.title("SleepSync Dashboard 🌙")
root.geometry("900x700")
root.configure(bg=BACKGROUND_COLOR)




# Keep a reference to the image so it's not garbage collected
graph_photo = None

# Function to update content
def update_dashboard():
    global graph_photo  # So image isn't garbage collected
    
    # Clear previous widgets
    for widget in root.winfo_children():
        widget.destroy()
    
    # Run analysis
    avg, outliers = run_analysis()
    
    # Title
    title = tk.Label(root, text="✨ SleepSync Summary ✨", font=("Helvetica", 24, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
    title.pack(pady=20)

    # Average sleep label
    avg_label = tk.Label(root, text=f"Average Sleep Duration: {avg:.2f} hours", font=("Helvetica", 16), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
    avg_label.pack()

    # Outlier section
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

    # Graph image
    graph_img = Image.open("sleep_graph.png")
    graph_img = graph_img.resize((800, 300))
    graph_photo = ImageTk.PhotoImage(graph_img)
    graph_label = tk.Label(root, image=graph_photo, bg=BACKGROUND_COLOR)
    graph_label.image = graph_photo  # Keep reference
    graph_label.pack(pady=20)

    # Button Frame
    button_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
    button_frame.pack(pady=10)

    # 🔁 Re-run Analysis Button
    rerun_btn = tk.Button(button_frame, text="🔁 Re-run Analysis", command=update_dashboard,
                          font=("Helvetica", 12), bg="#4A90E2", fg="white", padx=20, pady=5)
    rerun_btn.grid(row=0, column=0, padx=10)

    # 📤 Export Report Button (placeholder)
    export_btn = tk.Button(button_frame, text="📤 Export Weekly Report", command=export_report,
                           font=("Helvetica", 12), bg="#7B61FF", fg="white", padx=20, pady=5)
    export_btn.grid(row=0, column=1, padx=10)

    # 📝 Add Sleep Entry Button (placeholder)
    add_entry_btn = tk.Button(button_frame, text="📝 Add Sleep Entry", command=add_entry,
                              font=("Helvetica", 12), bg="#00B894", fg="white", padx=20, pady=5)
    add_entry_btn.grid(row=0, column=2, padx=10)


# Function to export the weekly report
from generate_report import generate_weekly_report  # Make sure this is at the top

def export_report():
    generate_weekly_report()  # This will create and save the PDF report




# add sleep entry drop down
def add_entry():
    # Pop-up window
    entry_win = tk.Toplevel(root)
    entry_win.title("Add Sleep Entry")
    entry_win.geometry("400x400")
    entry_win.configure(bg=BACKGROUND_COLOR)

    # Labels + Inputs
    tk.Label(entry_win, text="Date (YYYY-MM-DD):", fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(pady=5)
    date_entry = tk.Entry(entry_win)
    date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
    date_entry.pack()

    tk.Label(entry_win, text="Sleep Time (HH:MM 24hr):", fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(pady=5)
    sleep_time_entry = tk.Entry(entry_win)
    sleep_time_entry.pack()

    tk.Label(entry_win, text="Wake Time (HH:MM 24hr):", fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(pady=5)
    wake_time_entry = tk.Entry(entry_win)
    wake_time_entry.pack()

    # Sleep Quality Dropdown
    tk.Label(entry_win, text="Sleep Quality:", fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(pady=5)
    quality_var = tk.StringVar()
    sleep_quality_dropdown = ttk.Combobox(entry_win, textvariable=quality_var, state="readonly",
                                          values=["😴 Excellent", "🙂 Good", "😐 Average", "😕 Poor", "😫 Very Poor"])
    sleep_quality_dropdown.current(2)  # Default to "Average"
    sleep_quality_dropdown.pack()

    # Submit button
    def submit_entry():
        date = date_entry.get()
        sleep_time = sleep_time_entry.get()
        wake_time = wake_time_entry.get()
        quality = quality_var.get()

        try:
            # Convert to datetime objects
            sleep_dt = datetime.strptime(f"{date} {sleep_time}", "%Y-%m-%d %H:%M")
            wake_dt = datetime.strptime(f"{date} {wake_time}", "%Y-%m-%d %H:%M")
            if wake_dt <= sleep_dt:
                wake_dt += timedelta(days=1)

            # Calculate hours
            hours_slept = round((wake_dt - sleep_dt).total_seconds() / 3600, 2)

            # Append to CSV
            with open("sleep_log.csv", "a", newline="") as f:
                writer =

    
    
from datetime import datetime, timedelta
import csv

def add_entry():
    # Pop-up window
    entry_win = tk.Toplevel(root)
    entry_win.title("Add Sleep Entry")
    entry_win.geometry("400x300")
    entry_win.configure(bg=BACKGROUND_COLOR)

    # Labels + Entries
    tk.Label(entry_win, text="Date (YYYY-MM-DD):", fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(pady=5)
    date_entry = tk.Entry(entry_win)
    date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
    date_entry.pack()

    tk.Label(entry_win, text="Sleep Time (HH:MM 24hr):", fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(pady=5)
    sleep_time_entry = tk.Entry(entry_win)
    sleep_time_entry.pack()

    tk.Label(entry_win, text="Wake Time (HH:MM 24hr):", fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(pady=5)
    wake_time_entry = tk.Entry(entry_win)
    wake_time_entry.pack()

    # Submit button
    def submit_entry():
        date = date_entry.get()
        sleep_time = sleep_time_entry.get()
        wake_time = wake_time_entry.get()

        try:
            # Convert times to datetime
            sleep_dt = datetime.strptime(f"{date} {sleep_time}", "%Y-%m-%d %H:%M")
            wake_dt = datetime.strptime(f"{date} {wake_time}", "%Y-%m-%d %H:%M")

            # If wake time is earlier than sleep, assume next day
            if wake_dt <= sleep_dt:
                wake_dt += timedelta(days=1)

            # Calculate hours slept
            hours_slept = round((wake_dt - sleep_dt).total_seconds() / 3600, 2)

            # Append to CSV
            with open("sleep_log.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([date, hours_slept])

            print(f"📝 Logged {hours_slept} hours on {date}")
            entry_win.destroy()
            update_dashboard()  # Optional: refresh UI

        except Exception as e:
            error_label.config(text=f"Error: {str(e)}")

    submit_btn = tk.Button(entry_win, text="Submit", command=submit_entry, bg="#00B894", fg="white")
    submit_btn.pack(pady=10)

    error_label = tk.Label(entry_win, text="", fg="red", bg=BACKGROUND_COLOR)
    error_label.pack()

    

# Run the dashboard initially
update_dashboard()

# Run app
root.mainloop()
