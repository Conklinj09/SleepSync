from styling import GRAPH_LINE_COLOR

plt.plot(df["Date"], y_pred, color=GRAPH_LINE_COLOR, label="Trend Line")
