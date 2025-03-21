import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load sleep log
df = pd.read_csv("sleep_log.csv", header=None, names=["Date", "SleepHours"])

# Convert date for regression use
df["Date"] = pd.to_datetime(df["Date"])
df["DateOrdinal"] = df["Date"].map(pd.Timestamp.toordinal)

# Prepare regression inputs
X = df["DateOrdinal"].values.reshape(-1, 1)
y = df["SleepHours"].values

# Fit regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plot
plt.figure(figsize=(10, 5))
plt.scatter(df["Date"], y, color="skyblue", label="Actual Sleep")
plt.plot(df["Date"], y_pred, color="purple", label="Trend Line")
plt.title("SleepSync: Sleep Hours Over Time")
plt.xlabel("Date")
plt.ylabel("Sleep Hours")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("sleep_graph.png")  # Save image if needed
plt.show()
