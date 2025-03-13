from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to handle sleep data submission
@app.route("/log_sleep", methods=["POST"])
def log_sleep():
    data = request.get_json()

    sleep_time = data.get("sleep_time")
    wake_time = data.get("wake_time")
    notes = data.get("notes")

    # Here you can process the data, e.g., save it to a file or database
    # For now, let's just print the data to the console
    print(f"Sleep time: {sleep_time}")
    print(f"Wake time: {wake_time}")
    print(f"Notes: {notes}")

    # Respond back to Tkinter with success
    response = jsonify({"status": "success", "message": "Data logged successfully!"})
    response.status_code = 200  # HTTP success status code
    return response

if __name__ == "__main__":
    app.run(debug=True)
