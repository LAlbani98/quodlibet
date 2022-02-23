from quodlibet import _
from quodlibet import app
from quodlibet.qltk import Icons
from quodlibet.plugins.events import EventPlugin


class ReturnToStart(EventPlugin):
    PLUGIN_ID = "return_to_start"
    PLUGIN_NAME = _("Return to Start")
    PLUGIN_DESC = _(
        "Seeks to the beginning of the album when it ends, without playing.")
    PLUGIN_ICON = Icons.MEDIA_PLAYBACK_PAUSE

    DBUS_NAME = "org.gnome.ReturnToStart"
    DBUS_INTERFACE = "org.gnome.ReturnToStart"
    DBUS_PATH = "/org/gnome/ReturnToStart"

    def plugin_on_song_started(self, song):
        """When an album or playlist ends we should return to the start, but not play"""
        if song is None:
            app.player.next()
            app.player.paused = True
