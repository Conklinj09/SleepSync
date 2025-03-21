import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from sleep_analysis import run_analysis
from styling import BACKGROUND_COLOR, TEXT_COLOR

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

# Placeholder functions
def export_report():
    print("📤 Export Weekly Report feature coming soon!")

def add_entry():
    print("📝 Add Sleep Entry feature coming soon!")

# Run the dashboard initially
update_dashboard()

# Run app
root.mainloop()
