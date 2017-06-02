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

Usage
-----

-  To run clix, open terminal and run this command:

   ::

       $ clix

   **Note:** Leave this terminal open as long as you want to use
   **clix**.

-  Press **Ctrl** + **space** keys to open clix GUI. Initially, all clip
   frames are empty.

-  Now, as you copy any text, (using **Ctrl** + **c** keys), the text is
   saved to topmost frame of clix clipboard.

-  Whenever you want to paste any clip, just open clix GUI (usin
   **Ctrl** + **space** keys) and click on **clip it** button to copy
   clip text to main clipboard.

Now, simply pressing **Ctrl** + **v** keys will paste the desired clip
text!

TODO
----

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

Finally, do report bugs and help us make **clix** more and more
productive!

.. |PyPI| image:: https://img.shields.io/badge/PyPi-v1.0.2-f39f37.svg
   :target: https://pypi.python.org/pypi/clix
.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000
   :target: https://github.com/nikhilkumarsingh/clix/blob/master/LICENSE.txt
