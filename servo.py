import pigpio


class Servo:
    """
    implements the hardware parts of controlling a servo (converting angle to
    pwm)
    """
    
    def __init__(self, pi, pin, left_limit, right_limit):
        self.pi = pi
        self.pin = pin
        
        if right_limit >= left_limit:
            raise Exception('right_limit >= left_limit')
        
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.start_angle = (left_limit + right_limit) / 2
        
        self.pi.set_mode(pin, pigpio.OUTPUT)
        
        self.move_to(self.start_angle)
    
    def move_to(self, angle):
        pulse_width = 500 + 2000 * (angle - self.right_limit) / (
                self.left_limit - self.right_limit)
        self.pi.set_servo_pulsewidth(self.pin, pulse_width)
    
    def stop(self):
        self.move_to(self.start_angle)


if __name__ == "__main__":
    import time
    
    pi = pigpio.pi()
    servo = Servo(pi, 18, 180, 0)
    time.sleep(1)
    for a in range(0, 180, 5):
        servo.move_to(a)
        time.sleep(0.05)
    
    servo.stop()
    pi.stop()
