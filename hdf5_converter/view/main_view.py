#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: HDF5 Converter
# File: hdf5_converter/view/main_view.py
# ----------------------------------------------------------------------------------
# Purpose:
# This is the main file of the controller package, and it is used to initialise the
# Hdf5 Converter controller.
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

from hdf5_converter.view.converter_view import ConverterView
from hdf5_converter.view.status_view import StatusView


class MainView(wx.Frame):
    """This class is responsible for displaying the main HDF5 Converter GUI."""

    def __init__(self) -> None:
        super(MainView, self).__init__(parent=None, style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)

        # Helper variables
        self._terminated = False
        self._worker_finished = False

        # Create the widgets
        self.main_panel = FlatPanel(self)
        self.converter_view = ConverterView(self.main_panel)
        self.status_view = StatusView(self.main_panel)

        # Run the configuration methods
        self._configure_view()
        self._layout()
        self.Bind(wx.EVT_CLOSE, self._on_close)

    def _configure_view(self) -> None:
        """Configures the main view of the HDF5 Converter GUI."""
        # Set the size of the main window
        self.SetMinSize(wx.Size(800, 600))

    def _layout(self) -> None:
        """Sets the layout of the main view."""
        # Set the layout of the main panel
        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        panel_sizer.Add(self.converter_view, 0, wx.EXPAND)
        panel_sizer.Add(self.status_view, 1, wx.EXPAND)
        self.main_panel.SetSizer(panel_sizer)

        frame_sizer = wx.BoxSizer(wx.VERTICAL)
        frame_sizer.Add(self.main_panel, 1, wx.EXPAND)
        self.SetSizer(frame_sizer)

    def display_window(self) -> None:
        """Sets the title and displays the main window."""
        # Set the window title
        self.SetTitle("HDF5 Converter")

        # Display the main window
        self.Show()

    def _on_close(self, event: wx.CloseEvent) -> None:
        """Creates a message box for exit confirmation if the window is closed."""
        dlg = wx.MessageDialog(self, "Are you sure you want to close the application?", "Exit confirmation", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self._terminated = True
            while not self._worker_finished:
                wx.SafeYield()
            event.Skip()
        else:
            event.Veto()
        dlg.Destroy()

    @property
    def terminated(self) -> bool:
        return self._terminated

    @property
    def worker_finished(self) -> bool:
        return self._worker_finished

    @worker_finished.setter
    def worker_finished(self, value: bool) -> None:
        self._worker_finished = value
