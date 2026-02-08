import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def run_suspension_simulation():
    # --- 1. System Parameters (Luxury Sedan Configuration) ---
    m = 450.0    # Sprung Mass (kg)
    k = 28000.0  # Spring Stiffness (N/m)
    c = 2500.0   # Damping Coefficient (Ns/m)

    # --- 2. Mathematical Derivations ---
    # Natural Frequency: omega_n = sqrt(k/m)
    omega_n = np.sqrt(k/m)
    # Damping Ratio: zeta = c / (2 * sqrt(m * k))
    zeta = c / (2 * np.sqrt(m * k))
    
    print(f"--- System Characteristics ---")
    print(f"Natural Frequency (omega_n): {omega_n:.2f} rad/s")
    print(f"Damping Ratio (zeta): {zeta:.3f} (Underdamped)")

    # --- 3. Define Transfer Function ---
    # H(s) = (omega_n^2) / (s^2 + 2*zeta*omega_n*s + omega_n^2)
    num = [omega_n**2]
    den = [1, 2 * zeta * omega_n, omega_n**2]
    sys = signal.TransferFunction(num, den)

    # --- 4. Time Domain Analysis (Step Response) ---
    t = np.linspace(0, 5, 1000)
    t, y = signal.step(sys, T=t)

    # --- 5. Frequency Domain Analysis (Bode Plot) ---
    w, mag, phase = signal.bode(sys)

    # --- 6. Visualization ---
    plt.figure(figsize=(12, 8))

    # Plot 1: Step Response (Curb Impact)
    plt.subplot(2, 1, 1)
    plt.plot(t, y, 'b', lw=2, label=f'zeta = {zeta:.2f}')
    plt.axhline(y=1.0, color='r', linestyle='--', label='Steady State')
    plt.title('Quarter-Car Step Response (Curb Impact Simulation)')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Displacement')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.7)

    # Plot 2: Bode Magnitude (Resonance Analysis)
    plt.subplot(2, 1, 2)
    plt.semilogx(w, mag, 'forestgreen', lw=2)
    plt.title('Frequency Response (Bode Magnitude)')
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True, which='both', linestyle='--', alpha=0.7)

    plt.tight_layout()
    
    # Save the figure for GitHub README
    plt.savefig('suspension_results.png', dpi=300)
    print("\nSimulation complete. Plot saved as 'suspension_results.png'")
    plt.show()

if __name__ == "__main__":
    run_suspension_simulation()