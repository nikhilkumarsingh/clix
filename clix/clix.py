import json
import xerox
from .pyxhook import HookManager
from .gui import clipboard
import argparse
from utils import available_keys
import sys
import pickle

# clipboard
clips = []
# number of active clix GUIs
active = 0
# previously logged key
prev_Key = None

with open("config", "rb") as f:
    key_binding = pickle.load(f)


def OnKeyPress(event):
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
    print("Available Keys:- "+"\n")
    for i in available_keys:
        print(i)


def _show_current_keybinding():
    with open("config", "rb") as f:
        key_binding = pickle.load(f)
        temp = {b: a for a, b in available_keys.items()}
        print(temp[key_binding[0]] + "+" + temp[key_binding[1]])


def main():
    global key_binding
    parser = argparse.ArgumentParser()
    help = """Set alternate key binding. Default is LCTRL+SPACE
                Format :- <KEY1>+<KEY2>. Ex:- RCTRL+RALT
                To see availble key bindings use 'clix -a' option"""
    parser.add_argument("-s", "--set-keybinding", type=str,
                        default="LCTRL+SPACE", help=help)
    parser.add_argument("-a", "--available-keybindings",
                        help="Show available key bindings", action="store_true")
    parser.add_argument("-c", "--show-current-keybinding", action="store_true")
    args = parser.parse_args()
    args_dict = vars(args)
    if args.show_current_keybinding is True:
        _show_current_keybinding()
        sys.exit()
    if args.available_keybindings is True:
        _show_available_keybindings()
        sys.exit()
    if args_dict['set_keybinding'] is not "LCTRL+SPACE":
        try:
            key_binding = [available_keys[args_dict['set_keybinding'].split(
                '+')[0]], available_keys[args_dict['set_keybinding'].split('+')[1]]]
        except KeyError:
            print("Please follow the correct format.")
        finally:
            with open("config", "wb") as f:
                pickle.dump(key_binding, f, protocol=2)
            sys.exit()

    new_hook = HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.HookKeyboard()
    new_hook.start()


if __name__ == "__main__":
    main()
