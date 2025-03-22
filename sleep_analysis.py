# Add this near the top of sleep_analysis.py
QUALITY_COLOR_MAP = {
    "😴 Excellent": "#90EE90",  # Light green
    "🙂 Good": "#ADD8E6",       # Light blue
    "😐 Average": "#FFD700",    # Gold
    "😕 Poor": "#FFA07A",       # Light salmon
    "😫 Very Poor": "#FF6347"   # Tomato red
}


import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def load_sleep_data(filepath="sleep_log.csv"):
    # ...

def calculate_average_sleep(df):
    # ...

def detect_inconsistencies(df):
    # ...

def generate_regression(df):
    # ...

def plot_sleep_graph(df, y_pred, save_path="sleep_graph.png"):
    # ...
    
    
 // Sleep quality rating 
 // Find Correlation between sleep duration and quality   
def analyze_sleep_data(filename="sleep_log.csv"):
    df = pd.read_csv(filename)

    avg_duration = df["Duration"].mean()
    avg_quality = df["Quality Rating"].mean()

    print(f"Average Sleep Duration: {avg_duration:.2f} hrs")
    print(f"Average Sleep Quality: {avg_quality:.2f} / 5")

    # Correlation between duration and quality
    correlation = df["Duration"].corr(df["Quality Rating"])
    print(f"Correlation between sleep duration and quality: {correlation:.2f}")

    return df



// Adding Sleep Quality Graph
import matplotlib.pyplot as plt

def plot_sleep_vs_quality(df):
    plt.scatter(df["Duration"], df["Quality Rating"])
    plt.title("Sleep Duration vs Quality")
    plt.xlabel("Duration (hrs)")
    plt.ylabel("Quality Rating (1–5)")
    plt.grid(True)
    plt.show()

    
    


from styling import GRAPH_LINE_COLOR


# Plot Sleep Graph
def plot_sleep_graph(df, y_pred, save_path="sleep_graph.png"):
    plt.figure(figsize=(10, 5))

    # Color-coded scatter plot based on Sleep Quality
    for quality, color in QUALITY_COLOR_MAP.items():
        subset = df[df["SleepQuality"] == quality]
        if not subset.empty:
            plt.scatter(subset["Date"], subset["SleepHours"], color=color, label=quality, alpha=0.8)

    # Plot regression line
    plt.plot(df["Date"], y_pred, color=GRAPH_LINE_COLOR, linewidth=2, label="Trend Line")

    plt.title("Sleep Duration Over Time")
    plt.xlabel("Date")
    plt.ylabel("Hours Slept")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()




# Load + Clean Sleep Data
# Parse the CSV File or other data formats
# Handle missing or messy data
# Covert dates into usdable formats
def load_sleep_data(filepath="sleep_log.csv"):
    df = pd.read_csv(filepath, header=None, names=["Date", "SleepHours", "SleepQuality"])
    df["Date"] = pd.to_datetime(df["Date"])
    df["DateOrdinal"] = df["Date"].map(pd.Timestamp.toordinal)
    return df


# Calculate Averages

def calculate_average_sleep(df):
    return df["SleepHours"].mean()


# Detect Sleep Patterns
def detect_inconsistencies(df):
    std_dev = df["SleepHours"].std()
    threshold = 1.5 * std_dev
    outliers = df[(df["SleepHours"] - df["SleepHours"].mean()).abs() > threshold]
    return outliers


# Generate Regression Model
# Fit a linear regression model to the data
# Predict sleep hours based on date
from sklearn.linear_model import LinearRegression
def generate_regression(df):
    X = df["DateOrdinal"].values.reshape(-1, 1)
    y = df["SleepHours"].values
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    return model, y_pred


# Graph Generator
# Plot and save the graph
# Optionally return image path or open it in a GUI
def plot_sleep_graph(df, y_pred, save_path="sleep_graph.png"):
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Date"], df["SleepHours"], color="skyblue", label="Actual Sleep")
    plt.plot(df["Date"], y_pred, color="purple", label="Trend Line")
    plt.title("Sleep Duration Over Time")
    plt.xlabel("Date")
    plt.ylabel("Hours Slept")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

# Run analysis on sleep data
# Load, clean, analyze, and visualize the sleep data
def run_analysis(filepath="sleep_log.csv"):
    df = load_sleep_data(filepath)
    avg = calculate_average_sleep(df)
    outliers = detect_inconsistencies(df)
    model, y_pred = generate_regression(df)
    plot_sleep_graph(df, y_pred)
    return avg, outliers

