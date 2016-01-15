# Automatically hide the sidebar after the file in the current view is
# modified XX times (default 5).
#
# Much code borrowed from SyncedSideBar: https://github.com/sobstel/SyncedSideBar
import sublime, sublime_plugin

PLUGIN_NAME = 'AutoHideSidebar'

# assume sidebar is visible by default on every window (there's no way to check, unfortunately)
DEFAULT_VISIBILITY = True
windowSidebarVisible = {}

CHANGE_COUNT_TRIGGER_KEY = 'hide_sidebar_change_count_trigger'
change_count_trigger = 10 # default, can be changed in prefs with above key
change_counter = 0

# preferences key, default value/current calue
behaviours = {
  'show_sidebar_on_activated': True,
  'show_sidebar_on_new': True,
  'show_sidebar_on_clone': True,
  'show_sidebar_on_load': True,
  'show_sidebar_on_save': True,
  'show_sidebar_on_close': True,
  'autohide_sidebar_verbose_logging': False
}

def shouldTrigger(pref_key):
  global behaviours
  return not not behaviours[pref_key]

def log(msg):
  if shouldTrigger('autohide_sidebar_verbose_logging'):
    named_print(msg)

def named_print(msg):
  print("%s: %s" % (PLUGIN_NAME, msg))

def plugin_loaded():
  s = sublime.load_settings('%s.sublime-settings' % PLUGIN_NAME)

  def read_pref():
    log("reading prefs")
    settings = sublime.load_settings("Preferences.sublime-settings")

    global change_count_trigger
    if settings.get(CHANGE_COUNT_TRIGGER_KEY):
      change_count_trigger = int(settings.get(CHANGE_COUNT_TRIGGER_KEY))
      log("%s: %i" % (CHANGE_COUNT_TRIGGER_KEY, change_count_trigger))
    else:
      log("using default %s: %i" % (CHANGE_COUNT_TRIGGER_KEY, change_count_trigger))

    global behaviours
    for index, pref_key in enumerate(behaviours.keys()):
      if settings.get(pref_key) == None:
        log("using default %s: %s" % (pref_key, behaviours[pref_key]))
      else:
        behaviours[pref_key] = not not settings.get(pref_key)
        log("using user preference for %s: %s" % (pref_key, behaviours[pref_key]))

  # read initial setting
  read_pref()

# ST2 backwards compatibility
if (int(sublime.version()) < 3000):
    plugin_loaded()

class AutoHideSidebarListener(sublime_plugin.EventListener):
  def on_modified_async(self, view):
    # crufty way to detect if sidebar can even be shown
    if view.window() and len(view.window().folders()) > 0:
      if not view.window().id() in windowSidebarVisible:
        windowSidebarVisible[view.window().id()] = DEFAULT_VISIBILITY
      if windowSidebarVisible[view.window().id()]:
        global change_counter
        change_counter += 1
        log("change_counter: %i/%i" % (change_counter, change_count_trigger))
        if change_counter == change_count_trigger:
          log("change_counter reached maximum of %i." % change_count_trigger)
          self.hide_sidebar(view)
      else:
        log("Sidebar already hidden")

  def on_activated_async(self, view):
    if shouldTrigger('show_sidebar_on_activated'):
      self.show_sidebar_and_reset_count(view)

  def on_new_async(self, view):
    if shouldTrigger('show_sidebar_on_new'):
      self.show_sidebar_and_reset_count(view)

  def on_clone_async(self, view):
    if shouldTrigger('show_sidebar_on_clone'):
      self.show_sidebar_and_reset_count(view)

  def on_load_async(self, view):
    if shouldTrigger('show_sidebar_on_load'):
      self.show_sidebar_and_reset_count(view)

  def on_pre_save_async(self, view):
    if shouldTrigger('show_sidebar_on_save'):
      self.show_sidebar_and_reset_count(view)

  def on_close(self, view):
    if shouldTrigger('show_sidebar_on_close'):
      self.show_sidebar_and_reset_count(view)

  def show_sidebar_and_reset_count(self, view):
    self.reset_count()
    self.show_sidebar(view)

  def reset_count(self):
    log("Resetting counter to zero (trigger is %i)" % change_count_trigger)
    global change_counter
    change_counter = 0

  def hide_sidebar(self, view):
    if not view.window().id() in windowSidebarVisible:
      windowSidebarVisible[view.window().id()] = DEFAULT_VISIBILITY
    if windowSidebarVisible[view.window().id()]:
      if view.window():
        log("Hiding sidebar")
        view.window().run_command("toggle_side_bar")
      else:
        log("No window, can't show sidebar")
    else:
      log("Sidebar already hidden")

  def show_sidebar(self, view):
    if view.window():
      if not view.window().id() in windowSidebarVisible:
        windowSidebarVisible[view.window().id()] = DEFAULT_VISIBILITY
      if windowSidebarVisible[view.window().id()]:
        log("Sidebar already visible")
      else:
        if view.window():
          log("Showing sidebar")
          view.window().run_command("toggle_side_bar")
        else:
          log("No window, can't show sidebar")
    else:
      log("No window, can't show sidebar")

  def on_window_command(self, window, command_name, args):
    # crufty way to detect if sidebar can even be shown
    if len(window.folders()) > 0:
      if command_name == "toggle_side_bar":
        global windowSidebarVisible
        if not window.id() in windowSidebarVisible:
          windowSidebarVisible[window.id()] = DEFAULT_VISIBILITY

        log("toggle_side_bar command reported")
        windowSidebarVisible[window.id()] = not windowSidebarVisible[window.id()]
        log("sidebarVisible: %s" % windowSidebarVisible[window.id()])

        self.reset_count()
