
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
Left_motor_in = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
Left_motor_mogo = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
Left = MotorGroup(Left_motor_in, Left_motor_mogo)
Right_motor_in = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
Right_motor_mogo = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
Right = MotorGroup(Right_motor_in, Right_motor_mogo)
controller_1 = Controller(PRIMARY)
mogo = DigitalOut(brain.three_wire_port.a)
cc = DigitalOut(brain.three_wire_port.c)
intake_motor_a = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
intake_motor_b = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
intake_motor_c = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
intake = MotorGroup(intake_motor_a, intake_motor_b, intake_motor_c)
Lb = Motor(Ports.PORT11 ,GearSetting.RATIO_18_1, False)
inertial = Inertial(Ports.PORT19)
ai_vision = AiVision(Ports.PORT5, AiVision.ALL_AIOBJS)
class GameElements:
    MOBILE_GOAL = 0
    RED_RING = 1
blue_ring = Colordesc(1, 28, 64, 107, 40, 0.2)
ai_vision = AiVision(Ports.PORT4, AiVision.ALL_AIOBJS, blue_ring)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))

# Set random seed 
initializeRandomSeed()

def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

#####################
#   Drive function  #
#####################

invert = False
Intake = False
vexcode_ai_vision_5_object_index = 0
vexcode_ai_vision_5_objects = []

def Drive():
    # drive function using arcade with two sticks
    if invert:
        # front = mogo
        Left.set_velocity((-1 * controller_1.axis3.position() + controller_1.axis1.position()), PERCENT)
        Right.set_velocity((-1 * controller_1.axis3.position() - controller_1.axis1.position()), PERCENT)
        Left.spin(FORWARD)
        Right.spin(FORWARD)
    else:
        # front = intake
        Left.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()), PERCENT)
        Right.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()), PERCENT)
        Left.spin(FORWARD)
        Right.spin(FORWARD)

def ondriver_drivercontrol_0():
    while True:
        Drive()
        wait(5, MSEC)

#   drive invertion toggle  #
def when_started2():
    global invert
    invert = False
    while True:
        while not controller_1.buttonRight.pressing():
            wait(5, MSEC)
        invert = True
        while controller_1.buttonRight.pressing():
            wait(5, MSEC)
        while not controller_1.buttonRight.pressing():
            wait(5, MSEC)
        invert = False
        while controller_1.buttonRight.pressing():
            wait(5, MSEC)
        wait(5, MSEC)

#   toggle mogo mech    #
def when_started3():
    while True:
        while not controller_1.buttonA.pressing():
            wait(5, MSEC)
        mogo.set(True)
        while controller_1.buttonA.pressing():
            wait(5, MSEC)
        while not controller_1.buttonA.pressing():
            wait(5, MSEC)
        mogo.set(False)
        while controller_1.buttonA.pressing():
            wait(5, MSEC)
        wait(5, MSEC)

#   toggle corner cleaner (CC)  #
def when_started5():
    while True:
        while not controller_1.buttonY.pressing():
            wait(5, MSEC)
        cc.set(True)
        while controller_1.buttonY.pressing():
            wait(5, MSEC)
        while not controller_1.buttonY.pressing():
            wait(5, MSEC)
        cc.set(False)
        while controller_1.buttonY.pressing():
            wait(5, MSEC)
        wait(5, MSEC)

#   set intake velocity and brake   #
def when_started4():
    intake.set_velocity(120, RPM)
    intake.set_stopping(BRAKE)

#   enable intake on B reverse on hold   #
def onevent_controller_1buttonB_pressed_0():
    while controller_1.buttonB.pressing():
        intake.spin(REVERSE)
    intake.spin(FORWARD)

#   spin intake forward on L1   #
def onevent_controller_1buttonL1_pressed_0():
    global Intake
    Intake = True
    intake.spin(FORWARD)
    while controller_1.buttonL1.pressing():
        wait(5, MSEC)
    intake.stop()
    Intake = False

#   spin intake backwards on L2   #
def onevent_controller_1buttonL2_pressed_0():
    global Intake
    Intake = True
    intake.spin(REVERSE)
    while controller_1.buttonL2.pressing():
        wait(5, MSEC)
    intake.stop()
    Intake = False

#   toggle ladybrown to next position  #
def when_started6():
    Lb.set_velocity(30, PERCENT)
    Lb.set_max_torque(100, PERCENT)
    while True:
        while not controller_1.buttonR1.pressing():
            wait(50, MSEC)
        Lb.spin_to_position(120, DEGREES)
        while not controller_1.buttonR1.pressing():
            wait(50, MSEC)
        Lb.spin_to_position(380, DEGREES)
        while not controller_1.buttonR1.pressing():
            wait(50, MSEC)
        Lb.spin_to_position(0, DEGREES)

#   spin ladybrown forwards on R2   #
def onevent_controller_1buttonUp_pressed_0():
    Lb.spin(FORWARD, 20, PERCENT)
    while controller_1.buttonUp.pressing():
        wait(5, MSEC)
    Lb.stop(HOLD)

#   spin ladybrown backwards on R1   #
def onevent_controller_1buttonDown_pressed_0():
    Lb.spin(REVERSE, 20, PERCENT)
    while controller_1.buttonDown.pressing():
        wait(5, MSEC)
    Lb.stop(HOLD)

