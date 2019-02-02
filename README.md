# amdgpu-fancontrol-python3.7
This is a WIP python fancontrol script for controlling gpu fanspeeds. 
many features are missing due to it's early status. 
Planned features are:
  * Automatic card detection
    - automatic detection of max and min speeds
  * Configuration files
  * Multi-GPU support - WIP

It will attempt to keep gpu temperature around 60 degrees Celcius, keeping fanspeeds low if the temperature is beneath 60 degrees and is not increasing. This makes for a more silent system overall.
Support is intended to be for Fedora/Redhat altough I see few reasons it would not work for distros like Ubuntu.

Dependencies:
Python 3.7 (altough 2.7 appears to function just fine)

 
  
    
