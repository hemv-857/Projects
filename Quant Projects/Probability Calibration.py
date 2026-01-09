"""
PROBABILITY CALIBRATION.py

Purpose:
Study probability calibration under distribution shift
using simple, interpretable models.

Tools:
- Python standard library
- pandas
- matplotlib
"""

import random
import math
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. DATA GENERATION
# -----------------------------

def generate_binary_stream(n, p1, p2=None, switch_point=None, seed=50):
    random.seed(seed)
    outcomes = []

    for i in range(n):
        if (p2 is not None and switch_point is not None and i >= switch_point):
            p = p2
        else:
            p = p1
        outcomes.append(1 if random.random() < p else 0)

    return outcomes

# -----------------------------
# 2. PROBABILISTIC MODELS
# -----------------------------

def mean_probability(y):
    return sum(y) / len(y)

def well_specified_model(y_train):
    p = mean_probability(y_train)
    return lambda n: [p] * n

def mis_specified_model(y_train):
    p = min(max(mean_probability(y_train) + 0.30, 0.0), 1.0)
    return lambda n: [p] * n

def overconfident_model(y_train):
    p = mean_probability(y_train)
    return lambda n: [0.95 if p >= 0.5 else 0.05] * n

# -----------------------------
# 3. SCORING RULES
# -----------------------------

def brier_score(y_true, p_pred):
    errors = [(p_pred[i] - y_true[i]) ** 2 for i in range(len(y_true))]
    return sum(errors) / len(errors)

def log_loss(y_true, p_pred, eps=1e-12):
    losses = []
    for y, p in zip(y_true, p_pred):
        p = min(max(p, eps), 1 - eps)
        losses.append(-(y * math.log(p) + (1 - y) * math.log(1 - p)))
    return sum(losses) / len(losses)

# -----------------------------
# 4. CALIBRATION CURVE
# -----------------------------

def calibration_curve(y_true, p_pred, bins=10):
    df = pd.DataFrame({"y": y_true, "p": p_pred})
    df["bin"] = pd.cut(df["p"], bins=bins)

    grouped = df.groupby("bin", observed=False)
    mean_pred = grouped["p"].mean()
    mean_true = grouped["y"].mean()

    return mean_pred.tolist(), mean_true.tolist()

# -----------------------------
# 5. EXPERIMENT
# -----------------------------

def run_experiment():
    n = int(input("Enter the length of the binary stream: "))
    switch_point = int(input(f"Enter the switch point (1 to {n-1}): "))

    y = generate_binary_stream(
        n=n,
        p1=0.38,
        p2=0.56,
        switch_point=switch_point
    )

    train_y = y[:switch_point]
    test_y = y[switch_point:]

    models = {
        "Well Specified": well_specified_model(train_y),
        "Mis Specified": mis_specified_model(train_y),
        "Overconfident": overconfident_model(train_y)
    }

    results = {}

    for name, model in models.items():
        p_test = model(len(test_y))

        results[name] = {
            "brier": brier_score(test_y, p_test),
            "log_loss": log_loss(test_y, p_test),
            "calibration": calibration_curve(test_y, p_test)
        }

    return results

# -----------------------------
# 6. VISUALIZATION
# -----------------------------

def plot_reliability(results):
    plt.figure(figsize=(6, 6))

    for name, res in results.items():
        mp, mt = res["calibration"]
        plt.plot(mp, mt, marker="o", label=name)

    plt.plot([0, 1], [0, 1], "--", color="gray")
    plt.xlabel("Predicted Probability")
    plt.ylabel("Empirical Frequency")
    plt.title("Reliability Diagram")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -----------------------------
# 7. MAIN
# -----------------------------

if __name__ == "__main__":
    results = run_experiment()

    print("\nMODEL PERFORMANCE (TEST SET)\n")
    for name, res in results.items():
        print(name)
        print(f"  Brier Score : {res['brier']:.4f}")
        print(f"  Log Loss    : {res['log_loss']:.4f}\n")

    plot_reliability(results)