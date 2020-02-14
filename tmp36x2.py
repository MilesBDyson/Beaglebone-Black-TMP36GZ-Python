import Adafruit_BBIO.ADC as ADC
import time

sensor_pin1 = 'P9_40'
sensor_pin2 = 'P9_37'
ADC.setup()

while True:
    reading1 = ADC.read(sensor_pin1)
    reading2 = ADC.read(sensor_pin2)

    millivolts1 = reading1 * 1800  # 1.8V reference = 1800 mV
    millivolts2 = reading2 * 1800

    temp_c1 = (millivolts1 - 500) / 10
    temp_c2 = (millivolts2 - 500) / 10

    temp_f1 = (temp_c1 * 9/5) + 32
    temp_f2 = (temp_c2 * 9/5) + 32

    print('F1=%.2f F2=%.2f' % (temp_f1, temp_f2))
    time.sleep(0.2)
