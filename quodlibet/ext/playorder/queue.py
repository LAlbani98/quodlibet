# Copyright 2009 Steven Robertson
#        2016-20 Nick Boultbee
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

from quodlibet import _
from quodlibet import app
from quodlibet.plugins.playorder import ShufflePlugin
from quodlibet.qltk import Icons
from quodlibet.qltk.playorder import OrderInOrder


class QueueOrder(ShufflePlugin, OrderInOrder):
    PLUGIN_ID = "queue"
    PLUGIN_NAME = _("Queue Only")
    PLUGIN_ICON = Icons.VIEW_LIST
    PLUGIN_DESC = _("Limits playing of songs to the queue.\n\n"
                    "Select this play order in the main window, "
                    "then double-clicking any song will enqueue it "
                    "instead of playing.")
    display_name = _("Queue only")
    accelerated_name = _("_Queue only")

    def next(self, playlist, iter):
        return None

    def set_explicit(self, playlist, iter):
        if iter is None:
            return
        song = playlist[iter][0]
        if song is None:
            return
        app.window.playlist.enqueue([playlist[iter][0]])
