# pyMultiSerial
[![GitHub release](https://img.shields.io/github/release/SunitRaut/pyMultiSerial.svg)](https://github.com/SunitRaut/pyMultiSerial)
[![license](https://img.shields.io/github/license/SunitRaut/pyMultiSerial.svg)](https://github.com/SunitRaut/pyMultiSerial/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5035457.svg)](https://doi.org/10.5281/zenodo.5035457)

A Python module for continuous communication with multiple serial ports, based on pyserial module

## Features: 
- Monitor multiple serial ports simultaneously.
- Detect connections to port automatically and starts monitoring them. 
- Raises a trigger whenever data is received from the port. You can attach callback function to process this data on-demand. 
- Detect disconnections from port automatically. 
- You can add your own processing logic to the above events using callback functions 

## How to Install:
```
pip3 install pyMultiSerial
```

## Dependencies: 
Dependencies are automatically installed during installation of pyMultiSerial.

- PySerial
- Threading

## How to use

pyMultiSerial is very easy to use! Below are the important statements & functions of the library. Do check the Examples folder for simple examples to get started with.

### Step 1: Initialize

Import Module
```
import pyMultiSerial as p
```
Create Object
```
ms = p.MultiSerial()
```
Set Properties of Object:
```
ms.baudrate = 9600    
ms.timeout = 2
```
### Step 2: Define Callback Functions

Callback functions are the functions defined by you in your program which are triggered by pyMultiSerial module whenever an event occurs.

The pyMultiSerial module provides 5 callback events for which you can define functions:
1. **New Serial Port Connection Found** - Allows you to write a function which triggers when a new serial port connection is found. With this feature, you can perform many operations like authenticating, performing handshake or simply creating a list of newly connected devices.
2. **Data Received on a Serial Port** - Allows you to write a function which triggers when any data is received on the serial port. With this feature, you can process incoming data from serial ports.
3. **Device disconnected from Serial Port** - Allows you to write a function which triggers when any device is disconnected. With this feature, you can keep track of serial ports that have been disconnected.
4. **On Keyboard Interrupt (Ctrl+C) by user** - Allows you to write a function which triggers when you force stop the python script with keyborard interrupt or through your Python IDE. This feature allows you to perform any clean up activities necessary before exiting your application.
5. **Continuous Loop Execution** - Allows you to write a function which triggers continuously. With this feature, you can perform repitive / periodic tasks. Don't forget to add appropriate delay in this callback since this event occurs continuously. The user gets to decide what frequency / delay is needed.

Note: All the above callbacks are optional. You need to only program those callbacks which you need.  

**How to define and register callback function:**
```
def your_func_name(standard_arguments):
    Your Statements
    End of function
#register callback function
ms.callback_name = your_func_name
```
Here, **your_func_name** can be any name as decided by you. Arguments passed to this function should be in accordance to the **standard_arguments** as defined in below table. These arguments will be passed from pyMultiSerial module to your function. **callback_name** is the property name of the callback event to which you need to assign your function as shown in above snippet.

|    Event                              | callback_name                 | standard_arguments for callback function|
|---------------------------------------|-------------------------------|-----------------------------------------|
|New Serial Port Connection Found       |port_connection_found_callback |Port Number, Serial Port Object          |    
|Data Received on a Serial Port         |port_read_callback             |Port Number, Serial Port Object, Data    |
|Device disconnected from Serial Port   |port_disconnection_callback    |Port Number                              |
|On Keyboard Interrupt (Ctrl+C) by user |interrupt_callback             |-                                        |
|Continuous Loop Execution              |loop_callback                  |-                                        |

In the above table, there are mainly three types of arguments:
1. Port Number - The Port Number of the port on which the event has occured.
2. Serial Port Object - pySerial Object of the Port on which event has occured. This object can be used to read, write to the port from your callback function.
3. Data - Data received from Serial Port in String format.

Note: You must include above paramenters in your function definition. However, it is optional to use those parameters.


### Step 3: Start Monitoring

Start Monitoring with below statement:
```
ms.Start()
```
Caution: Since this module monitors all serial ports simultaneously, ms.Start() is a blocking function. Unless you don't stop monitoring using Stop() method, the execution will be stuck at this line. Start() method should ideally be called at the end of your code. To perform other opertions, you should use the provided callback functions.
Caution: Callback functions should be defined before ms.Start() statement. The Callback functions should be registered with the object before monitoring is started, else your callback functions won't be called.

If you need to stop monitoring for any reason, use below statement:
```
ms.Stop()
```

Here is an [instructable with simple Arduino-Raspberry Pi example](https://www.instructables.com/How-to-Monitor-Arduinos-Connected-to-Multiple-Port/)

Hope this module helps you to build your Projects. In case of any issues do open an Issue on Github. 
