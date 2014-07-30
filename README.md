AutoHideSidebar
===============

[Sublime Text 3](http://www.sublimetext.com/) plugin to automatically hide and
show the sidebar as you type, save and navigate. Untested with ST2, but may
work too.

Usage
-----

The plugin watches for modifications on the current open file. After the
current file is modified by a certian number of keystrokes (defaults to 5)
the sidebar will automatically hide.

A hidden sidebar will then automatically be shown when:

* the current file is saved
* the current file is closed
* a new file is created
* a file is loaded
* a file is cloned
* current active file/tab changes

Credit
------

Parts of this code are borrowed or based on Przemek Sobstel's 
[SyncedSideBar](https://github.com/sobstel/SyncedSideBar) plugin.

License
-------

GNU GENERAL PUBLIC LICENSE v2.0