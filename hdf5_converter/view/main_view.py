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

from qtpy.QtWidgets import QMainWindow


class MainView(QMainWindow):
    """This class is responsible for displaying the main HDF5 Converter GUI."""

    def __init__(self) -> None:
        super(MainView, self).__init__()

    def display_window(self) -> None:
        """Sets the title and displays the main window."""
        # Set the window title
        self.setWindowTitle("HDF5 Converter")

        # Display the main window
        self.showNormal()
