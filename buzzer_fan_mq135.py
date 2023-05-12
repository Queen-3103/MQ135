from machine import ADC,Pin
import time

BUZZER_PIN = 0
fan_pin =Pin(1,Pin.OUT)

buzzer =Pin(BUZZER_PIN, Pin.OUT)
adc = machine.ADC(26) # create an ADC object on pin GP26 (ADC0)
voltageConversionFactor = 3.3 / (65535) # ADC reference voltage is 3.3V
while True:
    sensor_value = adc.read_u16() # read the raw ADC value
    print("Sensor value: ", sensor_value)
    voltage = sensor_value * voltageConversionFactor # convert the ADC value to voltage
    ppm = (voltage - 0.1) * 10000 / 0.8 # convert voltage to ppm (parts per million)
    print("MQ135 Value (ppm):", ppm)
    # Turn on the buzzer if the MQ135 value is above a threshold
    if ppm > 2000:
        buzzer.value(1)
        time.sleep(0.5)
        buzzer.value(0)
        time.sleep(0.1)
    time.sleep(2) # wait for 1 second before taking the next reading
