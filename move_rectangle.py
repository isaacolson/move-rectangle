#!/usr/bin/env python
"""Move Rectangle Farmware"""

from farmware_tools import device
from farmware_tools import get_config_value

# Load inputs from Farmware page widget specified in manifest file
pos_x = get_config_value('Move Rectangle', 'start_x')
pos_y = get_config_value('Move Rectangle', 'start_y')
pos_z = get_config_value('Move Rectangle', 'start_z')
rectLength = get_config_value('Move Rectangle', 'length')
rectWidth = get_config_value('Move Rectangle', 'width')

def moveAbs(x, y, z):
    device.log('Moving to ' + str(x) + ', ' + str(y) + ', ' + str(z), 'success', ['toast'])
    device.move_absolute(
        {
            'kind': 'coordinate',
            'args': {'x': x, 'y': y, 'z': z}
        },
        100,
        {
            'kind': 'coordinate',
            'args': {'x': 0, 'y': 0, 'z': 0}
        }
    )

moveAbs(pos_x, pos_y, pos_z)
moveAbs(pos_x, pos_y + rectWidth, pos_z)
moveAbs(pos_x + rectLength, pos_y + rectWidth, pos_z)
moveAbs(pos_x + rectLength, pos_y, pos_z)
moveAbs(pos_x, pos_y, pos_z)

device.log('success!!', 'success', ['toast'])

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
