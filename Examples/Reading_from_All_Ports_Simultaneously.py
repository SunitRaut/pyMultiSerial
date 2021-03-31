from pyMultiSerial import pyMultiSerial as p
import time

# Create object of class MultiSerial
ms = p.MultiSerial()

ms.baudrate = 9600
ms.timeout = 2


#Add Callbacks
#Callback functions provide you an interface to perform an action at certain event.

# Callback on receiving port data
# Parameters: Port Number, Serial Port Object, Text read from port
def port_read_callback(portno, serial, text):
    print ("Received '"+text+"' from port "+portno)
    pass

#register callback function
ms.port_read_callback = port_read_callback




# Start Monitoring all Ports
ms.Start()

##To stop the gateway, press Ctrl+C in the console or command line.

# Do not write any code below gateway.autopilot(), as this method takes over the main thread.
# Rely on callbacks to add your own code / funcionality into this program.
    


