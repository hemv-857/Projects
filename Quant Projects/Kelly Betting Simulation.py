import random
import math
import matplotlib.pyplot as plt

# -----------------------------
# 1. SIMULATE BETTING OUTCOME
# -----------------------------

def simulate_outcomes(n, p_true, seed=42):
    random.seed(seed)
    return [1 if random.random() < p_true else 0 for _ in range(n)]

# -----------------------------
# 2. BETTING STRATEGIES
# -----------------------------

def kelly_fraction(p_hat):
    return max(0.0, 2 * p_hat - 1)

def simulate_wealth(outcomes, f):
    wealth = 1.0
    history = [wealth]

    for y in outcomes:
        bet = f * wealth
        if y == 1:
            wealth += bet
        else:
            wealth -= bet
        history.append(wealth)

        if wealth <= 0:
            break

    return history

# -----------------------------
# 3. EXPERIMENT
# -----------------------------

def run_experiment():
    n = 300
    p_true = 0.55      # real edge
    p_hat = 0.60       # overestimated belief

    outcomes = simulate_outcomes(n, p_true)

    strategies = {
        "Full Kelly": kelly_fraction(p_hat),
        "Half Kelly": 0.5 * kelly_fraction(p_hat),
        "Fixed 5%": 0.05,
        "No Bet": 0.0
    }

    results = {}
    for name, f in strategies.items():
        results[name] = simulate_wealth(outcomes, f)

    return results

# -----------------------------
# 4. PLOT RESULTS
# -----------------------------

def plot_wealth(results):
    plt.figure(figsize=(8, 5))

    for name, wealth_path in results.items():
        plt.plot(wealth_path, label=name)

    plt.xlabel("Bet Number")
    plt.ylabel("Wealth")
    plt.title("Wealth Evolution Under Different Betting Strategies")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -----------------------------
# 5. MAIN
# -----------------------------

if __name__ == "__main__":
    results = run_experiment()
    plot_wealth(results)