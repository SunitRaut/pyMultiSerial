'''
-----------------------------------------------------------------------------------------
Author: Sunit Raut - github.com/SunitRaut
-----------------------------------------------------------------------------------------
This example shows how to read data coming from one / multiple serial ports simultaneously.
-----------------------------------------------------------------------------------------
'''

import pyMultiSerial as p
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




# Start Monitoring ports
ms.Start()

## To stop monitoring, press Ctrl+C in the console or command line.

# Caution: Any code written below ms.Start() will be executed only after monitoring is stopped.
# Make use of callback functions to execute your code. 
    


