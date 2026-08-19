# 3DOF stewart platform aka motion simulator

To be able to run the simulation, you need the following installed - 
# MATLAB
- MATLAB (with Simulink)
- Simscape Multibody Library
- Instrument Control Toolbox Library

and the python libraries as needed.


# To run the simulator
- For keyboard input, open stewart_pl_keycontrol.slx in MATLAB Simulink.
- In a terminal window write ```python3 "absolute\path\to\sendkeytomat.py"```
- W/A/S/D for pitch and roll, slider for heave.
- For dashboard control, open stewart_pl_dbcontrol.slx in MATLAB Simulink.
- Use the knobs and the slider for control.
