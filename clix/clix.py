import os
import sys
import json
import xerox
import pickle
import argparse
try:
    import utils
except:
    import clix.utils as utils
from .pyxhook import HookManager
from .gui import clipboard

# number of active clix GUIs
active = 0
# previously logged key
prev_Key = None
# path to site package
curr_dir = os.getcwd()

key_binding = []

# loading key_binding from config file
# try:
with open(os.path.join(os.path.dirname(__file__),'config'), "rb") as f:
    key_binding = pickle.load(f)

# if file does not exist create empty file

clips_data = open(os.path.join(os.path.dirname(__file__),'clips_data'), "rb")
utils.clips = pickle.load(clips_data)
clips_data.close()


def OnKeyPress(event):
    """
    function called when any key is pressed
    """
    global prev_Key, active, key_binding

    if event.Key == key_binding[1] and prev_Key == key_binding[0] \
            and active == 0:
        active = 1
        clipboard(utils.clips)
        active = 0
        prev_Key = None

    elif event.Key == 'c' and prev_Key == 'Control_L':
        text = xerox.paste(xsel=True)
        utils.clips.append(text)
        # pickle clips data
        with open(os.path.join(os.path.dirname(__file__),'clips_data'), "wb") as f:
            pickle.dump(utils.clips, f, protocol=2)

        print("You just copied: {}".format(text))

    else:
        prev_Key = event.Key

    return True


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
    return temp[key_binding[0]] + "+" + temp[key_binding[1]]


def create_new_session():
    """
     clear old session
    """
    with open(os.path.join(os.path.dirname(__file__),'clips_data'), "wb") as f:
        utils.clips = []
        pickle.dump(utils.clips, f, protocol=2)


def main():
    """
    main function (CLI endpoint)
    """
    global key_binding

    parser = argparse.ArgumentParser()

    help = """Set alternate key binding. Default is LCTRL+SPACE
                Format :- <KEY1>+<KEY2>. Ex:- RCTRL+RALT .
                To see availble key bindings use 'clix -a' option"""

    parser.add_argument("-s", "--set-keybinding", type=str,
                        default=None, help=help)

    parser.add_argument("-a", "--show-available-keybindings",
                        help="Show available key bindings",
                        action="store_true")

    parser.add_argument("-c", "--show-current-keybinding",
                        action="store_true")

    parser.add_argument("-n", "--new-session", action="store_true",
                        help="start new session clearing old session")

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
            key_binding = [utils.available_keys[keys[0]],
                           utils.available_keys[keys[1]]]
        except KeyError:
            print("Please follow the correct format.")
        else:
            with open(os.path.join(os.path.dirname(__file__),'config'), "wb") as f:
                pickle.dump(key_binding, f, protocol=2)
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
