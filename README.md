# Versus Project

Welcome to the Versus Project! This project is designed to control our VEX V5 robot using Python during versus. The main code for the robot is located in the `src/main.py` file.

## Project Structure

- `.vscode/`: Contains Visual Studio Code settings and extensions for the project.
- `src/`: Contains the main Python code for the robot.
  - `main.py`: The main code file for the robot.

## Main Code Overview

The `src/main.py` file contains the main code for controlling our bot. Below is an overview of the key functions and their purposes:

### Drive Function

- **Drive()**: Controls the robot's movement using arcade-style controls with two sticks.

### Event Handlers

- **ondriver_drivercontrol_0()**: Handles driver control during the competition.
- **when_started2()**: Toggles drive inversion using the controller's right button.
- **when_started3()**: Toggles the mogo mechanism using the controller's A button.
- **when_started5()**: Toggles the corner cleaner using the controller's Y button.
- **when_started4()**: Sets the intake motor's velocity and brake mode.
- **onevent_controller_1buttonB_pressed_0()**: Controls the intake motor in reverse when the B button is pressed.
- **onevent_controller_1buttonL1_pressed_0()**: Spins the intake motor forward when the L1 button is pressed.
- **onevent_controller_1buttonL2_pressed_0()**: Spins the intake motor backward when the L2 button is pressed.
- **onevent_controller_1buttonR2_pressed_0()**: Spins the ladybrown motor forward when the R2 button is pressed.
- **onevent_controller_1buttonR1_pressed_0()**: Spins the ladybrown motor backward when the R1 button is pressed.

### PID Controllers

- **Turn(turnDesired, tolerance=0.2)**: A PID controller for turning the robot to a desired angle.
- **forward(mm, V=60)**: A PID controller for keeping the bot straight while driving forward a specified distance in millimeters.

### Autonomous

- **onauton_autonomous_0()**: The autonomous routine for the robot.

## Getting Started

To get started with this project, open the `src/main.py` file in Visual Studio Code and ensure you have the recommended Python extension installed. You can then run and debug the code using the VEX V5 robot.
