#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: HDF5 Converter
# File: hdf5_converter/view/status_view.py
# ----------------------------------------------------------------------------------
# Purpose:
# This is the status view of the HDF5 Converter GUI. It is responsible for
# displaying the status messages and progress of the conversion process.
# ----------------------------------------------------------------------------------
# Author: Christofanis Skordas
#
# Copyright (c) 2025 GSECARS, The University of Chicago
# Copyright (c) 2025 NSF SEES, Synchrotron Earth and Environmental Science
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
# ----------------------------------------------------------------------------------

import wx
from wxutils import FlatPanel
from wxutils.themes import get_theme


class StatusView(FlatPanel):
    """Creates the status view of the HDF5 Converter GUI."""

    def __init__(self, parent: wx.Window) -> None:
        """Initialises the status view."""
        super(StatusView, self).__init__(parent)

        theme = get_theme()
        self.SetBackgroundColour(theme.background)

        self.txt_info = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_NONE)
        self.txt_info.SetBackgroundColour(theme.bright_black)
        self.txt_info.SetForegroundColour(theme.foreground)
        self._line_number = 0

        # Set the layout of the status view
        self._layout()

    def add_status_message(self, message: str) -> None:
        """Adds a status message to the status view."""
        self._line_number += 1
        self.txt_info.AppendText(f"{self._line_number}. {message}\n")

    def clear(self) -> None:
        """Clears the status view."""
        self.txt_info.Clear()
        self._line_number = 0

    def _layout(self) -> None:
        """Sets the layout of the status view."""
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND)
        sizer.Add(self.txt_info, 1, wx.EXPAND)
        self.SetSizer(sizer)
