import tkinter as tk
import requests  # We'll use this to send data to Flask

def submit_data():
    # Collect the data from the input fields
    sleep_time = sleep_time_entry.get()
    wake_time = wake_time_entry.get()
    notes = notes_entry.get("1.0", tk.END).strip()

    # Send data to Flask backend using a POST request
    url = "http://127.0.0.1:5000/log_sleep"  # Flask backend endpoint
    data = {
        "sleep_time": sleep_time,
        "wake_time": wake_time,
        "notes": notes
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        message_label.config(text="Data submitted successfully!")
    else:
        message_label.config(text="Failed to submit data. Please try again.")

# Set up the main window
root = tk.Tk()
root.title("SleepSync - Log Your Sleep")

# Create widgets
sleep_time_label = tk.Label(root, text="Enter sleep time (HH:MM):")
sleep_time_label.pack()

sleep_time_entry = tk.Entry(root)
sleep_time_entry.pack()

wake_time_label = tk.Label(root, text="Enter wake-up time (HH:MM):")
wake_time_label.pack()

wake_time_entry = tk.Entry(root)
wake_time_entry.pack()

notes_label = tk.Label(root, text="Enter any notes:")
notes_label.pack()

notes_entry = tk.Text(root, height=4, width=40)
notes_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.pack()

message_label = tk.Label(root, text="")
message_label.pack()

# Run the GUI
root.mainloop()
