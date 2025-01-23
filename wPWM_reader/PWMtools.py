from machine import(
    Pin,
    PWM,
)
from time import(
    time,
    time_ns
)

def _sample_avg(
        sample: list 
        ):
    
    if type(sample) is not list: raise ValueError

    filtered_sample = []
    for i in range(1, (len(sample) - 1)): filtered_sample.append(sample[i])

    _total = sum(filtered_sample)

    average = (round((_total/len(filtered_sample))))
    return average


def read_signal(
    pin: int,
    accuracy_padding: int = 1000000,
    ) -> int:
    
    '''
    !!!
    '''

    # pwm_pin = Pin(6, Pin.OUT)
    # pulse = PWM(pwm_pin)
    # pulse.init(freq=10, duty_u16=0, duty_ns=10000)
    # pulse.duty_u16(1000)

    reader_pin = Pin(pin, Pin.IN, Pin.PULL_DOWN)
    accuracy_padding = (10**accuracy_padding)
    samples: list = []
    timer = 0
    timer_start = time()
    while timer <= 1:
        if reader_pin.value() == 1:
            starting_time = time_ns()
            while True:
                if reader_pin.value() == 0:
                    ending_time = time_ns()
                    break
                else:
                    pass
            samples.append((ending_time-starting_time)/accuracy_padding)
            # break
        else:
            pass
        timer_end = time()
        timer = timer_end - timer_start

    signal_ = _sample_avg(samples)
    return(signal_)

def generate_PWM_object(
    pin: int,
    ) -> PWM | None:
    
    '''
    !!!
    '''
    
    return PWM(Pin(pin, Pin.OUT), freq=100, duty_ns=100)