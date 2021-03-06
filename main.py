import time
# Notes:
#   /sys/class/drm/card0 ** Card location
#  /sys/class/drm/card0/device/hwmon/hwmon0/ hwmon0 location
# Modify "/sys/class/drm/card0/device/hwmon/hwmon0/pwm1" to set speed
# current temperature is stored inside /sys/class/drm/card0/device/hwmon/hwmon0/temp1_input
# Max speed:255
# Min speed: 0
 # TODO: Figure out whether or not the fancontrol (existence of pwm1) is dependent on drivers or not. Solve that.


class GraphicsProcessor:

 # Defines what happens when the class is created.
 # It adds input value to variable "device" , which is used for detecting GPU location.
 # Afterwards the temperature control process is started.
    def __init__(self, devicex)
    device = devicex
    self.fanspeed_apply(50)
    while true:
        self.function()


    def function(self):

        # Checking temperatures with a small timeout and then checking current fanspeed.
        try:
            temp_old_check = open("/sys/class/drm/card{0}/device/hwmon/hwmon0/temp1_input".format(device), "r")
            temp_old = int(temp_old_check.read())
        finally:
            temp_old_check.close()
            time.sleep(7)
        try:
            temp_new_check = open("/sys/class/drm/card{0}/device/hwmon/hwmon0/temp1_input".format(device), "r")
            temp_new = int(temp_new_check.read())
        finally:
            temp_new_check.close()

    # Checking current fanspeed, assigning it to variable fan_current as an int
        try:
            fans = open("/sys/class/drm/card{0}/device/hwmon/hwmon0/pwm1".format(device), "r")
            fan_current = int(fans.read())
        finally:
            fans.close()

    # ---------------------------------Below is the actual fanspeed being modified-----------------------------------
    # Calculating difference between temp_old and temp_new then increasing or decreasing fanspeed appropriately

    # if temp difference is 0 the function checks if the variable new_temp is lower or higher than 60 degrees C
    # if new_temp is higher than 60 degrees, the fanspeed isn't modified. if it is lower, the fanspeed is lowered.
    # if temp is lower than 60 and fan PWM value is lower than 15 it simply kills the fans.

    # if the gpu temp is higher than 90 degrees C, the fans are put at max speed to prevent damage.

    # if a temperature increase is detected, fanspeed is increased.

    # If a temperature decrease is detected the fanspeed is lowered
        if temp_new > 90000:
            print("Emergency: Temp too high! Maximising fanspeed")
            self.fanspeed_apply(255)
        else:

            if temp_new == temp_old:
                if fan_current <= 15 and temp_new <= 60000:
                    self.killfans()

                elif temp_new <= 60000 and fan_current != 0:
                    print("Temperature stagnated and below 60 degrees, attempting to lower fans. "
                      "Current value: " + str(fan_current))
                    self.fanspeed_apply((lambda c: c - 5)(fan_current))

                elif temp_new > 60000:
                    print("Temperature is above 60 degrees, increasing fanspeed... Value is: " + str(fan_current))
                    self.fanspeed_apply((lambda c: c+20)(fan_current))

            elif temp_new > temp_old and fan_current <=255:
                print("Temperature is increasing. Increasing fanspeed... Value is: " + str(fan_current))
                self.fanspeed_apply((lambda c: c+20)(fan_current))

            elif temp_new < temp_old and temp_new <= 60000:
                if fan_current <= 15:
                    self.killfans()
                else:
                    print("Temperature is dropping and is below 60 degrees. Lowering fanspeed... "
                          " Current value: " + str(fan_current))
                    self.fanspeed_apply((lambda c: c-10)(fan_current))
    # killfans is a function that kills the fans.
    # This was made into a function due to the need of using the same code twice. Keep it DRY :)

    def killfans(self):
        print("Temperature stagnated and temp lower than 60 degrees... Killing fans...")
        self.fanspeed_apply(0)

    def fanspeed_apply(self, inputs):
        try:
            pwm1 = open("/sys/class/drm/card{0}/device/hwmon/hwmon0/pwm1".format(device), "w")
            pwm1.write(str(inputs))
        finally:
            pwm1.close()


 # Assigning up to 6 graphics processors to one class each.
gpudictionary = {}
for i in range (6):
    try:
        gpudictionary["device{0}".format(i)] = GraphicsProcessor(i)
    except FileNotFoundError:
        break
