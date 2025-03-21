# 🌙 SleepSync 🐸  
**Track your sleep, spot trends, and sync with your natural rhythm.**  
A cozy sleep tracking application built in C, Python, and Tkinter with beautiful graphing and mindful wellness insights.

---

![Python](https://img.shields.io/badge/python-3.10-blue)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![GUI: Tkinter](https://img.shields.io/badge/GUI-Tkinter-blueviolet)
![PDF Reports](https://img.shields.io/badge/feature-PDF%20Reports-informational)
![Sleepy Vibes](https://img.shields.io/badge/vibe-cozy%20dreams-ff69b4)
![Made with Frog](https://img.shields.io/badge/made%20with-%F0%9F%90%B8-green)

## ✨ Features

### ✅ Core Functionality:
- ⌨️ **C-based Logging System**  
  Logs your sleep data including sleep/wake time and saves it to `sleep_log.csv`.

- 📈 **Sleep Data Analysis with Linear Regression**  
  Python calculates your sleep trends over time and visualizes them with a best-fit line.

- 🖼️ **Graph with Color-Coded Sleep Quality**  
  Each night's sleep is represented with a color-coded dot based on how well you slept:
  - 😴 Excellent → Green
  - 🙂 Good → Blue
  - 😐 Average → Gold
  - 😕 Poor → Salmon
  - 😫 Very Poor → Red

- 📊 **Tkinter Dashboard (GUI)**  
  An intuitive, cozy dashboard shows:
  - Average sleep duration
  - Inconsistent sleep nights (outliers)
  - A scatterplot of your sleep over time
  - Easy-to-use buttons to trigger features

- 📝 **Add New Sleep Entry Popup**  
  Log new entries with:
  - Date
  - Sleep Time
  - Wake Time
  - Sleep Quality (via dropdown menu)  
  The system auto-calculates total sleep duration and appends it to your CSV file.

- 📤 **Generate Weekly PDF Report**  
  Create a downloadable PDF showing:
  - Weekly date range
Create a downloadable PDF showing:
  - Weekly date range
  - Average sleep hours
  - Sleep quality breakdown
  - Your color-coded graph
  - A soft affirmation to keep you motivated 🌟

---

## 🗂 File Structure
SleepSync/ ├── sleep_log.csv # Your sleep data file ├── sleep_analysis.py # Analyzes data + generates graph ├── gui.py # Main Tkinter dashboard ├── generate_report.py # PDF report generator ├── styling.py # Color themes and aesthetic constants └── sleep_graph.png # Generated graph image


---

## 🚀 How to Run

### 📌 Prerequisites:
Install the required Python packages:

```bash
pip install pandas matplotlib scikit-learn pillow reportlab


## 🧪 Run the GUI:
bash
Copy
Edit
python gui.py

Click buttons in the interface to:

Add new sleep logs
View updated insights
Export your weekly PDF report


## 🌌 Sleep Quality Legend
Emoji	Meaning	Graph Color
😴 Excellent	Best quality	Green
🙂 Good	Restful sleep	Blue
😐 Average	Neutral	Gold
😕 Poor	Restless	Salmon
😫 Very Poor	Low quality	Red

# 💖 Created By
Jeanette Conklin
SleepSync is part of a passion project to merge wellness + coding ✨

# 🛠️ License
This project is licensed under the GNU GPLv3 License.

## 🤝 Contributions
Contributions are welcome! Just be gentle and keep it dreamy. 🌙

yaml
Copy
Edit

---










