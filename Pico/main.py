import usb_cdc
usb_cdc.enable(console=True, data=True)
import time
#usb_cdc.disable()
#usb_cdc.enable(console=True, data=False)

print('bruh')
serial = usb_cdc.data

#servo = PWM(Pin(9))
#servo.freq(50)
MIN = 1000000
MAX = 2000000


while True:
    #ret = uart.readline()
    #print(ret)
    
    
    if serial.in_waiting > 0:
        byte = serial.read(1)
        if byte == b'\r':
            log(in_data.decode("utf-8"))
            out_data = in_data
            out_data += b'  '
            in_data = bytearray()
            out_index = 0
        else:
            in_data += byte
            if len(in_data) == 129:
                in_data = in_data[128] + in_data[0:127]
            
    try:
        ret = ret.decode("utf-8", "ignore")
        if ret[-1] == '\n':
            uart0.write('ok\n')
        
        print(com)
        comm = ret[0]
        param = ret[1:]

        print(comm)
        
        if comm == 'r':
            pass
        else:
            mes_ok = False
        
    except:
        print('error')
        
        
                

    sleep(0.01)

"""

import usb_cdc
#usb_cdc.disable()
usb_cdc.enable(console=True, data=False)

print('bruh')
"""