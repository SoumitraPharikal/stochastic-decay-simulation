import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Add these utility functions
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

# Setup output directory
save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plots')
os.makedirs(save_dir, exist_ok=True)

# Parameters
print("Creating animation...")
N0_anim = 200
lambda_decay = 0.1
steps = 75

# Data
theory = analytical_decay(N0_anim, lambda_decay, steps)
sim = simulate_decay(N0_anim, lambda_decay, steps)
time = np.arange(steps)

# Setup plot
fig, ax = plt.subplots(figsize=(8, 5))
sim_line, = ax.plot([], [], 'o-', label="Simulation")
theory_line, = ax.plot(time, theory, '--', label="Theory", color='black')

ax.set_xlim(0, steps)
ax.set_ylim(0, N0_anim)
ax.set_xlabel("Time Step")
ax.set_ylabel("Number of Particles")
ax.set_title("Decay Process Simulation")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

def update(frame):
    sim_line.set_data(time[:frame+1], sim[:frame+1])
    return sim_line,

ani = FuncAnimation(fig, update, frames=steps, interval=200, repeat=False)

# Save as GIF
gif_writer = PillowWriter(fps=5)
ani.save(os.path.join(save_dir, "decay_simulation.gif"), writer=gif_writer)
