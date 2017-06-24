import os, sys
import json
import xerox
import pickle
import argparse
from .pyxhook import HookManager
from .gui import clipboard
import utils


# number of active clix GUIs
active = 0
# previously logged key
prev_Key = None
# path to site package
curr_dir = os.getcwd()

# loading key_binding from config file 
with open(curr_dir + "/clix/config", "rb") as f:
        key_binding = pickle.load(f)


# if file does not exist create empty file
try:    
    clips_data = open(curr_dir + "/clix/clips_data", "rb")
    utils.clips = pickle.load(clips_data)
    clips_data.close()
except:
    clips_data = open(curr_dir + "/clix/clips_data", "wb")
    utils.clips = []
    clips_data.close()


def OnKeyPress(event):
    """
    function called when any key is pressed
    """
    global prev_Key, active, key_binding

    if event.Key == key_binding[1] and prev_Key == key_binding[0] and active == 0:
        active = 1
        clipboard(utils.clips)
        active = 0
        prev_Key = None

    elif event.Key == 'c' and prev_Key == 'Control_L':
        text = xerox.paste(xsel=True)
        utils.clips.append(text)
        # pickle clips data 
        with open(curr_dir + "/clix/clips_data", "wb") as f:
            pickle.dump(utils.clips, f, protocol = 2)
        
        print("You just copied: {}".format(text))

    else:
        prev_Key = event.Key


def _show_available_keybindings():
    """
    function to show available keys
    """
    print("Available Keys: "+"\n")
    for key in utils.available_keys:
        print(key)


def get_current_keybinding():
    """
    function to show current key-binding
    """
    global key_binding
    temp = {b: a for a, b in utils.available_keys.items()}
    print(temp)
    print(key_binding)
    return temp[key_binding[0]] + "+" + temp[key_binding[1]]

def create_new_session():
    """
     clear old session
    """
    with open(curr_dir + "/clix/clips_data", "wb") as f:
        utils.clips=[]
        pickle.dump(utils.clips, f, protocol = 2)


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
    
    parser.add_argument("-n", "--new-session", action = "store_true",
                         help = "start new session clearing old session")

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
            key_binding = [utils.available_keys[keys[0]], utils.available_keys[keys[1]]]
        except KeyError:
            print("Please follow the correct format.")
        else:
            with open(curr_dir + "/clix/config", "wb") as f:
                pickle.dump(key_binding, f, protocol = 2)
        finally:
            sys.exit()

    elif args.new_session:
        print("new session")
        create_new_session()


    # start key-logging session
    new_hook = HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.HookKeyboard()
    new_hook.start()


if __name__ == "__main__":
    main()