MultiSerial Class
=================
.. module:: pyMultiSerial
 
.. class:: MultiSerial
 
    .. method:: __init__()
 
On creating object of class MultiSerial, port parameters are set up. All ports are configured with the same parameters. 

    .. method:: Start()
Start the monitoring of ports.

    .. method:: Stop()
Stop the monitoring of ports.

    ..attribute:: baudrate (Necessary)
       :type: int
    Sets baudrate for the serial ports. 
    
    ..attribute:: timeout (Optional)
       :type: int
    Sets timeout for the serial ports. Default value = 2 sec
    
    ..attribute:: portno_range (Optional)
       :type: int
    Sets range of port numbers to monitor starting from 0. Default value = 29
    
    ..attribute:: monitoring_freq (Optional)
       :type: int
    Sets monitoring frequency. Default value = 0 msec
    
    ..attribute:: port_connection_found_callback (Optional)
       :type: function
    Sets callback function for Event when new serial port connection is found 
    
    ..attribute:: port_read_callback (Optional)
       :type: function
    Sets callback function for Event when data is received on any serial port
    
    ..attribute:: port_disconnection_callback (Optional)
       :type: function
    Sets callback function for Event when a port is disconnected 
    
    ..attribute:: interrupt_callback (Optional)
       :type: function
    Sets callback function for Event when execution of program is interrupted
    
    ..attribute:: loop_callback (Optional)
       :type: function
    Sets callback function to be executed in continuous loops.
    
    
