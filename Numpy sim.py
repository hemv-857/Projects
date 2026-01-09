import numpy as np
import matplotlib.pyplot as plpt
import json

data = np.random.normal(loc=50, scale=10, size=10000)

stats = {
    "mean": float(np.mean(data)),
    "median": float(np.median(data)),
    "variance": float(np.var(data)),
    "std_dev": float(np.std(data))
}

with open("stats.json", "w") as f:
    json.dump(stats, f, indent=2)

plpt.hist(data, bins=50)
plpt.xlabel("Value")
plpt.ylabel("Frequency")
plpt.title("Histogram of Generated Data")
plpt.savefig("histogram.png")
plpt.close()

print("Simulation complete. Files generated: stats.json, histogram.png")