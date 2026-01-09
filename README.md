# Projects

This repository contains small quantitative experiments focused on decision theory, probability, and incentives.  

The main work is inside the `Quant Projects` folder.

---

## Quant Projects

This folder contains self-contained simulations and analyses related to betting strategies, probabilistic forecasting, and information value.

### Kelly Betting Simulation (`Kelly Betting Simulation.py`)

Simulates repeated betting using the Kelly criterion to study long-run capital growth.

Core ideas:
- Optimal bet sizing under known probabilities
- Tradeoff between growth rate and volatility
- Risk of ruin under different leverage levels

What it demonstrates:
- Monte Carlo simulation
- Log-utility maximization
- Sensitivity of outcomes to probability estimates

This script is useful for understanding why Kelly betting is theoretically optimal but practically dangerous when probabilities are misestimated.

---

### Probability Calibration (`Probability Calibration.py`)

Evaluates how well predicted probabilities match observed outcomes.

Core ideas:
- Calibration vs accuracy
- Overconfidence and underconfidence in probabilistic models
- Reliability of forecasts

What it demonstrates:
- Binning predicted probabilities
- Comparing predicted vs empirical frequencies
- Basic diagnostics for probabilistic predictions

This is directly relevant to forecasting, risk modeling, and any system that outputs probabilities rather than point estimates.

---

### Scoring Rules and Incentives (`Scoring rules incentives.r`)

Explores how different scoring rules incentivize honest probability reporting.

Core ideas:
- Proper vs improper scoring rules
- Incentive compatibility
- Why some metrics encourage truthfulness and others do not

What it demonstrates:
- Expected score analysis
- Comparison of scoring rules under different reported probabilities
- Use of R for statistical reasoning and visualization

This project connects decision theory with practical evaluation metrics used in forecasting and machine learning.

---

### Value of Information (`Value of Information.py`)

Simulates how additional information changes expected utility and decision quality.

Core ideas:
- Expected value of perfect and imperfect information
- When more data is actually worth paying for
- Diminishing returns of information

What it demonstrates:
- Decision making under uncertainty
- Utility-based comparisons
- Simulation of information updates

This is relevant to domains like trading, experimentation, and data acquisition strategy.

---

## Requirements

Python:
- Python 3.8+
- pandas
- matplotlib

R (for the scoring rules analysis):
- R base installation

---

## Setup and Usage

Clone the repository:

```bash
git clone https://github.com/hemv-857/Projects.git
cd Projects
```

Create a virtual environment and install Python dependencies:

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
.\venv\Scripts\Activate         # Windows PowerShell
pip install numpy matplotlib
```

Run any Python script:

```bash
cd "Quant Projects"
python "Kelly Betting Simulation.py"
```

Run the R script from R or RStudio:

```r
source("Scoring rules incentives.r")
```

---

## Scope and Intent

This repository is intentionally small and focused.

It exists to:
- Explore quantitative decision-making concepts
- Test ideas with simulation
- Demonstrate reasoning under uncertainty

It does not aim to:
- Be a reusable library
- Provide optimized or production-ready code
- Hide assumptions behind abstractions

---

## License

No license is currently specified.  
Without a license, reuse is not permitted by default. Add one if reuse is intended.

---

Clear reasoning beats large codebases. Every file here exists to answer a specific question, not to pad a portfolio.