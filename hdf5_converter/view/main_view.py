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

from qtpy.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QMessageBox
from qtpy.QtCore import Qt
from qtpy.QtGui import QCloseEvent

from hdf5_converter.view.converter_view import ConverterView
from hdf5_converter.view.status_view import StatusView


class MainView(QMainWindow):
    """This class is responsible for displaying the main HDF5 Converter GUI."""

    def __init__(self) -> None:
        super(MainView, self).__init__()

        # Create the widgets
        self.converter_view = ConverterView()
        self.status_view = StatusView()

        # Helper variables
        self._terminated = False
        self._worker_finished = False

        # Run the configuration methods
        self._configure_view()
        self._layout()

    def _configure_view(self) -> None:
        """Configures the main view of the HDF5 Converter GUI."""
        # Set the size of the main window
        self.setMinimumSize(800, 600)

        # Set the window flags
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # Main frame
        self.main_frame = QFrame()
        self.setCentralWidget(self.main_frame)

    def _layout(self) -> None:
        """Sets the layout of the main view."""
        # Set the layout of the main frame
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.converter_view)
        layout.addWidget(self.status_view)

        self.main_frame.setLayout(layout)

    def display_window(self) -> None:
        """Sets the title and displays the main window."""
        # Set the window title
        self.setWindowTitle("HDF5 Converter")

        # Display the main window
        self.showNormal()

    def closeEvent(self, event: QCloseEvent) -> None:
        """Creates a message box for exit confirmation if closeEvent is triggered."""
        _msg_question = QMessageBox.question(self, "Exit confirmation", "Are you sure you want to close the application?")

        if _msg_question == QMessageBox.Yes:

            self._terminated = True

            while not self._worker_finished:
                continue

            event.accept()
        else:
            event.ignore()

    @property
    def terminated(self) -> bool:
        return self._terminated
