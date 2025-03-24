
# Refactor comparison for sleep_analysis.py update


def update_dashboard(self):
    for widget in self.root.winfo_children():
        widget.destroy()

    # Redraw canvas background
    self.canvas = tk.Canvas(self.root, width=self.bg_image.width, height=self.bg_image.height)
    self.canvas.pack(fill="both", expand=True)
    self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

    # ✨ Restart the animated stars + shooting star
    self.stars = []  # Reset stars
    self.max_stars = 50
    self.animate_stars()
    self.launch_shooting_star()

    # Run analysis
    results = run_analysis()
    avg = results["average_sleep"]
    outliers = results["outliers"]
    quality_stats = results["quality_stats"]
    graph_path = results["graph_path"]

    # Summary title
    title = tk.Label(self.root, text="✨ SleepSync Summary ✨", font=("Helvetica", 24, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
    title.place(x=250, y=20)

    # Summary stats
    avg_label = tk.Label(self.root, text=f"Average Sleep Duration: {avg:.2f} hours", font=("Helvetica", 16), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
    avg_label.place(x=280, y=80)

    quality_label = tk.Label(self.root, text=f"Average Sleep Quality: {quality_stats['avg_quality']:.2f} / 5", font=("Helvetica", 16), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
    quality_label.place(x=280, y=110)

    correlation_label = tk.Label(self.root, text=f"Correlation Between Duration & Quality: {quality_stats['correlation']:.2f}", font=("Helvetica", 14), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
    correlation_label.place(x=230, y=140)

    # Outlier box
    outlier_label = tk.Label(self.root, text="Inconsistent Sleep Days:", font=("Helvetica", 14, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
    outlier_label.place(x=320, y=180)

    outlier_box = tk.Text(self.root, height=5, width=60, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12), borderwidth=0)
    outlier_box.place(x=120, y=220)

    if outliers.empty:
        outlier_box.insert(tk.END, "No major inconsistencies detected ✨")
    else:
        for index, row in outliers.iterrows():
            outlier_box.insert(tk.END, f"{row['Date'].strftime('%Y-%m-%d')} - {row['SleepHours']} hrs\n")
    outlier_box.config(state='disabled')

    # Sleep Graph
    if os.path.exists(graph_path):
        graph_img = Image.open(graph_path).resize((800, 300))
        self.graph_photo = ImageTk.PhotoImage(graph_img)
        graph_label = tk.Label(self.root, image=self.graph_photo, bg=BACKGROUND_COLOR)
        graph_label.image = self.graph_photo
        graph_label.place(x=50, y=330)
    else:
        graph_label = tk.Label(self.root, text="Graph not found.", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        graph_label.place(x=350, y=330)

    # Buttons
    button_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
    button_frame.place(x=250, y=650)

    rerun_btn = tk.Button(button_frame, text="🔁 Re-run Analysis", command=self.update_dashboard,
                          font=("Helvetica", 12), bg="#4A90E2", fg="white", padx=20, pady=5)
    rerun_btn.grid(row=0, column=0, padx=10)

    export_btn = tk.Button(button_frame, text="📤 Export Weekly Report", command=self.export_report,
                           font=("Helvetica", 12), bg="#7B61FF", fg="white", padx=20, pady=5)
    export_btn.grid(row=0, column=1, padx=10)

    add_entry_btn = tk.Button(button_frame, text="📝 Add Sleep Entry", command=self.add_entry,
                              font=("Helvetica", 12), bg="#00B894", fg="white", padx=20, pady=5)
    add_entry_btn.grid(row=0, column=2, padx=10)
