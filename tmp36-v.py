import Adafruit_BBIO.ADC as ADC
import time

sensor_pin = 'P9_40'

ADC.setup()

tmp0 = 0
tmp1 = 0
tmp2 = 0
tmp3 = 0
tmp4 = 0
tmp5 = 0
tmp6 = 0
tmp7 = 0
tmp8 = 0
tmp9 = 0

while True:
   reading = ADC.read(sensor_pin)
   millivolts = reading * 1800  # 1.8V reference = 1800 mV
   temp_c = (millivolts - 500) / 10
   temp_f = (temp_c * 9/5) + 32

   tmp9 = tmp8
   tmp8 = tmp7
   tmp7 = tmp6
   tmp6 = tmp5
   tmp5 = tmp4
   tmp4 = tmp3
   tmp3 = tmp2
   tmp2 = tmp1
   tmp1 = tmp0
   tmp0 = temp_f

   tmp = (tmp0 + tmp1 + tmp2 + tmp3 + tmp4 + tmp5 + tmp6 + tmp7 + tmp8 + tmp9) / 10

   print('temp= %.1f' % (tmp))
   #print('mv=%d C=%d F=%.2f' % (millivolts, temp_c, temp_f))
   
   time.sleep(0.2)
