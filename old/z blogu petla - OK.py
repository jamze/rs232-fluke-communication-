import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM3',
    baudrate=115200,
    timeout=0.1,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)


#ser.open()
ser.isOpen()

print (ser.isOpen())
#'Enter your commands below.\r\nInsert "exit" to leave the application.'

while 1:
    #print ("podaj qm by odczytac wartosci / id by sprawdzic id fluke")
    input1 = "qm"
    if input1 == 'exit':
        ser.close()
        exit()
    else:
        while 1:
            # send the character to the device
            ser.write((input1 + '\r\n').encode())
            out = ''
            # let's wait before reading output (let's give device time to answer)
            time.sleep(0.2)
            while ser.inWaiting() > 0:
                out = ser.read(99)

            if out != '':
                print(out.decode())
            time.sleep(0.2)