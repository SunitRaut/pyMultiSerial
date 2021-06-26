# pyMultiSerial
[![GitHub release](https://img.shields.io/github/release/SunitRaut/pyMultiSerial.svg)](https://github.com/SunitRaut/pyMultiSerial)
[![license](https://img.shields.io/github/license/SunitRaut/pyMultiSerial.svg)](https://github.com/SunitRaut/pyMultiSerial/blob/main/LICENSE)

A Python library for continuous communication with multiple serial ports, based on pyserial module

## Features: 
- Monitor multiple serial ports simultaneously.
- Detect connections to port automatically and starts monitoring them. 
- Raises a trigger whenever data is received from the port. You can attach callback function to process this data on-demand. 
- Detect disconnections from port automatically. 
- You can add your own processing logic to the above events using callback functions 

## How to Install:
```
pip3 install --index-url https://test.pypi.org/simple/ --no-deps pyMultiSerial==1.0.7
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
1. New Serial Port Connection Found - Allows you to write a function which triggers when a new serial port connection is found. With this feature, you can perform many operations like authenticating, performing handshake or simply creating a list of newly connected device.
2. Data Received on a Serial Port - Allows you to write a function which triggers when any data is received on the serial port. With this feature, you can process incoming data from serial ports.
3. Device disconnected from Serial Port - Allows you to write a function which triggers when any device is disconnected. With this feature, you can keep track of serial ports that have been disconnected.
4. On Keyboard Interrupt (Ctrl+C) by user - Allows you to write a function which triggers when you force stop the python script with keyborard interrupt or through your Python IDE. This feature allows you to perform any clean up activities necessary before exiting your application.
5. Continuous Loop Execution - Allows you to write a function which triggers continuously. With this feature, you can perform repitive / periodic tasks. Don't forget to add appropriate delay in this callback since this event occurs continuously. The user gets to decide what frequency / delay is needed.

Note: All the above callbacks are optional. You need to only program those callbacks which you need.  



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


Hope this module helps you to build your Projects. In case of any issues do open an Issue on Github. 
