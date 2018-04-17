from math import pi

# all lengths in mm and angles in radians
# --------------------------------------------------------------
# --------------------- parameters -----------------------------
# --------------------------------------------------------------

motor_vel_smoothing_factors = (0.01, 0.9, 0.9)
ball_speed_smoothing_factors = (20.0, 0.9, 0.9)
ball_heading_smoothing_factors = (20.0, 0.9, 0.9)

# ----- camera stuff -----
pink = ((158, 114, 19), (170, 255, 236))
awb_gains = (1.0, 1.8)
resolution = (320, 240)
min_obj_radius = 8

# ----- pids -----
servo_pid_constants = {
    'kp': 0.1,
    'ki': 0,
    'kd': 0,
    'dead_band': 0.05
}
left_motor_pid_constants = {
    'kp': 0.00110,
    'ki': 1.78333,
    'kd': 0,
    # 'dead_band': 0.005
}
right_motor_pid_constants = {
    'kp': 0.00102,
    'ki': 1.78333,
    'kd': 0,
    # 'dead_band': 0.005
}
forward_pid_constants = {
    'kp': 0.2,
    'ki': 1.5,
    'kd': 0.04,
    'dead_band': 25
}
angle_pid_constants = {
    'kp': 0.5,
    'ki': 0,
    'kd': 0.05,
    'dead_band': pi/36
}
# ----- navigation -----
# the distance the vehicle will aim to stay from the ball
target_ball_dist = 600
# when estimating the vehicles movements we use a point and shoot method
# which estimates a turn as a zero-radius turn and forward movement.
# this only works if the turns are kept small so we recursively split up large
# turns into many small turns with angles less than the parameter 'small_angle'
small_angle = pi/36
# the period the navigation system is run at
nav_timer_interval = 0.01
# maximum forward speed
max_forward_speed = 500
# maximum angular speed
max_angular_speed = 2

# ----- search system -----
# number of frames with the ball missing before searching starts
count_before_search = 30
# the amount that the servo can be off from the target angle when sweeping
# and still be recognized as reaching the target
acceptable_angle_error = 0.08
# speed that the servo sweeps at when searching
# the value does not correspond to any physical speed. its just a scalar
sweep_speed = 0.2
# angular velocity that the robot spins at when in searching's spin mode
spin_speed = 1.0
# number of times the servo will sweep from one side to another before it
# switches to the robot spinning
sweeps_before_spin = 2

# ----- miscellaneous -----
# minimum time in between presses of a button
button_debounce_delay = 0.3

# --------------------------------------------------------------
# ----------------------- constants ----------------------------
# --------------------------------------------------------------

# ----- pins ------
servo_pin = 25
button_pin = 22
# pwm and dir for motor controller
# a and b for rotary encoder quadrature input
left_pins = {'pwm': 6, 'dir': 5, 'a': 17, 'b': 27}
right_pins = {'pwm': 26, 'dir': 13, 'a': 23, 'b': 18}

# ----- servo controller -----
# speed of servo in radians per second
servo_speed = 8.727
# servo angle set at 50Hz
max_servo_move = servo_speed/50

# ----- current sensor -----
current_time_limit = 500

# also equal to the pos_dif per rev
encoder_edges_per_rev = 192.0

# robot dimensions
# all distances in mm
wheel_radius = 50  # 42 for smaller wheel
wheel_circumference = wheel_radius*2.0*pi
distance_ratio = wheel_circumference/encoder_edges_per_rev
distance_between_wheels = 400.0
max_wheel_vel = 16.0*wheel_circumference

# y distance from center of wheels to center of camera servo
camera_y_offset = 0
# distance from center of camera servo to camera sensor
camera_dist_offset = 0

motor_pwm_range = 40000
