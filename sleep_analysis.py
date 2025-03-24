import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from styling import GRAPH_LINE_COLOR  # Make sure styling.py exists

# Map sleep quality (emoji text) to colors
QUALITY_COLOR_MAP = {
    "😴 Excellent": "#90EE90",  # Light green
    "🙂 Good": "#ADD8E6",       # Light blue
    "😐 Average": "#FFD700",    # Gold
    "😕 Poor": "#FFA07A",       # Light salmon
    "😫 Very Poor": "#FF6347"   # Tomato red
}

# Load sleep data from CSV
def load_sleep_data(filepath="sleep_log.csv"):
    df = pd.read_csv(filepath, header=None, names=["Date", "SleepHours", "SleepQuality", "Quality Rating"])
    df["Date"] = pd.to_datetime(df["Date"])
    df["DateOrdinal"] = df["Date"].map(pd.Timestamp.toordinal)
    return df

# Calculate average sleep duration
def calculate_average_sleep(df):
    return df["SleepHours"].mean()

# Detect unusual patterns in sleep duration
def detect_inconsistencies(df):
    std_dev = df["SleepHours"].std()
    threshold = 1.5 * std_dev
    outliers = df[(df["SleepHours"] - df["SleepHours"].mean()).abs() > threshold]
    return outliers

# Generate regression model (Date → SleepHours)
def generate_regression(df):
    X = df["DateOrdinal"].values.reshape(-1, 1)
    y = df["SleepHours"].values
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    return model, y_pred

# Combined graph: sleep hours + trend line + color-coded quality
def plot_sleep_graph(df, y_pred, save_path="sleep_graph.png"):
    plt.figure(figsize=(10, 5))

    # Plot each quality rating as a different color
    for quality, color in QUALITY_COLOR_MAP.items():
        subset = df[df["SleepQuality"] == quality]
        if not subset.empty:
            plt.scatter(subset["Date"], subset["SleepHours"], color=color, label=quality, alpha=0.8, edgecolors="black")

    # Add linear regression trend line
    plt.plot(df["Date"], y_pred, color=GRAPH_LINE_COLOR, linewidth=2, label="Trend Line")

    plt.title("Sleep Duration Over Time (Color-Coded by Quality)")
    plt.xlabel("Date")
    plt.ylabel("Hours Slept")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    return save_path

# Analyze correlation between sleep duration and quality
def analyze_sleep_data(df):
    avg_duration = df["SleepHours"].mean()
    avg_quality = df["Quality Rating"].mean()
    correlation = df["SleepHours"].corr(df["Quality Rating"])

    print(f"Average Sleep Duration: {avg_duration:.2f} hrs")
    print(f"Average Sleep Quality: {avg_quality:.2f} / 5")
    print(f"Correlation between duration and quality: {correlation:.2f}")

    return {
        "avg_duration": avg_duration,
        "avg_quality": avg_quality,
        "correlation": correlation
    }

# Full pipeline: load data, analyze, visualize
def run_analysis(filepath="sleep_log.csv"):
    df = load_sleep_data(filepath)
    avg = calculate_average_sleep(df)
    outliers = detect_inconsistencies(df)
    model, y_pred = generate_regression(df)
    plot_path = plot_sleep_graph(df, y_pred)
    quality_summary = analyze_sleep_data(df)

    return {
        "average_sleep": avg,
        "outliers": outliers,
        "regression_model": model,
        "graph_path": plot_path,
        "quality_stats": quality_summary
    }
