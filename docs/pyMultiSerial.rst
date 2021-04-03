
==========
 pyMultiSerial
==========

Overview
========

A Python library for continuous communication with multiple serial ports, based on pyserial module.

pyMultiSerial module helps you to run 


It is released under a free software license, see LICENSE_ for more
details.


Other pages (online)

- `Download Page`_ with releases (PyPi)
- This page, when viewed online is at https://pymultiserial.readthedocs.io/en/latest/ or
  http://pythonhosted.org/pymultiserial/ .

.. _Python: http://python.org/
.. _LICENSE: appendix.html#license
.. _`Download Page`: http://pypi.python.org/pypi/pymultiserial


Features
========

- Monitor multiple serial ports simultaneously.

- Detect connections to port automatically and starts monitoring them.

- Raises a trigger whenever data is received from the port. You can attach callback function to process this data on-demand.

- Detect disconnections from port automatically.

- You can add your own processing logic to the above events using callback functions


Requirements
============
- Python 3+

- If running on Windows: Windows 7 or newer


Installation
============

This installs a package that can be used from Python (``import pyMultiSerial from pyMultiSerial``).

To install for all users on the system, administrator rights (root)
may be required.

From PyPI
---------
pySerial can be installed from PyPI::

    python -m pip install pymultiserial

Using the `python`/`python3` executable of the desired version (2/3.x).

Developers also may be interested to get the source archive, because it
contains examples, tests and the this documentation.

From Conda
----------
pyMultiSerial can be installed from Conda::

    conda install pyMultiSerial
    
    or
    
    conda install -c conda-forge pymultiserial

Conda: https://www.continuum.io/downloads

From source (zip/tar.gz or checkout)
------------------------------------
Download the archive from http://pypi.python.org/pypi/pymultiserial or
https://github.com/sunitraut/pymultiserial/releases.

Using the `python`/`python3` executable of the desired version (2/3.x).


.. _PyPi: http://pypi.python.org/pypi/pymultiserial

