import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
#means = df.groupby("level", as_index = False)["attempt"].mean()
mean_of_attempts = df.groupby(["level", "student_id"], as_index=False)[
    "attempt"].mean()
#graph = px.scatter(means, x=df["student_id"], y=df["level"],
#                   color=means["attempt"], size=means["attempt"])
graph = px.scatter(mean_of_attempts, x="student_id",
                   y="level", size="attempt", color="attempt")
graph.show()
