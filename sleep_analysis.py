from styling import GRAPH_LINE_COLOR

plt.plot(df["Date"], y_pred, color=GRAPH_LINE_COLOR, label="Trend Line")


# Load + Clean Sleep Data
# Parse the CSV File or other data formats
# Handle missing or messy data
# Covert dates into usdable formats
def load_sleep_data(filepath="sleep_log.csv"):
    df = pd.read_csv(filepath, header=None, names=["Date", "SleepHours"])
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


