# pyMultiSerial
A Python library for continuous communication with multiple serial ports, based on pyserial module

Features: 
- Monitor multiple serial ports simultaneously.
- Detect connections to port automatically and starts monitoring them. 
- Raises a trigger whenever data is received from the port. You can attach callback function to process this data on-demand. 
- Detect disconnections from port automatically. 
- You can add your own processing logic to the above events using callback functions 
