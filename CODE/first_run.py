from dearpygui.core import *
from dearpygui.simple import *

def save_callback(sender, data):
	print("Save clicked")

with window("Example Window"):
	add_text('Hello, World!')
	add_button("Save", callback=save_callback)
	add_input_text("String", default_value="Quick brow fox")
	add_slider_float("Float", default_value=0.273, max_value=1)

start_dearpygui()