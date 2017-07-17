|PyPI| |license|

clix
====

An easy to use clipboard manager made using tkinter.

.. figure:: https://media.giphy.com/media/l0IymVaUaR5xGRQHK/giphy.gif
   :alt: 

**Note:** Currently, clix works only on **Linux** systems.

Installation
------------

-  To install clix, simply,

   ::

       $ pip install clix

-  If you get ``ImportError`` for Xlib module, install it using this
   command:

   ::

       $ sudo apt-get install python-xlib

Usage
-----

-  To run clix, open terminal and run this command:

   ::

       $ clix

   if error shown try:

   ::

       $ sudo clix

**Note:** Leave this terminal open as long as you want to use **clix**.

Another alternative is to use this command:

``$ nohup clix &``

Now, you can close the terminal but **clix** will keep running.

To close clix, open a terminal and simply run:

``$ pkill clix``

-  Press **Ctrl** + **space** keys to open clix GUI. Initially, all clip
   frames are empty.

-  Now, as you copy any text, (using **Ctrl** + **c** keys), the text is
   saved to topmost frame of clix clipboard.

-  Whenever you want to paste any clip, just open clix GUI (usin
   **Ctrl** + **space** keys) and click on **clip it** button to copy
   clip text to main clipboard.

Now, simply pressing **Ctrl** + **v** keys will paste the desired clip
text!

-  **CLI usage to configure keys**

   ::

       $ clix [-h] [-s SET_KEYBINDING] [-a] [-c]

   You can always use ``$ clix -h`` command to open this help message:

   ::

       optional arguments:
         -h, --help            show this help message and exit
         -s SET_KEYBINDING, --set-keybinding SET_KEYBINDING
                               Set alternate key binding. Default is LCTRL+SPACE
                               Format :- <KEY1>+<KEY2>. Ex:- RCTRL+RALT. To see
                               availble key bindings use 'clix -a' option
         -a, --available-keybindings
                               Show available key bindings
         -c, --show-current-keybinding

TODO
----

-  [X] Add support for user configurable keys.

-  [ ] Add support for Windows and MacOS.

-  [ ] Create a file system to log the clipboard.

-  [ ] Improve UI.

-  [ ] Add more functionalities.

Want to contribute?
-------------------

-  Clone the repository

   ::

       $ git clone http://github.com/nikhilkumarsingh/clix

-  Install dependencies

   ::

       $ pip install -r requirements.txt

-  Remove the ``.`` prefix from ``.pyxhook`` and ``.gui`` for the
   following imports in **clix.py**, so it changes from:

   .. code:: python

       from .pyxhook import HookManager
       from .gui import clipboard

   to:

   .. code:: python

       from pyxhook import HookManager
       from gui import clipboard

-  To test local version of clix:

   ::

       $ pip install -U .

Finally, do report bugs and help us make **clix** more and more
productive!

.. |PyPI| image:: https://img.shields.io/badge/PyPi-v1.0.8-f39f37.svg
   :target: https://pypi.python.org/pypi/clix
.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000
   :target: https://github.com/nikhilkumarsingh/clix/blob/master/LICENSE.txt
