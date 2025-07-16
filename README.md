\# ☢️ Stochastic Simulation of Probabilistic Decay Pathways Using Discrete Monte Carlo Sampling



This project simulates radioactive decay as a stochastic process using discrete-time Monte Carlo sampling. It models nuclear disintegration as a probabilistic event, where each nucleus has a fixed chance to decay during each time step. Repeating this across many nuclei and multiple runs allows us to observe how random microscopic behavior gives rise to deterministic macroscopic laws — like the exponential decay law.



---



\## 💡 Project Goals



\- Simulate radioactive decay as a discrete-time random process

\- Compare simulated decay with the analytical exponential decay curve

\- Analyze fluctuations across ensemble simulations

\- Study how fluctuations scale with initial population size (∼ 1/√N)

\- Estimate decay constants and analyze confidence intervals

\- Visualize decay curves and create animations



---



\## 📁 Folder Structure



```

stochastic-decay-simulation/

├── code/         # Python simulation and analysis scripts

├── data/         # Raw and processed simulation data (excluded from Git)

├── plots/        # Static plots of decay curves and error analysis

├── gifs/         # Animated simulations of decay processes

├── report/       # LaTeX report documenting the project

├── README.md     # Project description and instructions

├── .gitignore    # Files to ignore in version control

└── requirements.txt  # Python dependencies

```



---



\## 🚀 Getting Started



Once you clone this repository:



```bash

git clone https://github.com/yourusername/stochastic-decay-simulation.git

cd stochastic-decay-simulation

pip install -r requirements.txt

```



Then run the simulation scripts inside `code/` to begin exploring.



---



\## 🧪 Features (To Be Implemented)



\- \[ ] Core simulation of discrete stochastic decay

\- \[ ] Analytical comparison using exponential fit

\- \[ ] Fluctuation vs. N₀ scaling plots

\- \[ ] Estimation of λ and construction of confidence intervals

\- \[ ] Animated GIFs showing real-time decay

\- \[ ] Final LaTeX report with figures



---



\## 🔧 Dependencies



Python packages used:

\- `numpy`

\- `matplotlib`

\- `scipy`

\- `pillow` \*(for animations)\*



Install them with:



```bash

pip install -r requirements.txt

```



---



\## 📜 License



This project is open-source and available under the MIT License.



