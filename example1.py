import time

import pyMultiSerial as p

# Create object of class pyMultiSerial
gateway = p.MultiSerial()

gateway.baudrate = 9600

#Add Callbacks
#Callback functions provide you an interface to perform an action at certain event.
'''
List of Events for callback:
1. On detecting a port connection
2. On reading data from port
3. On port disconection
4. Callback to main thread to add other miscellaneous programming
'''  
# Callback function on detecting a port connection.
# Parameters: Port Number, Serial Port Object
# Return: True if the port is to be accepted, false if the port is to be rejected based on some condition
def port_connection_found_callback(portno, serial):
    print ("Port Found: "+portno)
    time.sleep(1.5)
    serial.write(b"Hello\n")
    y = serial.readline()
    print(y)
    if y==b"Hello\n":
        print("Port Accepted")
        return True
    else:
        print("Port rejected")
        return False

#register callback function
gateway.port_connection_found_callback = port_connection_found_callback


# Callback on receiving port data
# Parameters: Port Number, Serial Port Object, Text read from port
def port_read_callback(portno, serial, text):
    print ("Received '"+text+"' from port "+portno)
    pass

#register callback function
gateway.port_read_callback = port_read_callback

# Callback on port disconnection. Triggered when a device is disconnected from port.
# Parameters: Port No
def port_disconnection_callback(portno):
    print("Port "+portno+" disconnected")
    pass

#register callback function
gateway.port_disconnection_callback = port_disconnection_callback



#Set gateway on autopilot mode (Optional). 
#In this mode, the gateway runs on its own and handles the complete execution flow of program. 
#In this mode, you can't add your own code. You can register callbacks.
gateway.autopilot()

##To stop the gateway, press Ctrl+C in the console or command line.

# Do not write any code below gateway.autopilot(), as this method takes over the main thread.
# Rely on callbacks to add your own code / funcionality into this program.
    





