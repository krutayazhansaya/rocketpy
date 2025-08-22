from rocketpy import Environment, SolidMotor, Rocket, Flight, LiquidMotor
import datetime
import matplotlib
matplotlib.use("MacOSX")   # or "TkAgg" if MacOSX fails

import matplotlib.pyplot as plt

env = Environment(latitude=28.562106, longitude= 80.577180, elevation=3)

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 12)
)
env.set_atmospheric_model(type="Forecast", file="GFS")
env.info()
AeroTech = SolidMotor(
    thrust_source="./AeroTech_O5500X-PS.eng",
    dry_mass=7.001,  # kg  (loaded 16.78 - prop 9.779)
    dry_inertia=(1.31, 1.31, 0.0084),  # kg·m^2  (Ixx, Iyy, Izz) approximate
    nozzle_radius=0.025,  # m (example exit radius — tune if you have nozzle spec)
    throat_radius=0.012,  # m (estimate 12 mm throat radius; tune if using explicit flow model)
    grain_number=1,
    grain_density=1815,  # kg/m^3 (assumed)
    grain_outer_radius=0.049,  # m (98 mm diameter / 2)
    grain_initial_inner_radius=0.020,  # m (estimate — adjust to match prop mass)
    grain_initial_height=1.466,  # m (inside thrust ring length)
    grain_separation=0.0,  # m (single grain)
    grains_center_of_mass_position=0.733,  # m (half of 1.466 from chosen origin; change if origin differs)
    center_of_dry_mass_position=0.75,  # m  (estimate; compute from casing+grain geometry for accuracy)
    nozzle_position=0.0,
    burn_time=(0, 3.997),
    coordinate_system_orientation="nozzle_to_combustion_chamber"
)
AeroTech.info()
rocket_airframe = Rocket(
    radius=0.049,                # 98 mm diameter
    mass=4.0,                    # kg (dry airframe without motor)
    inertia=(5.3, 5.3, 0.005),   # kg·m² (Ixx, Iyy, Izz approx)
    power_off_drag="./drag_off.csv",   # placeholder drag curve
    power_on_drag="./drag_on.csv",     # placeholder drag curve
    center_of_mass_without_motor=1.0,        # m from tail (approx mid-body)
    coordinate_system_orientation="tail_to_nose"
)
rocket_airframe.add_motor(AeroTech, position=-1)
# Tail-based positions (0 m at tail)
rail_buttons = rocket_airframe.set_rail_buttons(
    upper_button_position=0.90,   # 0.90 m from tail
    lower_button_position=0.20,   # 0.20 m from tail
    angular_position=45
)
# --- Nose Cone ---
nose_cone = rocket_airframe.add_nose(
    length=0.55,               # m (≈ 5.5 calibers for 98mm)
    kind="von karman",         # aerodynamic nose shape
    position=1.50              # m from tail (adjust to rocket length)
)

# --- Fins ---
fin_set = rocket_airframe.add_trapezoidal_fins(
    n=4,
    root_chord=0.18,           # m (slightly larger than example since O-class rocket needs more stability)
    tip_chord=0.08,            # m
    span=0.12,                 # m (120 mm fin span)
    position=0.20,             # m from tail (behind rail button, ahead of nozzle)
    cant_angle=0.0,            # no spin
    airfoil=("./NACA0012_clean.csv", "radians")
)

# --- Tail Cone ---
tail = rocket_airframe.add_tail(
    top_radius=0.049,          # matches body tube radius
    bottom_radius=0.035,       # nozzle exit flare
    length=0.08,               # m
    position=0.10              # m from tail
)

# --- Recovery Parachutes ---
main = rocket_airframe.add_parachute(
    name="main",
    cd_s=10.0,                 # effective drag area [m²]
    trigger=300,               # deploy at 800 m altitude
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5)
)

drogue = rocket_airframe.add_parachute(
    name="drogue",
    cd_s=1.0,
    trigger="apogee",          # deploy at apogee
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5)
)

# --- Stability Analysis ---
rocket_airframe.plots.static_margin()
rocket_airframe.all_info()
test_flight = Flight(
    rocket=rocket_airframe,
    environment=env,
    rail_length=5.2,          # in meters (your rail length)
    inclination=85,           # degrees (almost vertical)
    heading=0                 # azimuth, 0° = North
)
test_flight.prints.initial_conditions()
test_flight.prints.surface_wind_conditions()
test_flight.prints.launch_rail_conditions()
test_flight.prints.out_of_rail_conditions()
test_flight.prints.burn_out_conditions()
test_flight.prints.apogee_conditions()
test_flight.prints.events_registered()
test_flight.prints.impact_conditions()
test_flight.prints.maximum_values()
test_flight.plots.trajectory_3d()
plt.show()
test_flight.plots.linear_kinematics_data()
test_flight.plots.flight_path_angle_data()
test_flight.plots.attitude_data()
test_flight.plots.angular_kinematics_data()
test_flight.plots.aerodynamic_forces()
test_flight.plots.rail_buttons_forces()
test_flight.plots.energy_data()
test_flight.plots.fluid_mechanics_data()
test_flight.plots.stability_and_control_data()





