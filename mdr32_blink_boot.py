#port control from built-in bootloader

import time
import serial

CMD_SYNC    = b'\x00'

MDR_RST_CLK_PER_CLOCK   = b'\x4C\x1C\x00\x02\x40\x04\x00\x00\x00\x90\x00\x80\x00'
MDR_PORTC_PWR           = b'\x4C\x18\x80\x0B\x40\x04\x00\x00\x00\x30\x00\x00\x00'
MDR_PORTC_ANALOG        = b'\x4C\x0C\x80\x0B\x40\x04\x00\x00\x00\x04\x00\x00\x00'
MDR_PORTC_OE            = b'\x4C\x04\x80\x0B\x40\x04\x00\x00\x00\x04\x00\x00\x00'
MDR_PORTC_RXTX_LED_ON   = b'\x4C\x00\x80\x0B\x40\x04\x00\x00\x00\x04\x00\x00\x00'
MDR_PORTC_RXTX_LED_OFF  = b'\x4C\x00\x80\x0B\x40\x04\x00\x00\x00\x00\x00\x00\x00'

ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=1)



print("Start Demo MDR app")

print("Start sync...")
for i in range(512):
    ser.write(CMD_SYNC)

data = ser.read(3)

if ((len(data) == 3) and (data[2] == 62)):
    print("...OK")

    time.sleep(0.1)
    ser.write(MDR_RST_CLK_PER_CLOCK)
    time.sleep(0.1)
    ser.write(MDR_PORTC_PWR)
    time.sleep(0.1)
    ser.write(MDR_PORTC_ANALOG)
    time.sleep(0.1)
    ser.write(MDR_PORTC_OE)
    time.sleep(0.1)

    while (1):
        print("\rLED_OFF")
        ser.write(MDR_PORTC_RXTX_LED_OFF)
        time.sleep(0.5)
        print("\rLED_ON")
        ser.write(MDR_PORTC_RXTX_LED_ON)
        time.sleep(0.5)

else:
    print("Error...")
