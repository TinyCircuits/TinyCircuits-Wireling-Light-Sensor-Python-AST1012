# TinyCircuits Light Sensor TSL2572 Wireling Module Example
# Prints illimuniance values read from ambient light sensor in terms of lux
# every second.
# Written by Laverena Wienclaw for TinyCircuits
# Initialized: 9-10-19
# Last Updated: 12-16-19

import tinycircuits_wireling
import tinycircuits_tsl2572
import time

# Initialize and enable power to Wireling Pi Hat
wireling = tinycircuits_wireling.Wireling()

# Toggle this variable to use the Light Sensor Wireling on a different port (0-3)
port = 0
wireling.selectPort(port)

# Create library object using our Bus I2C port
tsl2572 = tinycircuits_tsl2572.TinyCircuits_TSL2572_I2C(2) # Set Gain to 2 = 16x

while(True):
    lux = tsl2572.readAmbientLight()
    print("Lux: {}".format(lux))
    time.sleep(1)
