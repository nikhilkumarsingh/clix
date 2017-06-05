import os, sys
import json
import xerox
import pickle
import argparse
from .pyxhook import HookManager
from .gui import clipboard
from .utils import available_keys

# clipboard
clips = []
# number of active clix GUIs
active = 0
# previously logged key
prev_Key = None
# path to site package
curr_dir = os.getcwd()

# loading key_binding from config file 
with open(curr_dir + "/clix/config", "rb") as f:
        key_binding = pickle.load(f)


def OnKeyPress(event):
    """
    function called when any key is pressed
    """
    global prev_Key, active, key_binding

    if event.Key == key_binding[1] and prev_Key == key_binding[0] and active == 0:
        active = 1
        clipboard(clips)
        active = 0
        prev_Key = None

    elif event.Key == 'c' and prev_Key == 'Control_L':
        text = xerox.paste(xsel=True)
        clips.append(text)
        print("You just copied: {}".format(text))

    else:
        prev_Key = event.Key


def _show_available_keybindings():
    """
    function to show available keys
    """
    print("Available Keys: "+"\n")
    for key in available_keys:
        print(key)


def get_current_keybinding():
    """
    function to show current key-binding
    """
    global key_binding
    temp = {b: a for a, b in available_keys.items()}
    return temp[key_binding[0]] + "+" + temp[key_binding[1]]


def main():
    """
    main function (CLI endpoint)
    """
    global key_binding

    parser = argparse.ArgumentParser()
    
    help = """Set alternate key binding. Default is LCTRL+SPACE
                Format :- <KEY1>+<KEY2>. Ex:- RCTRL+RALT .
                To see availble key bindings use 'clix -a' option"""
    
    parser.add_argument("-s", "--set-keybinding", type = str,
                        default = None, help = help)

    parser.add_argument("-a", "--show-available-keybindings",
                        help = "Show available key bindings", action = "store_true")
    
    parser.add_argument("-c", "--show-current-keybinding", action = "store_true")
    
    args = parser.parse_args()
    args_dict = vars(args)
    
    if args.show_current_keybinding:
        print("Current key binding is: {}".format(get_current_keybinding()))
        sys.exit()

    elif args.show_available_keybindings:
        _show_available_keybindings()
        sys.exit()
    
    elif args.set_keybinding:
        try:
            keys = args_dict['set_keybinding'].split('+')
            key_binding = [available_keys[keys[0]], available_keys[keys[1]]]
        except KeyError:
            print("Please follow the correct format.")
        else:
            with open(curr_dir + "/clix/config", "wb") as f:
                pickle.dump(key_binding, f, protocol = 2)
        finally:
            sys.exit()

    # start key-logging session
    new_hook = HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.HookKeyboard()
    new_hook.start()


if __name__ == "__main__":
    main()