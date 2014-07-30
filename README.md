AutoHideSidebar
===============

AutoHideSidebar is a [Sublime Text 3](http://www.sublimetext.com/) plugin that
will automatically hide and show the sidebar as you type, save and navigate.
Untested with ST2, but may work too.

The plugin watches for modifications on the currently open file. After the
current file is modified by a certian number of keystrokes (defaults to 10)
the sidebar will automatically hide.

Once the sidebar is hidden, it will automatically be shown when:

* the current file is saved
* the current file is closed
* a new file is created
* a file is loaded
* a file is cloned
* current active file/tab changes
* the app gains or loses focus

Installation
------------

Plugin is not yet in package management, so you will need to `git clone` the
repo in to your ST3 directory for now.

Configuration
-------------

The default behaviour can be overridden by settings in your preferences:

#### hide_sidebar_change_count_trigger

The number of change keystrokes required before the sidebar automatically
hides.  The default is `10`. It can be changed like this:

```json
{ "hide_sidebar_change_count_trigger": 5 }
```

Now the sidebar will hide after 5 change keystrokes.

#### show_sidebar_on_activated

If the sidebar is hidden, automatically show it when a file/tab gains focus.
This will trigger when the currently open tab changes or when the app window
itself gains or loses focus. Default is `true`, can be changed like this:

```json
{ "show_sidebar_on_activated": false }
```

Now the sidebar will not automatically show when focus changes.

#### show_sidebar_on_new

If the sidebar is hidden, automatically show it when a new file is created
with File Menu -> New File or Command-N/Super-N/Ctrl-N. Default is `true`, can
be changed like this:

```json
{ "show_sidebar_on_new": false }
```

Now the sidebar will not automatically show when a new file is created.

#### show_sidebar_on_clone

If the sidebar is hidden, automatically show it when a clone is created
from a file. Default is `true`, can be changed like this:

```json
{ "show_sidebar_on_clone": false }
```

Now the sidebar will not automatically show when a file is cloned.

#### show_sidebar_on_load

If the sidebar is hidden, automatically show it when a file is loaded
with File Menu -> Open or Command-T/Super-T/Ctrl-T. Default is `true`, can
be changed like this:

```json
{ "show_sidebar_on_load": false }
```

Now the sidebar will not automatically show when a new file is created.

#### show_sidebar_on_save

If the sidebar is hidden, automatically show it when a file is saved with
File Menu -> Save or Command-S/Super-S/Ctrl-S or when "save_on_focus_lost" is
triggered. Default is `true`, can be changed like this:

```json
{ "show_sidebar_on_save": false }
```

Now the sidebar will not automatically show when a file is saved.

#### show_sidebar_on_close

If the sidebar is hidden, automatically show it when an open file is closed with
File Menu -> Close File or Command-W/Ctrl-F4. Default is `true`, can be
changed like this:

```json
{ "show_sidebar_on_close": false }
```

Now the sidebar will not automatically show when a file is closed.

Changelog
---------

*1.0*, *July 31, 2014*

Initial release.

Credit
------

Parts of this code are borrowed or based on Przemek Sobstel's 
[SyncedSideBar](https://github.com/sobstel/SyncedSideBar) plugin.

License
-------

GNU GENERAL PUBLIC LICENSE v2.0