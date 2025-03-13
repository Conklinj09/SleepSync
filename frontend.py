import tkinter as tk
import requests  # Library to make HTTP requests

def submit_data():
    # Collect data from the Tkinter input fields
    sleep_time = sleep_time_entry.get()
    wake_time = wake_time_entry.get()
    notes = notes_entry.get("1.0", tk.END).strip()

    # Define the URL of the Flask endpoint that will handle the POST request
    url = "http://127.0.0.1:5000/log_sleep"  # This is the route where Flask listens

    # Prepare the data to be sent as a JSON object
    data = {
        "sleep_time": sleep_time,
        "wake_time": wake_time,
        "notes": notes
    }

    try:
        # Send the POST request with the data to Flask
        response = requests.post(url, json=data)

        # Check the response from the Flask backend
        if response.status_code == 200:
            # Update the Tkinter label to indicate success
            message_label.config(text="Data submitted successfully!")
        else:
            # If something went wrong, show an error message
            message_label.config(text=f"Error: {response.status_code}")
            print(response.text)  # Print the response text for debugging

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        message_label.config(text="Failed to connect to the server.")
        print(f"Error: {e}")

# Tkinter setup (UI part)
root = tk.Tk()
root.title("SleepSync - Log Your Sleep")

# Labels and Entry fields
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

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.pack()

# Label to show the result message
message_label = tk.Label(root, text="")
message_label.pack()

# Run the Tkinter event loop
root.mainloop()
