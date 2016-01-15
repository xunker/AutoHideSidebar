AutoHideSidebar
===============

AutoHideSidebar is a [Sublime Text 3](http://www.sublimetext.com/) package that
will automatically hide and show the sidebar as you type, save and navigate.
Untested with ST2, but may work too.

AutoHideSidebar watches for modifications on the currently open file. After the
current file is modified by a certain number of keystrokes (defaults to 10)
the sidebar will automatically hide.

Once the sidebar is hidden, it will automatically be shown when:

* The current file is saved.
* A file is loaded or cloned.
* A new tab is opened.
* An open tab is closed.
* The Current active tab changes.
* The app gains or loses focus.

Only keystrokes that add, remove or change text in the current tab ("change"
keystrokes) will hide the sidebar. Other keystrokes, such arrow keys, will not
cause the sidebar to hide.

Installation
------------

AutoHideSidebar is not yet in Sublime Package Control so you will need to add
it manually by downloading `AutoHideSidebar.py` in to the User Packages
directory. On OS X this defaults to `~/Library/Application Support/Sublime Text 3/Packages/User`
but may vary on other operating systems.

It has been [submitted to Package Control](https://github.com/wbond/package_control_channel/pull/5133) and will (hopefully)
be available there soon.

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

####  autohide_sidebar_verbose_logging

Toggle event and debugging messages being written to the console. Default is
`false`, can be changed like this:

```json
{ "autohide_sidebar_verbose_logging": true }
```

Changelog
---------

*1.0.1*, Jan 15, 2016*

Fixed errant logging message that would print to the console regardless of the
value of `autohide_sidebar_verbose_logging`.

Added documentation on the `autohide_sidebar_verbose_logging` config option.

Submitted to be included in [Sublime Package Control](https://github.com/wbond/package_control_channel/pull/5133).

*1.0*, *July 31, 2014*

Initial release.

Credit
------

Parts of this code are borrowed or based on Przemek Sobstel's
[SyncedSideBar](https://github.com/sobstel/SyncedSideBar) package.

License
-------

GNU GENERAL PUBLIC LICENSE v2.0