# amdgpu-fancontrol-python3.7
This is a WIP python fancontrol script for automatically controlling the fans for amd graphicscards.
some features are missing due to it's early status. it has currently been tested on an R9 380 (4gb) and a Radeon hd4870
Planned features are:
  * Automatic card detection
    - automatic detection of max and min speeds
  * Configuration files
  * ATI-GPU support. -- Old graphics-cards like the Radeon hd4870 appears to adjust fans differently. so they are currently not supported.

Current features are:
   * Fans are controlled, and do appear to adjust efficently. The current locations should be standard if only one GPU is connected to the system. If not, adjust the code yourself until it works for now.


It will attempt to keep gpu temperature around 60 degrees Celcius, keeping fanspeeds low if the temperature is beneath 60 degrees and is not increasing. This makes for a more silent operation.

Support is intended to be for Fedora/Redhat altough I see few reasons it would not work for distros like Ubuntu.

Dependencies:
Python 3.7
