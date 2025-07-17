import numpy as np
import matplotlib.pyplot as plt
import os

def simulate_decay(N0, lambda_decay, steps):
    """
    Simulates radioactive decay using discrete Monte Carlo method.

    Returns:
    - Array of undecayed particles at each timestep.
    """
    decay_monte_carlo = np.zeros(steps)
    N = N0
    for t in range(steps):
        decayed = np.sum(np.random.rand(N) < lambda_decay)
        N -= decayed
        decay_monte_carlo[t] = N
    return decay_monte_carlo

def theoretical_decay(N0, lambda_decay, steps):
    """
    Computes theoretical decay using exponential model.

    Returns:
    - Array of expected undecayed particles at each timestep.
    """
    lambda_eff = -np.log(1 - lambda_decay)
    t = np.arange(steps)
    return N0 * np.exp(-lambda_eff * t)

# This block only runs if the file is executed directly
if __name__ == "__main__":
    # Set up paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    plots_dir = os.path.join(os.path.dirname(current_dir), 'plots')
    os.makedirs(plots_dir, exist_ok=True)

    # Initial conditions
    N0 = 1000
    lambda_decay = 0.1
    steps = 100

    # Run Simulation
    decay_monte_carlo = simulate_decay(N0, lambda_decay, steps)
    decay_theoretical = theoretical_decay(N0, lambda_decay, steps)
    t = np.arange(steps)

    # Create the plot
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(t, decay_monte_carlo, label=f'Monte Carlo (λ={lambda_decay})', color='green', marker='o', markersize=3)
        ax.plot(t, decay_theoretical, label='Theoretical Decay', color='red', linestyle='--')

        ax.set_xlabel('Time Step')
        ax.set_ylabel('Number of Undecayed Particles')
        ax.set_title(f'Radioactive Decay: Simulation vs Theoretical')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()

        plot_path = os.path.join(plots_dir, 'decay_simulation.png')
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        print(f'✅ Plot saved to: {plot_path}')

        plt.show()
    except Exception as e:
        print(f'❌ Error creating/saving plot: {str(e)}')
