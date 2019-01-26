import time
# Notes:
#   /sys/class/drm/card0 ** Card location
#  /sys/class/drm/card0/device/hwmon/hwmon0/ hwmon0 location
# Modify "/sys/class/drm/card0/device/hwmon/hwmon0/pwm1" to set speed
# current temperature is stored inside /sys/class/drm/card0/device/hwmon/hwmon0/temp1_input  (Divide it by 100)
# Max speed:255
# Min speed: 0

# TODO make sure fanspeed isn't stuck on being unnecessarily high


def function():

    # Checking old and new temperature with a time difference of 5 seconds, assigning temps to temp_old && temp_new
    try:
        temp_old_check = open("/sys/class/drm/card0/device/hwmon/hwmon0/temp1_input", "r")
        temp_old = int(temp_old_check.read())
    finally:
        temp_old_check.close()
    time.sleep(5)
    try:
        temp_new_check = open("/sys/class/drm/card0/device/hwmon/hwmon0/temp1_input", "r")
        temp_new = int(temp_new_check.read())
    finally:
        temp_new_check.close()

    # Checking current fanspeed, assigning it to variable fan_current as an int
    try:
        fans = open("/sys/class/drm/card0/device/hwmon/hwmon0/pwm1", "r")
        fan_current = int(fans.read())
    finally:
        fans.close()

    # Calculating difference between temp_old and temp_new then calling function fanspeed_change()
    # Calling fan_speed("max") if temp_new is greater than 80 degrees C
    if temp_new > 80000:
        fanspeed_change("max", fan_current)
    else:
        if temp_new > temp_old:
            fanspeed_change(5, fan_current)
        elif temp_new == temp_old:
            fanspeed_change(0, fan_current)
        else:
            fanspeed_change(-0, fan_current)


def fanspeed_change(input, fan_current):

    # Checks input value. if input is max the apply variable is put to 255 (my fans max speed)
    # if it's 5 the apply variable is put as current fanspeed + roughly 5% of max speed (13)
    # if input is -5 apply variable is set to current fanspeed - roughly 5% of max speed (13)

    if str(input) == "max":
        apply = 255
        print("Emergency: putting fans to max")
        fanspeed_apply(apply)

    elif int(input) == 5 and fan_current <= 242:
        apply = fan_current + 13
        print("increasing fanspeed")
        fanspeed_apply(apply)

    elif int(input) == 0:
        print("returning none")
        return None

    elif int(input) == -5:
        if fan_current <= 13:
            apply = 0
            print("killing fans")
            fanspeed_apply(apply)
        else:
            apply = fan_current - 13
            print("decreasing fanspeed")
            fanspeed_apply(apply)


def fanspeed_apply(inputs):

    try:
        pwm1 = open("/sys/class/drm/card0/device/hwmon/hwmon0/pwm1", "w")
        pwm1.write(str(inputs))
    finally:
        pwm1.close()











while True:
    function()
    time.sleep(2)