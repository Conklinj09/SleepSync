import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
from sleep_analysis import run_analysis
from styling import BACKGROUND_COLOR, TEXT_COLOR
from generate_report import generate_weekly_report
from datetime import datetime, timedelta
import csv

class SleepSyncApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SleepSync Dashboard 🌙")
        self.root.geometry("900x700")
        self.root.configure(bg=BACKGROUND_COLOR)

        # Load and place background image
        self.bg_image = Image.open("starry_bg.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=self.bg_image.width, height=self.bg_image.height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.stars = []
        self.max_stars = 50
        self.animate_stars()
        self.launch_shooting_star()

        self.graph_photo = None
        self.update_dashboard()

    def animate_stars(self):
        for star in self.stars:
            self.canvas.delete(star)
        self.stars.clear()

        for _ in range(self.max_stars):
            x = random.randint(0, self.bg_image.width)
            y = random.randint(0, self.bg_image.height)
            size = random.randint(1, 3)
            color = random.choice(["white", "light yellow", "light gray"])
            star = self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline=color)
            self.stars.append(star)

        self.root.after(500, self.animate_stars)

    def launch_shooting_star(self):
        x_start = random.randint(-100, self.bg_image.width // 2)
        y_start = random.randint(0, self.bg_image.height // 3)

        comet = self.canvas.create_oval(x_start, y_start, x_start + 4, y_start + 4, fill="white", outline="white")

        def move_comet(x, y, comet_id):
            if x < self.bg_image.width and y < self.bg_image.height:
                self.canvas.move(comet_id, 5, 3)
                self.root.after(30, lambda: move_comet(x + 5, y + 3, comet_id))
            else:
                self.canvas.delete(comet_id)

        move_comet(x_start, y_start, comet)
        next_star_delay = random.randint(4000, 10000)
        self.root.after(next_star_delay, self.launch_shooting_star)

    def update_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.root, width=self.bg_image.width, height=self.bg_image.height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        avg, outliers = run_analysis()

        title = tk.Label(self.root, text="✨ SleepSync Summary ✨", font=("Helvetica", 24, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        title.place(x=250, y=20)

        avg_label = tk.Label(self.root, text=f"Average Sleep Duration: {avg:.2f} hours", font=("Helvetica", 16), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        avg_label.place(x=280, y=80)

        outlier_label = tk.Label(self.root, text="Inconsistent Sleep Days:", font=("Helvetica", 14, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        outlier_label.place(x=320, y=130)

        outlier_box = tk.Text(self.root, height=5, width=60, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12), borderwidth=0)
        outlier_box.place(x=120, y=170)

        if outliers.empty:
            outlier_box.insert(tk.END, "No major inconsistencies detected ✨")
        else:
            for index, row in outliers.iterrows():
                outlier_box.insert(tk.END, f"{row['Date'].strftime('%Y-%m-%d')} - {row['SleepHours']} hrs\n")
        outlier_box.config(state='disabled')

        graph_img = Image.open("sleep_graph.png").resize((800, 300))
        self.graph_photo = ImageTk.PhotoImage(graph_img)
        graph_label = tk.Label(self.root, image=self.graph_photo, bg=BACKGROUND_COLOR)
        graph_label.image = self.graph_photo
        graph_label.place(x=50, y=300)

        button_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        button_frame.place(x=250, y=620)

        rerun_btn = tk.Button(button_frame, text="🔁 Re-run Analysis", command=self.update_dashboard,
                              font=("Helvetica", 12), bg="#4A90E2", fg="white", padx=20, pady=5)
        rerun_btn.grid(row=0, column=0, padx=10)

        export_btn = tk.Button(button_frame, text="📤 Export Weekly Report", command=self.export_report,
                               font=("Helvetica", 12), bg="#7B61FF", fg="white", padx=20, pady=5)
        export_btn.grid(row=0, column=1, padx=10)

        add_entry_btn = tk.Button(button_frame, text="📝 Add Sleep Entry", command=self.add_entry,
                                  font=("Helvetica", 12), bg="#00B894", fg="white", padx=20, pady=5)
        add_entry_btn.grid(row=0, column=2, padx=10)

    def export_report(self):
        generate_weekly_report()

    def add_entry(self):
        entry_win = tk.Toplevel(self.root)
        entry_win.title("Add Sleep Entry")
        entry_win.geometry("400x400")
        entry_win.configure(bg=BACKGROUND_COLOR)

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

        tk.Label(entry_win, text="Sleep Quality:", fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(pady=5)
        quality_var = tk.StringVar()
        sleep_quality_dropdown = ttk.Combobox(entry_win, textvariable=quality_var, state="readonly",
                                              values=["🛌 Excellent", "🙂 Good", "😐 Average", "😕 Poor", "😫 Very Poor"])
        sleep_quality_dropdown.current(2)
        sleep_quality_dropdown.pack()

        def submit_entry():
            date = date_entry.get()
            sleep_time = sleep_time_entry.get()
            wake_time = wake_time_entry.get()
            quality = quality_var.get()

            try:
                sleep_dt = datetime.strptime(f"{date} {sleep_time}", "%Y-%m-%d %H:%M")
                wake_dt = datetime.strptime(f"{date} {wake_time}", "%Y-%m-%d %H:%M")
                if wake_dt <= sleep_dt:
                    wake_dt += timedelta(days=1)

                hours_slept = round((wake_dt - sleep_dt).total_seconds() / 3600, 2)

                with open("sleep_log.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([date, hours_slept, quality])

                print(f"📝 Logged {hours_slept} hours on {date}")
                entry_win.destroy()
                self.update_dashboard()

            except Exception as e:
                error_label.config(text=f"Error: {str(e)}")

        submit_btn = tk.Button(entry_win, text="Submit", command=submit_entry, bg="#00B894", fg="white")
        submit_btn.pack(pady=10)

        error_label = tk.Label(entry_win, text="", fg="red", bg=BACKGROUND_COLOR)
        error_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SleepSyncApp(root)
    update_dashboard() # Initial update
    root.mainloop()


// Adding drop down for sleep quality

from tkinter import StringVar, Label, OptionMenu

quality_var = StringVar()
quality_var.set("3")  # Default value

Label(root, text="Sleep Quality (1-5):").pack()
OptionMenu(root, quality_var, "1", "2", "3", "4", "5").pack()




// Update Submit Button Handler
def submit_sleep_data():
    date = date_entry.get()
    sleep_time = sleep_time_entry.get()
    wake_time = wake_time_entry.get()
    quality_rating = int(quality_var.get())

    log_sleep_entry(date, sleep_time, wake_time, quality_rating)
    messagebox.showinfo("Success", "Sleep entry recorded!")

