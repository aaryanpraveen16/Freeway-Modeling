import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Simulation Function
def compute_safe_distance(v_trailing):
    return 3 * v_trailing  # 3-second rule

def simulate_traffic(num_cars, time_steps, dt, a_max, k, initial_gap):
    v = np.full((num_cars, time_steps), 20.0)
    x = np.zeros((num_cars, time_steps))
    h = np.full((num_cars - 1, time_steps), 50.0)

    for i in range(num_cars):
        x[i, 0] = (num_cars - 1 - i) * initial_gap

    for t in range(1, time_steps):
        if t >= 50 and v[0, t-1] > 2.0:
            v[0, t] = max(v[0, t-1] - 0.2, 2.0)
        else:
            v[0, t] = v[0, t-1]
        x[0, t] = x[0, t-1] + v[0, t] * dt

        for i in range(1, num_cars):
            h_current = x[i-1, t-1] - x[i, t-1]
            h_safe = compute_safe_distance(v[i, t-1])

            if h_current < h_safe:
                a_required = (v[i, t-1] ** 2 - v[i-1, t-1] ** 2) / (2 * max(h_safe - h_current,1))
                # print(a_required)
                print("Type of a_required:", type(a_required))
                print("Shape of a_required:", np.shape(a_required))  # This will show if it's an array
                if a_required == 0:
                    v[i, t] = max(v[i, t-1] - a_max * dt, 0)
                else:
                    v[i, t] = max(v[i, t-1] - min(a_required, a_max) * dt, 0)
            else:
                v[i, t] = v[i, t-1] + k * (v[i-1, t-1] - v[i, t-1]) * dt

            x[i, t] = x[i, t-1] + v[i, t] * dt
            h[i-1, t] = x[i-1, t] - x[i, t]

    return v, x

# Web App Interface
st.title("Freeway Simulation")

num_cars = st.slider("Number of Cars", 2, 10, 5)
time_steps = st.slider("Time Steps", 100, 500, 200)
dt = st.slider("Time Step (seconds)", 0.05, 0.5, 0.1)
# t_r = st.slider("Reaction Time (seconds)", 0.5, 3.0, 1.5)
a_max = st.slider("Max Deceleration (m/s²)", 1.0, 10.0, 4.5)
k = st.slider("Speed Adjustment Sensitivity", 0.1, 1.0, 0.5)
initial_gap = st.slider("Initial Gap", 10, 60, 200)

if st.button("Run Simulation"):
    v, x = simulate_traffic(num_cars, time_steps, dt, a_max, k, initial_gap)
    
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))
    time = np.arange(time_steps) * dt

    for i in range(num_cars):
        ax[0].plot(time, v[i], label=f'Car {i+1}')
    ax[0].set_xlabel("Time (s)")
    ax[0].set_ylabel("Speed (m/s)")
    ax[0].set_title("Speed of Cars Over Time")
    ax[0].legend()
    ax[0].grid()

    for i in range(num_cars):
        ax[1].plot(time, x[i], label=f'Car {i+1}')
    ax[1].set_xlabel("Time (s)")
    ax[1].set_ylabel("Position (m)")
    ax[1].set_title("Position of Cars Over Time")
    ax[1].legend()
    ax[1].grid()

    st.pyplot(fig)

