import serial
# make sure to use the correct serial serial communication device name 
# e.g. /dev/ttyUSB0, /dev/ttyUSB1, /dev/ttyACM0, ...
#  as you discovered in the steps above
ser = serial.Serial('/dev/ttyACM1', 9600)
# loop until manually stopped
# first flush possibly existing data in the input buffer:
ser.flushInput()
while True:
        # read a single line from the serial interface represented by the ser object
        lineBytes = ser.readline()
        # convert Bytes returned by the ser.readline() function to String
        line = lineBytes.decode('utf-8')
        # print the read line to the output
        estado = int(line)
        if estado == 0:
            print("Se detecto un choque en la parte frontal")
        elif estado == 2:
            print("se abrio el capo del auto")
        elif estado == 3:
            print("se abrio la puerta del piloto")
        elif estado == 4:
            print("Se abrio la puerta del copiloto")
        elif estado == 5:
            print("Se abrio la puerta trasera del piloto")
        elif estado == 6:
            print("Se abrio la puerta trasera del copiloto")
        elif estado == 7:
            print("Se abrio la maletera")
        elif estado == 8:
            print("Se detecto un choque en la parte Trasera") 
