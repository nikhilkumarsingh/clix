import os
import sys
import json
import xerox
import pickle
import argparse
import threading
try:
    import utils
except:
    import clix.utils as utils
from pyxhook import HookManager
from gui import clipboard

# previously logged key
prev_Key = None
# path to site package
curr_dir = os.getcwd()

key_binding = []

# loading key_binding from config file
# try:
with open(os.path.join(os.path.dirname(__file__), 'config'), "rb") as f:
    key_binding = pickle.load(f)

# if file does not exist create empty file
try:
    clips_data = open(os.path.join(os.path.dirname(__file__),
                      'clips_data'), "rb")
    utils.clips = pickle.load(clips_data)
    clips_data.close()
except:
    utils.clips = []


class ThreadedKeyBind(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.new_hook = HookManager()
        self.new_hook.KeyDown = self.OnKeyPress
        self.new_hook.HookKeyboard()
        self.new_hook.start()
        # self.new_hook.cancel()

    def OnKeyPress(self, event):
        """
        function called when any key is pressed
        """
        global prev_Key, key_binding

        if event.Key == key_binding[1] and prev_Key == key_binding[0]:
            if utils.active == 1:
                utils.active = 0
            elif utils.active == 0:
                utils.active = 1
            prev_Key = None

        elif event.Key == 'c' and prev_Key == 'Control_L':
            self.text = xerox.paste(xsel=True)
            utils.clips.append(self.text)
            # pickle clips data
            with open(os.path.join(os.path.dirname(__file__),
                      'clips_data'), "wb") as f:
                pickle.dump(utils.clips, f, protocol=2)

            print("You just copied: {}".format(self.text))

        elif event.Key == 'z' and prev_Key == 'Control_L':
            print("can")
            self.new_hook.cancel()

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
    with open(os.path.join(os.path.dirname(__file__),
              'clips_data'), "wb") as f:
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
            with open(os.path.join(os.path.dirname(__file__),
                      'config'), "wb") as f:
                pickle.dump(key_binding, f, protocol=2)
        finally:
            sys.exit()

    elif args.new_session:
        print("new session")
        create_new_session()

    # seperate thread because of tkinter mainloop
    # which blocks every other event
    t = ThreadedKeyBind().start()

    # start gui
    utils.active = 1
    clipboard(utils.clips)


if __name__ == "__main__":
    main()
