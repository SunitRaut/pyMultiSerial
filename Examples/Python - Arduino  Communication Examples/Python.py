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


	#register callback function
	ms.port_disconnection_callback = port_disconnection_callback


	# Start Monitoring ports
	ms.Start()


	## To stop monitoring, press Ctrl+C in the console or command line.


	# Caution: Any code written below ms.Start() will be executed only after monitoring is stopped.
	# Make use of callback functions to execute your code. 
