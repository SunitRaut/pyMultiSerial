import time

import pyMultiSerial as p

# Create object of class pyMultiSerial
ms = p.MultiSerial()

ms.baudrate = 9600
ms.timeout = 2


#Add Callbacks
#Callback functions provide you an interface to perform an action at certain event.
 
# Callback function on detecting a port connection.
# Parameters: Port Number, Serial Port Object
# Return: True if the port is to be accepted, false if the port is to be rejected based on some condition
def port_connection_found_callback(portno, serial):
    print ("Port Found: "+portno)

#register callback function
ms.port_connection_found_callback = port_connection_found_callback

# Callback on port disconnection. Triggered when a device is disconnected from port.
# Parameters: Port No
def port_disconnection_callback(portno):
    print("Port "+portno+" disconnected")

#register callback function
ms.port_disconnection_callback = port_disconnection_callback



ms.Start()

##To stop the program, press Ctrl+C in the console or command line.

# Do not write any code below ms.Start(), as this method takes over the main thread.
# Rely on callbacks to add your own code / funcionality into this program.
