# Examples

## Python - Arduino Communication Examples

Open this folder to check Arduino - Python Communication sample projects/examples. In these examples, source code for Raspberry Pi / PC Python as well as Arduino IDE have been provided.

## Basic Examples

Basic Examples to Learn usage of this library easily.

### 1.Reading_from_All_Ports_Simultaneously.py

This example shows how to read data coming from one / multiple serial ports simultaneously.

### 2.Monitor_Connections.py

This example shows how to monitor serial ports to check if a new port is connected or if a previously connected port is now disconnected.

### 3.Monitor_Connections_and_Read_from_all_ports.py

This example shows how to Monitor connections as well as read simultaneously from serial ports. This example is a combination of Examples 1 & 2.

### 4.Stop_reading_from_a_port.py

This example shows how to stop reading a particular port. 


## Advanced Examples

### Adv1_Authenticate_on_connection
This example authenticates the serial port with password for security purposes. This is recommended to ensure that you are communicating with the right device only.



1. Authenticate a device on finding new connection, if authentication failed, ignore the device
2. Ignore a device if it sends disconnection request on serial port
3. Pause or Resume a port




1. How to read incoming data as and when available on any port
2. How to display devices when they are connected or disconnected from any port
3. Display Connections, Disconnections and incoming data from any port
4. Perform a set of Tasks once on start of Monitoring
5. Perform a Task in Loop
6. Interrupt Callback Example
7. Combination of All Basic Examples
