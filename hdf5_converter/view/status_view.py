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

from gsewidgets import TextInfoBox, HorizontalLine
from qtpy.QtWidgets import QFrame, QVBoxLayout
from qtpy.QtCore import QObject, Signal


class StatusView(QFrame):
    """Creates the status view of the HDF5 Converter GUI."""

    update_status = Signal(str)

    def __init__(self) -> None:
        """Initialises the status view."""
        super(StatusView, self).__init__()

        self.txt_info = TextInfoBox()
        self._line_number = 0

        # Set the layout of the status view
        self.update_status.connect(self._add_status_message)
        self._layout()

    def _add_status_message(self, message: str) -> None:
        """Adds a status message to the status view."""
        self._line_number += 1
        self.txt_info.append(f"{self._line_number}. {message}")

    def clear(self) -> None:
        """Clears the status view."""
        self.txt_info.clear()
        self._line_number = 0

    def _layout(self) -> None:
        """Sets the layout of the status view."""
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(HorizontalLine())
        layout.addWidget(self.txt_info)

        # Set the layout to the status view
        self.setLayout(layout)
