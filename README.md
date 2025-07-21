# Stochastic Simulation of Probabilistic Decay Pathways Using Discrete Monte Carlo Sampling

This project simulates the radioactive decay process using discrete-time Monte Carlo techniques. It analyzes how statistical noise scales with population size by computing RMS deviations from the analytical decay law, and presents both absolute and normalized error trends over varying initial populations  N_0 belongs to [10, 10^4] \).

---

## Repository Structure

stochastic-decay-simulation

│
├── code/
│ ├── decay_sim.py # Core simulation logic (decay curves)
│ ├── analysis.py # RMS deviation analysis and log-log scaling
│ └── animate_decay.py # Decay animation (GIF)
│
├── plots/
│ ├── decay_simulation.gif # Animated decay process (theory vs MC)
│ ├── rms_vs_N0_absolute.png # Absolute RMS vs N₀ (log-log plot)
│ └── rms_vs_N0_normalized.png# Normalized RMS vs N₀ (log-log plot)
│
├── main.tex # LaTeX Report (full analysis)
├── README.md # You're here.
└── requirements.txt # All Python dependencies

---

##  Key Features

- Simulates decay across multiple time steps and trials.
- Computes RMS deviation between theoretical and Monte Carlo decay.
- Analyzes absolute and normalized error scaling across \( N_0 \in [10, 10^4] \).
- Fits power-law scaling using `scipy.optimize.curve_fit`.
- Exports high-quality plots and GIF animation.
- Full report available in LaTeX format.

---

##  Installation

### 1. Clone this Repository

git clone https://github.com/SoumitraPharikal/stochastic-decay-simulation.git
cd stochastic-decay-simulation
2. Create a Virtual Environment (Recommended)
python -m venv .venv
source .venv/bin/activate        # On Unix or macOS
.venv\Scripts\activate           # On Windows
3. Install Dependencies
pip install -r requirements.txt
### How to Run
Simulation + RMS Analysis

python code/animate_decay.py
python code/analysis.py
Animated Decay Process (GIF)

All output files (plots and animations) are saved to the plots/ folder.

### Report
The full technical report is written in LaTeX and available in the report Folder.

Contents include:
Theoretical background and decay law derivation
Stochastic modeling methodology
Power-law fit and residual analysis
Animation overview
Reproducible Python code (included in appendix)

### System Requirements
Python ≥ 3.9

RAM: ≥ 4 GB

Disk: ~200 MB

Recommended: Jupyter, VS Code, or LaTeX editor for report compilation


Project completed as part of independent exploration of statistical modeling and computational physics.


### Acknowledgements
Thanks to open-source libraries like NumPy, SciPy, and Matplotlib. Animation made possible using FuncAnimation and Pillow.


### License
This project is open-source under the MIT License.
