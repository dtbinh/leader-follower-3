import pigpio

from parameters import button_debounce_delay


class ButtonPushedException(Exception):
    pass


class Button:
    """
    Waits for a button to be pressed
    """
    
    def __init__(self, pin, active_low=True):
        global raspi
        raspi.set_mode(pin, pigpio.INPUT)
        if active_low:
            raspi.set_pull_up_down(pin, pigpio.PUD_UP)
            self._cb = raspi.callback(pin, pigpio.FALLING_EDGE, self._press)
        else:
            raspi.set_pull_up_down(pin, pigpio.PUD_DOWN)
            self._cb = raspi.callback(pin, pigpio.RISING_EDGE, self._press)
        
        self._last_time = 0.0
    
    def _press(self, gpio, level, tick):
        # convert ns to s
        time = tick/1000000.0
        if time - self._last_time >= button_debounce_delay:
            self._last_time = time
            print('somebody pushed the button')
            # raise ButtonPushedException
    
    def stop(self):
        self._cb.cancel()


if __name__ == '__main__':
    from time import sleep
    
    raspi = pigpio.pi()
    btn = Button(22)
    while True:
        try:
            while True:
                sleep(10)
        except ButtonPushedException:
            print('somebody pushed the button')
        except KeyboardInterrupt:
            break
    btn.stop()
    raspi.stop()