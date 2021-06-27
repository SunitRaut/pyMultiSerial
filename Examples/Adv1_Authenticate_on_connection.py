'''
-----------------------------------------------------------------------------------------
Author: Sunit Raut - github.com/SunitRaut
-----------------------------------------------------------------------------------------
This example authenticates the serial port with password for security purposes. This is 
recommended to ensure that you are communicating with the right device only.
-----------------------------------------------------------------------------------------
'''

import time

import pyMultiSerial as p


# Create object of class pyMultiSerial
ms = p.MultiSerial()

ms.baudrate = 9600
ms.timeout = 2


#Add Callbacks
#Callback functions provide you an interface to perform an action at certain event.
'''
List of Events for callback:
1. On detecting a port connection
2. On reading data from port
3. On port disconection
4. On Keyboard Interrupt (Ctrl+C)
5. Continuous loop execution
'''  
# Callback function on detecting a port connection.
# Parameters: Port Number, Serial Port Object
def port_connection_found_callback(portno, serial):
    print ("Port Found: "+portno)
    #time.sleep(1.5)
    serial.write(b"Password?\n")
    y = serial.readline().decode("utf=8")
    print(y)
    if y=="Hello\n":
        print("Port Accepted")
    else:
        ms.ignore_port(serial)
        print("Port rejected")

#register callback function
ms.port_connection_found_callback = port_connection_found_callback


# Callback on receiving port data
# Parameters: Port Number, Serial Port Object, Text read from port
def port_read_callback(portno, serial, text):
    print ("Received '"+text+"' from port "+portno)
    pass

#register callback function
ms.port_read_callback = port_read_callback

# Callback on port disconnection. Triggered when a device is disconnected from port.
# Parameters: Port No
def port_disconnection_callback(portno):
    print("Port "+portno+" disconnected")
    pass

#register callback function
ms.port_disconnection_callback = port_disconnection_callback


# Callback on interrupt. Triggered when python script execution is interrupted.
# Parameters: -

def interrupt_callback():
    print("Stopped Monitoring")
    pass

#register callback function
ms.interrupt_callback = interrupt_callback



## Start monitoring serial ports
ms.Start()

## To stop monitoring, press Ctrl+C in the console or command line.

# Caution: Any code written below ms.Start() will be executed only after monitoring is stopped.
# Make use of callback functions to execute your code. 

