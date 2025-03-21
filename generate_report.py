# generate_report.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime, timedelta
import pandas as pd
import os

def generate_weekly_report(log_path="sleep_log.csv", graph_path="sleep_graph.png", report_path="SleepSync_Weekly_Report.pdf"):
    # Load data
    df = pd.read_csv(log_path, header=None, names=["Date", "SleepHours", "SleepQuality"])
    df["Date"] = pd.to_datetime(df["Date"])

    # Filter for last 7 days
    today = datetime.now().date()
    last_week = today - timedelta(days=7)
    weekly_data = df[df["Date"].dt.date >= last_week]

    if weekly_data.empty:
        print("❗ No data for the last 7 days.")
        return

    avg_sleep = weekly_data["SleepHours"].mean()
    quality_counts = weekly_data["SleepQuality"].value_counts()

    # Setup PDF
    c = canvas.Canvas(report_path, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 60, "🌙 SleepSync Weekly Report")

    # Date Range
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 90, f"Date Range: {last_week} to {today}")
    c.drawString(50, height - 110, f"Average Sleep Duration: {avg_sleep:.2f} hours")

    # Sleep Quality Summary
    c.drawString(50, height - 140, "Sleep Quality Breakdown:")
    y = height - 160
    for quality, count in quality_counts.items():
        c.drawString(70, y, f"{quality}: {count} nights")
        y -= 20

    # Insert graph image
    if os.path.exists(graph_path):
        img = ImageReader(graph_path)
        c.drawImage(img, 50, 150, width=500, height=250)  # adjust if needed
    else:
        c.drawString(50, 160, "No graph image found.")

    # Closing message
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 100, "✨ Keep showing up for yourself, one night at a time. ✨")

    # Save PDF
    c.save()
    print(f"✅ Weekly report saved as: {report_path}")
