from math import pi

# ------------------------------ parameters ------------------------------
# camera stuff
pink = ((140, 100, 100), (240, 255, 255))
resolution = (640, 480)
min_obj_radius = 5

# pids
servo_pid_constants = {'kp': 0.3, 'ki': 0, 'kd': 0}
left_motor_pid_constants = {'kp': 0.00107, 'ki': 0.0180333, 'kd': 0}
right_motor_pid_constants = {'kp': 0.00102, 'ki': 0.0178333, 'kd': 0}
forward_pid_constants = {'kp': 3, 'ki': 0, 'kd': 3}
angle_pid_constants = {'kp': 2, 'ki': 0, 'kd': 1}

target_dist_offset = 600
small_angle = pi/36
nav_timer_interval = 0.01
accel_limit = 0.01

button_delay = 0.3

# ------------------------------ constants ------------------------------
# pins
servo_pin = 25
left_pins = {'pwm': 6, 'dir': 5, 'a': 17, 'b': 27}
right_pins = {'pwm': 26, 'dir': 13, 'a': 23, 'b': 18}

frame_rates = {(320, 240): 33, (640, 480): 12, (1280, 720): 5, (1920, 1080): 2}
frame_rate = frame_rates[resolution]
servo_speed = 1.67
max_move = 2*pi/servo_speed/frame_rate

# converts 10 bit adc to current in amps
current_coefficient = 0.0488
current_time_limit = 500

# also equal to the pos_dif per rev
encoder_edges_per_rev = 192.0

# robot dimensions
# all distances in mm and angles in radians
wheel_radius = 50.0  # 42
wheel_circumference = wheel_radius*2.0*pi
distance_ratio = wheel_circumference/encoder_edges_per_rev
distance_between_wheels = 400.0
max_wheel_vel = 16.0*wheel_circumference

# y distance from center of wheels to center of camera servo
camera_y_offset = 30
# distance from center of camera servo to camera sensor
camera_dist_offset = 10

motor_pwm_range = 40000
