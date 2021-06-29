'''
Items in DPG can be broken into 4 main points:
	- regular items (inputs, buttos, etc)
	- container items (window, popup, tooltip, child)
	- laytou items (group, next_column)

Item are added with ther respective add_*** commands or context managers
'''

# List of Regular Items
'''
add_button(name='text label')
'''

# List of Container Items
'''
with window(name='text label'):
	block
'''

# List of Laytout Items
'''
add_same_line(spacing=10)
add_spacing(count=5)
'''

# example
from dearpygui.core import *
from dearpygui.simple import *

with window(name="Tutorial"):
    add_button(name="Apply1")
    add_same_line(spacing=10)
    add_button(name="Apply2")
    add_same_line(spacing=10)
    add_button(name="Apply3")
    add_spacing(count=5)

start_dearpygui() 