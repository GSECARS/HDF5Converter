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

from gsewidgets import TextInfoBox
from qtpy.QtWidgets import QFrame, QVBoxLayout


class StatusView(QFrame):
    """Creates the status view of the HDF5 Converter GUI."""
    
    def __init__(self) -> None:
        """Initialises the status view."""
        super(StatusView, self).__init__()

        self.txt_info = TextInfoBox()

        # Set the layout of the status view
        self._layout()

    def _layout(self) -> None:
        """Sets the layout of the status view."""
        layout = QVBoxLayout()
        layout.addWidget(self.txt_info)

        # Set the layout to the status view
        self.setLayout(layout)

