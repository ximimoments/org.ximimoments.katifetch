# window.py
#
# Copyright 2026 katifetchtest
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import gi
# Le decimos explícitamente al sistema que use WebKit para GTK 4
gi.require_version('WebKit', '6.0')

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import WebKit # Importamos la versión compatible con GTK 4

@Gtk.Template(resource_path='/org/ximimoments/katifetch/window.ui')
class KatifetchWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'KatifetchWindow'

    scrolled_window = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Usamos WebKit.WebView() en lugar de WebKit2
        self.webview = WebKit.WebView()

        self.webview.load_uri("https://kfetchweb.valentinomartinezferreira456.workers.dev/")

        self.scrolled_window.set_child(self.webview)
