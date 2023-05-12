from machine import ADC
import utime

# Define the pin number for the MQ135 sensor
mq135_pin = machine.ADC(26)

# MQ135 calibration values
RL_VALUE = 90.05  # check using code for Resistance value
RO_CLEAN_AIR = 76.63  # MQ135 resistance in clean air (RO value at 100 ppm CO2)

# Function to calculate the resistance of the MQ135 sensor
def get_mq135_resistance():
    raw_value = mq135_pin.read_u16()
    voltage = raw_value * 3.3 / 65535
    resistance = RL_VALUE * (3.3 - voltage) / voltage
    return resistance

# Function to calculate the gas concentration in ppm
def get_gas_concentration(resistance, gas_type):
    # Gas-specific calibration values
    if gas_type == "NH3":
        a = 112.58
        b = -2.0
    elif gas_type == "S":
        a = 142.95
        b = -3.58
    elif gas_type == "C6H6":
        a = 97.15
        b = -1.64
    elif gas_type == "CO2":
        a = 119.16
        b = -2.75
    else:
        return None

    ppm = a * (resistance/RO_CLEAN_AIR)**(-b)
    return ppm

# Main loop
while True:
    # Read the MQ135 sensor resistance
    mq135_resistance = get_mq135_resistance()

    # Calculate gas concentrations in ppm
    nh3_ppm = get_gas_concentration(mq135_resistance, "NH3")
    s_ppm = get_gas_concentration(mq135_resistance, "S")
    c6h6_ppm = get_gas_concentration(mq135_resistance, "C6H6")
    co2_ppm = get_gas_concentration(mq135_resistance, "CO2")

    # Print the gas concentrations
    print("Ammonia (NH3) Concentration (ppm):", nh3_ppm)
    print("Sulfur (S) Concentration (ppm):", s_ppm)
    print("Benzene (C6H6) Concentration (ppm):", c6h6_ppm)
    print("Carbon Dioxide (CO2) Concentration (ppm):", co2_ppm)

    utime.sleep(1)  # Delay for 1 second
