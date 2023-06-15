from pyvesc import VESC
import time

# serial port that VESC is connected to. Something like "COM3" for windows and as below for linux/mac
serial_port = '/dev/ttyACM0'


# a function to show how to use the class with a with-statement
def run_motor_using_with():
    with VESC(serial_port=serial_port) as motor:
        time.sleep(1) # timer to give enough time to initialize
        print("Firmware: ", motor.get_firmware_version())

        motor.set_duty_cycle(.025)
        for i in range(10):
            time.sleep(0.1)
            measurements = motor.get_measurements()
            if measurements is not None:
                print(measurements.rpm)

        motor.set_duty_cycle(.045)
        # run motor and print out rpm for ~2 seconds
        for i in range(10):
            time.sleep(0.1)
            measurements = motor.get_measurements()
            if measurements is not None:
                print(measurements.rpm)

        motor.set_duty_cycle(.025)
        for i in range(10):
            time.sleep(0.1)
            measurements = motor.get_measurements()
            if measurements is not None:
                print(measurements.rpm)

        motor.set_rpm(0)
    motor.stop_heartbeat()


# a function to show how to use the class as a static object.
def run_motor_as_object():
    motor = VESC(serial_port=serial_port)
    print("Firmware: ", motor.get_firmware_version())

    # sweep servo through full range
    for i in range(100):
        time.sleep(0.01)
        motor.set_servo(i/100)

    # IMPORTANT: YOU MUST STOP THE HEARTBEAT IF IT IS RUNNING BEFORE IT GOES OUT OF SCOPE. Otherwise, it will not
    #            clean-up properly.
    motor.stop_heartbeat()


# a function to show how to use the class as a static object.
def servo_set_position(value):
    motor = VESC(serial_port=serial_port)
    print("Firmware: ", motor.get_firmware_version())

    # sweep servo through full range
    print("{}".format(value))
    
    motor.set_servo(value)

    # IMPORTANT: YOU MUST STOP THE HEARTBEAT IF IT IS RUNNING BEFORE IT GOES OUT OF SCOPE. Otherwise, it will not
    #            clean-up properly.
    motor.stop_heartbeat()



def time_get_values():
    with VESC(serial_port=serial_port) as motor:
        start = time.time()
        motor.get_measurements()
        stop = time.time()
        print("Getting values takes ", stop-start, "seconds.")


if __name__ == '__main__':
    #servo_set_position(0.45)
    run_motor_using_with() 
    #run_motor_as_object()
    #time_get_values()