#   colorsorter   #
def when_started7():
    while True:
        rings = ai_vision.take_snapshot(blue_ring)
        if rings and ai_vision.object_count() > 0 and rings[0].width > 50:
            wait(0.42, SECONDS)
            intake.stop()
            wait(200)
            intake.spin(FORWARD)
        wait(5, MSEC)

#   stakelock   #
def when_started8():
    while True:
        if controller_1.buttonY.pressing():
            if vexcode_ai_vision_5_objects[vexcode_ai_vision_5_object_index].id == GameElements.MOBILE_GOAL:
                Turn(vexcode_ai_vision_5_objects[vexcode_ai_vision_5_object_index].angle)
                wait(1, SECONDS)
        wait(5, MSEC)

#########################
#   PID controllers     #
#########################

KP =0.65
KI =0.03
KD =0.5

def Turn(turnDesired, tolerance=0.2):                                                                           # a self made PID to turn, parameters turnDesired and tolerance are given in the function
    inertial.reset_rotation()                                                                                   # resets the inertial sensor to 0
    turnPrevError = 0                                                                                           # \
    turnTotalError = 0                                                                                          #  } declares variables for the PID
    t = 0                                                                                                       # /
    while abs(turnDesired + inertial.rotation()) > tolerance:                                                   # repeats the PID until the given angle is reached   
        t += 1                                                                                                  # counts iterrations for feedback
        turnError = turnDesired + inertial.rotation()                                                           # calculates the error
        turnDerivative = turnError - turnPrevError                                                              # calculates the derivative
        turn = turnError * KP + turnDerivative * KD + turnTotalError * KI                                       # The total value in percentage as motor input
        turnPrevError = turnError                                                                               # sets the previous error to the current error
        turnTotalError += turnError                                                                             # adds the current error to the total error
        if turnTotalError > 100:                                                                                #  } clamping on positive values to prevent buildup above 100%
            turnTotalError = 100                                                                                # /
        elif turnTotalError < -100:                                                                             #  } clamping on negative values to prevent buildup below -100%
            turnTotalError = -100                                                                               # /
        Right.spin(FORWARD, -turn, PERCENT)                                                                     #  } starts the motors and set the speed to turn
        Left.spin(FORWARD, turn, PERCENT)                                                                       # /
        
        wait(50)                                                                                                # waits to lighten the program
        print(inertial.rotation(), "\t", turnError, "\t", turnDerivative, "\t", turnTotalError, "\t",t*50)      # prints feedback used to tune the PID
    
    Right.stop(HOLD)                                                                                            #  } stops motors using hold brakestyle
    Left.stop(HOLD)                                                                                             # /

    """wait(1000)                                                                                               # used in debuging to see the final angle
    print(inertial.rotation(), "\t", turnError, "\t", turnDerivative, "\t", turnTotalError, "\t",t*50)
"""

KFP = KP
KFI = 0
KFD = 0

def forward(mm, V=60):                                                                                          # a function to drive forward, parameters mm as distance in milimeters and V as velocity are given in the function
    deg = mm*(360/320)                                                                                          # converts the distance to degrees of the motors
    inertial.reset_rotation()                                                                                   # resets the inertial sensor to 0
    Right.reset_position()                                                                                      # resets the motor position to 0
    forwardPrevError = 0                                                                                        # \
    forwardTotalError = 0                                                                                       #  } declares variables for the PID
    while abs(Right.position()) < deg:                                                                               # repeats the loop until the distance is reached
        forwardError = inertial.rotation()                                                                      # calculates the error
        forwardDerivative = forwardError - forwardPrevError                                                     # calculates the derivative
        correct = forwardError * KFP + forwardDerivative * KFD + forwardTotalError * KFI                        # The total value in percentage as motor input
        forwardPrevError = forwardError                                                                         # sets the previous error to the current error
        forwardTotalError += forwardError                                                                       # adds the current error to the total error
        if forwardTotalError > 75:                                                                             #  } clamping on positive values to prevent buildup above 100%
            forwardTotalError = 75                                                                             # /
        elif forwardTotalError < -75:                                                                          #  } clamping on negative values to prevent buildup below -100%
            forwardTotalError = -75                                                                            # /
        Right.spin(FORWARD, V - correct, PERCENT)                                                               #  } spins the motors using the computed degrees and set the speed to V with correction
        Left.spin(FORWARD, V + correct, PERCENT)                                                                # /
        wait(20)                                                                                                # waits to lighten the program 
    Right.stop(HOLD)                                                                                            #  } stops motors using hold brakestyle
    Left.stop(HOLD)                                                                                             # /

#################
#   Autonomous  #
#################

def onauton_autonomous_0():
    intake.spin_for(REVERSE, 100, DEGREES, wait=False)
    forward(700, -75)
    mogo.set(True)
    Turn(-65)
    intake.spin(FORWARD)
    forward(600)
    Turn(60)
    cc.set(True)
    forward(900)
    Turn(90)
    cc.set(False)
    intake.stop()

def when_started1():
    inertial.calibrate()
    inertial.set_turn_type(LEFT)

#####################
#       END         #
#####################

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()

# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# system event handlers
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)
controller_1.buttonB.pressed(onevent_controller_1buttonB_pressed_0)
controller_1.buttonUp.pressed(onevent_controller_1buttonUp_pressed_0)
controller_1.buttonDown.pressed(onevent_controller_1buttonDown_pressed_0)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
ws4 = Thread( when_started4 )
ws5 = Thread( when_started5 )
ws6 = Thread( when_started6 )
ws7 = Thread( when_started7 )
ws8 = Thread( when_started8 )

when_started1()
