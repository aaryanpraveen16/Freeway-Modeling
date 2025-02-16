# 🚗 Freeway Simulation

This web application simulates **traffic flow dynamics**, where multiple cars adjust their speeds to maintain safe distances. Users can **input custom parameters** (reaction time, deceleration, speed sensitivity) and visualize the effects in real-time.



## **🌟 Features**
- 🌊 **Real-time visualization** of speed and position of cars.
- 🎧 **User-adjustable parameters** for fine-tuning traffic behavior.
- 🇮 **Gradual braking & acceleration** modeled using physics-based equations.
- 🌐 **Runs in a web browser** using **Streamlit**.



## **🚀 Getting Started**

### **🔧 Installation**
Ensure you have **Python 3.7+** installed. Then install the dependencies:

```sh
pip install streamlit numpy matplotlib
```

### **▶ Running the Web App**
To start the simulation, run:

```sh
streamlit run freeway.py
```

This will open the app in your **browser** at `http://localhost:8501`.



## **⚙ How to Use**
1. **Adjust Parameters:**
   - 🏆 **Number of Cars**: Choose how many cars to simulate.
   - ⏳ **Time Steps**: Increase for longer simulations.
   - ⏱ **Reaction Time (t_r)**: Defines driver reaction delay.
   - 🚑 **Max Deceleration (a_max)**: Determines braking power.
   - 🔹 **Initial Gap**: Distance between cars at the start.
   - ⚙ **Speed Sensitivity (k)**: How fast cars adjust speed.

2. **Click "Run Simulation"** to generate traffic graphs.

3. **View Graphs**:
   - 📈 **Speed vs. Time**: Shows how car speeds evolve over time.
   - 📉 **Position vs. Time**: Tracks movement along the road.



## **🔬 How the Simulation Works**
1. **Cars start at fixed intervals behind each other.**
2. If a car is **too close**, it slows down to maintain **a safe distance**.
3. If a car is **far behind**, it speeds up smoothly to match the lead car.
4. The **lead car may decelerate** (simulating traffic congestion).
5. The **kinematic equation** is used for realistic braking:

   $$
   a_{\text{required}} = \frac{v_{\text{trailing}}^2 - v_{\text{lead}}^2}{2 \cdot (h_{\text{safe}} - h_{\text{current}})}
   $$

6. **Graph visualizations** track speed & position over time.



## **🐟 License**
This project is **open-source** under the **MIT License**.



## **💬 Contact**
📧 Email: [aaryan.praveen@gmail.com](mailto:aaryan.praveen@gmail.com)
