# rocketpy

# 🚀 Rocket Flight Simulation with RocketPy

This repository contains a complete **rocket flight simulation** project built using [RocketPy](https://rocketpy.org/).  
It models a high-power solid motor rocket, including the motor, airframe, fins, nose cone, tail, and recovery system, and generates detailed plots of stability, kinematics, aerodynamics, and trajectory.

---

## 📂 Project Structure

RocketPy
├── main.py # Main simulation script
├── AeroTech_O5500X-PS.eng # Motor thrust curve file
├── drag_off.csv # Drag curve (power off)
├── drag_on.csv # Drag curve (power on)
├── NACA0012_clean.csv # Airfoil lift coefficient data
├── requirements.txt # Dependencies (full environment)
└── README.md # Project documentation
## 📊 Results

This simulation models the complete flight of a high-power solid rocket and generates a wide range of outputs:

- **Stability Analysis**  
  - Static margin plots showing how the rocket’s stability evolves during flight.  
  - Center of Mass (CoM) and Center of Pressure (CoP) tracking for safe design.  

- **3D Flight Trajectory**  
  - Full visualization of the rocket’s ascent, apogee, and descent.  
  - Prediction of landing location based on weather conditions (GFS forecast).  

- **Flight Events Timeline**  
  - Out of rail (rocket leaving the guide rail)  
  - Motor burnout (~4 seconds after ignition)  
  - Apogee (maximum altitude)  
  - Drogue parachute deployment at apogee  
  - Main parachute deployment at 300 m altitude  
  - Impact and landing velocity  

- **Kinematics & Dynamics**  
  - Altitude, velocity, and acceleration over time  
  - Angular motion (pitch, yaw, roll)  
  - Aerodynamic forces (lift, drag, thrust)  
  - Flight path angle variations  

- **Energy Analysis**  
  - Evolution of kinetic and potential energy throughout flight  
  - Verification of total energy conservation and efficiency  

- **Atmospheric & Wind Effects**  
  - Incorporation of real forecast weather data (GFS model)  
  - Analysis of how wind and atmospheric density affect trajectory and landing point  

---

 ✅ Key Insights
This project demonstrates how to:
- Simulate a complete rocket mission from liftoff to recovery  
- Evaluate aerodynamic stability and flight performance  
- Vis
