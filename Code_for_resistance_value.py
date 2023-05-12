import machine
import time
# Define the pin number for the MQ135 sensor
mq135_pin = machine.ADC(26)

# Read the MQ135 sensor resistance
def get_mq135_resistance():
    raw_value = mq135_pin.read_u16()
    voltage = raw_value * 3.3 / 65535
    resistance = (3.3 * 10 / voltage) - 10
    return resistance

# Main loop
while True:
    # Read the MQ135 sensor resistance
    mq135_resistance = get_mq135_resistance()

    # Print the resistance value
    print("MQ135 Resistance (RL_VALUE):", mq135_resistance)

    # Delay for 1 second
    time.sleep(1000)

