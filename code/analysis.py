import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit

# ---------- Utility Functions ---------- #
def analytical_decay(N0, lambda_decay, steps):
    t = np.arange(steps)
    return N0 * np.exp(-lambda_decay * t)

def simulate_decay(N0, lambda_decay, steps):
    N = N0
    results = [N]
    for _ in range(1, steps):
        decay_chance = np.random.rand(N)
        decayed = np.sum(decay_chance < lambda_decay)
        N -= decayed
        results.append(N)
    return np.array(results)

def compute_rms_over_curve(sim_runs, theory):
    diffs = [np.mean((sim - theory)**2) for sim in sim_runs]
    rms_vals = np.sqrt(diffs)
    return np.mean(rms_vals), np.std(rms_vals), rms_vals

def power_law(N, A, alpha):
    return A * N ** alpha

def setup_paths():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    plots_dir = os.path.join(os.path.dirname(current_dir), 'plots')
    os.makedirs(plots_dir, exist_ok=True)
    return plots_dir

def run_simulation(N0_values, lambda_decay, steps, runs):
    rms_list = []
    rms_std_list = []
    rms_norm_list = []
    rms_norm_std_list = []

    for N0 in N0_values:
        theory = analytical_decay(N0, lambda_decay, steps)
        sim_runs = [simulate_decay(N0, lambda_decay, steps) for _ in range(runs)]
        rms_mean, rms_std, _ = compute_rms_over_curve(sim_runs, theory)
        rms_list.append(rms_mean)
        rms_std_list.append(rms_std)
        rms_norm_list.append(rms_mean / np.sqrt(N0))
        rms_norm_std_list.append(rms_std / np.sqrt(N0))

    return (np.array(rms_list), np.array(rms_std_list),
            np.array(rms_norm_list), np.array(rms_norm_std_list))

# ---------- Main Simulation and Analysis ---------- #
def main():
    np.random.seed(42)
    lambda_decay = 0.1
    steps = 75
    runs = 20
    N0_values_all = np.unique(np.logspace(np.log10(10), np.log10(10000), num=20, dtype=int))
    plots_dir = setup_paths()

    print("Running single computation...")

    rms_array, rms_std_array, rms_norm_array, rms_norm_std_array = run_simulation(N0_values_all, lambda_decay, steps, runs)

    fit_mask = (N0_values_all >= 100) & (N0_values_all <= 1000)
    N0_fit = N0_values_all[fit_mask]
    rms_fit = rms_array[fit_mask]
    rms_norm_fit = rms_norm_array[fit_mask]

    params_abs, _ = curve_fit(power_law, N0_fit, rms_fit)
    A_abs, alpha_abs = params_abs

    params_norm, _ = curve_fit(power_law, N0_fit, rms_norm_fit)
    A_norm, alpha_norm = params_norm

    # Absolute RMS plot
    plt.figure(figsize=(10, 6))
    plt.errorbar(N0_values_all, rms_array, yerr=rms_std_array, fmt='o', label="Monte Carlo RMS (Simulated)", color="#6a0dad", capsize=3)
    plt.loglog(N0_values_all, rms_array, 'o', color="#6a0dad")
    plt.loglog(N0_fit, power_law(N0_fit, A_abs, alpha_abs), '--',
               label=fr"Fit: RMS $\propto N_0^{{{alpha_abs:.2f}}}$ (Fit Range: $10^2 < N_0 < 10^3$)", color="black")
    plt.loglog(N0_values_all, np.sqrt(N0_values_all), ':',
               label=r"Theory: RMS $\propto \sqrt{N_0}$ (Theoretical Slope = 0.5)", color="gray")
    plt.xlabel(r"Initial Population $N_0$ (log scale)", fontsize=12)
    plt.ylabel(r"RMS Deviation (log scale)", fontsize=12)
    plt.title(r"Absolute RMS vs $N_0$", fontsize=14)
    plt.grid(True, which="both", linestyle='--', alpha=0.6)
    plt.legend(fontsize=10, loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'rms_vs_N0_absolute.png'), dpi=300)
    plt.show()

    # Normalized RMS plot
    plt.figure(figsize=(10, 6))
    plt.errorbar(N0_values_all, rms_norm_array, yerr=rms_norm_std_array, fmt='s',
                 label=r"Normalized RMS (RMS$/\sqrt{N_0}$, Simulated)", color="#00796B", capsize=3)
    plt.loglog(N0_values_all, rms_norm_array, 's', color="#00796B")
    plt.loglog(N0_fit, power_law(N0_fit, A_norm, alpha_norm), '--',
               label=fr"Fit: RMS$/\sqrt{{N_0}} \propto N_0^{{{alpha_norm:.2f}}}$ (Fit Range: $10^2 < N_0 < 10^3$)", color="black")
    plt.axhline(np.mean(rms_norm_array), linestyle=':', color='gray',
                label=r"Theory: RMS$/\sqrt{N_0}$ (Theoretical Slope = 0.0)")
    plt.xlabel(r"Initial Population $N_0$ (log scale)", fontsize=12)
    plt.ylabel(r"Normalized RMS (log scale)", fontsize=12)
    plt.title(r"Normalized RMS vs $N_0$", fontsize=14)
    plt.grid(True, which="both", linestyle='--', alpha=0.6)
    plt.legend(fontsize=10, loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'rms_vs_N0_normalized.png'), dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
