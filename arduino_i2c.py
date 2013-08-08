import quick2wire.i2c as i2c
import time

#bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04
gpio_register = 0x09

def writeNumber(value):
    with i2c.I2CMaster() as bus:
        bus.transaction(
            i2c.writing_bytes(address, gpio_register, value))
    return -1

def readNumber():
    with i2c.I2CMaster() as bus:
        read_results = bus.transaction(
            i2c.reading(address, 1))
    number = read_results[0][0]
    return number

while True:
    var = int(input("Enter 1 - 9: "))
    if not var:
        continue

    writeNumber(var)
    print("RPI: Hi Arduino, I sent you ", var)
    # sleep one second
    time.sleep(1)

    number = readNumber()
    print("Arduino: Hey RPI, I received a digit ", number)
    print

