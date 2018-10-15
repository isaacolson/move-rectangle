#!/usr/bin/env python
"""Move To Safe Farmware"""

from farmware_tools import device
from farmware_tools import get_config_value

# Load inputs from Farmware page widget specified in manifest file
pos_x = get_config_value('Move Rectangle', 'start_x')
pos_y = get_config_value('Move Rectangle', 'start_y')
pos_z = get_config_value('Move Rectangle', 'start_z')
rectLength = get_config_value('Move Rectangle', 'length')
rectWidth = get_config_value('Move Rectangle', 'width')

device.log('Moving to ' + str(pos_x) + ', ' + str(pos_y) + ', ' + str(pos_z), 'success', ['toast'])

def moveAbs(x, y, z, length, width):


device.move_absolute(
    {
        'kind': 'coordinate',
        'args': {'x': pos_x, 'y': pos_y, 'z': pos_z}
    }, 
    100,    
    {
        'kind': 'coordinate',
        'args': {'x': 0, 'y': 0, 'z': 0}
    }
)

device.log('success!!', 'success', ['toast'])

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
