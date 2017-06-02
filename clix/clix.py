import json
import xerox
from .pyxhook import HookManager
from .gui import clipboard

# clipboard
clips = []
# number of active clix GUIs 
active = 0
# previously logged key
prev_Key = None

def OnKeyPress(event):
	global prev_Key, active
	if event.Key == 'space' and prev_Key == 'Control_L' and active == 0:
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
	new_hook = HookManager()
	new_hook.KeyDown = OnKeyPress
	new_hook.HookKeyboard()
	new_hook.start()


if __name__ == "__main__":
	main()
	

