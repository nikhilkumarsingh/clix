import json
import xerox
from pyxhook import HookManager
from gui import clipboard
import argparse


# clipboard
clips = []
# number of active clix GUIs 
active = 0
# previously logged key
prev_Key = None
available_keys = {	'LCTRL' : 'Control_L',
					'RCTRL' : 'Control_R',
					'ALT'   : "",
					'LSHIFT' : 'Shift_L',
					'RSHIFT' : 'Shift_R',
					'SPACE' : 'space'
					}

key_binding = ['Control_L','space']

def OnKeyPress(event):
	global prev_Key, active,key_binding
	if event.Key == key_binding[1] and prev_Key == key_binding[0] and active == 0:
		active = 1
		clipboard(clips)
		active = 0
		prev_Key = None
	elif event.Key == 'c' and prev_Key == 'Control_L':
		text = xerox.paste(xsel = True)
		clips.append(text) 
		print("You just copied: {}".format(text))
	else:
		prev_Key = event.Key

def main():
	global key_binding
	parser = argparse.ArgumentParser()
	parser.add_argument("-s","--set-keybinding",type=str,default="LCTRL+SPACE",help="Set alternate key binding. Default is LCTRL+SPACE")
	args = parser.parse_args()
	args_dict = vars(args)
	if args_dict['set_keybinding'] is not "LCTRL+SPACE":
		key_binding = [available_keys[args_dict['set_keybinding'].split('+')[0]],available_keys[args_dict['set_keybinding'].split('+')[1]]]
	new_hook = HookManager()	
	new_hook.KeyDown = OnKeyPress
	new_hook.HookKeyboard()
	new_hook.start()


if __name__ == "__main__":
	main()
	

