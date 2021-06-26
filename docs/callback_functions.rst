====================
 Callback Functions
====================

Callback functions are the functions defined by you in your program which are triggered by pyMultiSerial module whenever an event occurs.

The pyMultiSerial module provides 5 callback events for which you can define functions:
  #. **New Serial Port Connection Found** - Allows you to write a function which triggers when a new serial port connection is found. With this feature, you can perform many operations like authenticating, performing handshake or simply creating a list of newly connected devices.
  #. **Data Received on a Serial Port** - Allows you to write a function which triggers when any data is received on the serial port. With this feature, you can process incoming data from serial ports.
  #. **Device disconnected from Serial Port** - Allows you to write a function which triggers when any device is disconnected. With this feature, you can keep track of serial ports that have been disconnected.
  #. **On Keyboard Interrupt (Ctrl+C) by user** - Allows you to write a function which triggers when you force stop the python script with keyborard interrupt or through your Python IDE. This feature allows you to perform any clean up activities necessary before exiting your application.
  #. **Continuous Loop Execution** - Allows you to write a function which triggers continuously. With this feature, you can perform repitive / periodic tasks. Don't forget to add appropriate delay in this callback since this event occurs continuously. The user gets to decide what frequency / delay is needed.

Note: All the above callbacks are optional. You need to only program those callbacks which you need.  

**How to define and register callback function:**
   >>> def your_func_name(standard_arguments):
   >>>   Your Statements
   >>>   End of function
   >>> #register callback function
   >>> ms.callback_name = your_func_name

Here, **your_func_name** can be any name as decided by you. Arguments passed to this function should be in accordance to the **standard_arguments** as defined in below table. These arguments will be passed from pyMultiSerial module to your function. **callback_name** is the property name of the callback event to which you need to assign your function as shown in above snippet.

.. list-table:: Table
   :widths: 45 45 45
   :header-rows: 1
   
   * - Event
     - callback_name
     - standard_arguments for callback function
   * - New Serial Port Connection Found  
     - port_connection_found_callback 
     - Port Number, Serial Port Object 
   * - Data Received on a Serial Port  
     - port_read_callback 
     - Port Number, Serial Port Object, Data 
   * - Device disconnected from Serial Port  
     - port_disconnection_callback
     - Port Number              
   * - On Keyboard Interrupt (Ctrl+C) by user
     - interrupt_callback
     -                
   * - Continuous Loop Execution
     - loop_callback
     - 

In the above table, there are mainly three types of arguments:
  #. Port Number - The Port Number of the port on which the event has occured.
  #. Serial Port Object - pySerial Object of the Port on which event has occured. This object can be used to read, write to the port from your callback function.
  #. Data - Data received from Serial Port in String format.

Note: You must include above paramenters in your function definition. However, it is optional to use those parameters.
