import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# === Setup ===
grid_height, grid_width = 30, 50
center_x, center_y = grid_width // 2, grid_height // 2
a, b = center_x, center_y
y, x = np.ogrid[:grid_height, :grid_width]
oval_mask = ((x - center_x) / a) ** 2 + ((y - center_y) / b) ** 2 <= 1

# Load and resize map image
background = Image.open("C:/Users/Owner/OneDrive/Personal/Portfolio/edc-vegas-2023-map-1024x1282.jpeg")
background = background.resize((grid_width, grid_height))

# Output folder
os.makedirs("output", exist_ok=True)

# === Time Blocks and Zone Evolution ===
time_blocks = {
    "T1": {  # Early entry
        "cosmic": 3.5, "circuit": 2.0, "kinetic": 1.5, "basspod": 1.0, "water": 2.5, "surge": False
    },
    "T2": {  # Main crowd building
        "cosmic": 4.5, "circuit": 4.0, "kinetic": 3.5, "basspod": 2.5, "water": 3.0, "surge": False
    },
    "T3": {  # Peak density
        "cosmic": 5.0, "circuit": 5.5, "kinetic": 6.0, "basspod": 4.0, "water": 4.5, "surge": False
    },
    "T4": {  # Circuit Grounds ends, surge to Kinetic
        "cosmic": 3.0, "circuit": 2.0, "kinetic": 7.0, "basspod": 3.0, "water": 5.0, "surge": True
    },
    "T5": {  # Late night, fatigue
        "cosmic": 1.5, "circuit": 1.0, "kinetic": 4.0, "basspod": 2.0, "water": 3.0, "surge": False
    },
    "T6": {  # Closing time, exit buildup
        "cosmic": 0.5, "circuit": 0.3, "kinetic": 2.5, "basspod": 1.0, "water": 2.0, "surge": False
    }
}

# === Grid Cell Indexes for Zones ===
zones = {
    "kinetic": (slice(2,10), slice(25,45)),
    "circuit": (slice(18,28), slice(35,49)),
    "cosmic": (slice(5,12), slice(0,15)),
    "basspod": (slice(12,20), slice(30,38)),
    "water": (slice(10,14), slice(18,22)),
}

# === Loop Through Time Blocks ===
for t, settings in time_blocks.items():
    crowd_density = np.zeros((grid_height, grid_width))

    # Assign evolving densities
    for zone, sl in zones.items():
        crowd_density[sl] = settings[zone]
    
    # Cap density at 7
    crowd_density[crowd_density > 7.0] = 7.0

    # Apply oval mask
    masked_density = np.where(oval_mask, crowd_density, np.nan)

    # Turbulence risk calculation
    turbulence_risk = np.zeros_like(crowd_density)
    turbulence_risk[crowd_density > 5.5] = 1
    turbulence_risk[(crowd_density > 3) & (crowd_density <= 5.5)] = 0.5
    masked_risk = np.where(oval_mask, turbulence_risk, np.nan)

    # === Plot & Save Density Map ===
    plt.imshow(background, extent=[0, grid_width, grid_height, 0])
    plt.imshow(masked_density, cmap='hot', alpha=0.6, interpolation='nearest', extent=[0, grid_width, grid_height, 0])
    plt.title(f"EDC Density Map – {t}")
    plt.xlabel("East-West")
    plt.ylabel("North-South")
    plt.colorbar(label="Density (people/m²)")
    plt.tight_layout()
    plt.savefig(f"output/density_{t}.png")
    plt.close()

    # === Plot & Save Risk Map ===
    plt.imshow(background, extent=[0, grid_width, grid_height, 0])
    plt.imshow(masked_risk, cmap='Reds', alpha=0.6, interpolation='nearest', extent=[0, grid_width, grid_height, 0])
    plt.title(f"Turbulence Risk – {t}")
    plt.xlabel("East-West")
    plt.ylabel("North-South")
    plt.colorbar(label="Risk Level")
    
    # Plot surge vector for T4
    if settings["surge"]:
        from_y, from_x = 23, 42
        to_y, to_x = 6, 35
        u_surge = to_x - from_x
        v_surge = to_y - from_y
        plt.quiver(from_x, from_y, u_surge, v_surge, angles='xy', scale_units='xy', scale=1,
                   color='magenta', width=0.02, label='Surge Flow')
        plt.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig(f"output/risk_{t}.png")
    plt.close()

print("✅ Simulation complete. All images saved to /output folder.")
