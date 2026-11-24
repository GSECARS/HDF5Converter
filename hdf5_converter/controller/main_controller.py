#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: HDF5 Converter
# File: hdf5_converter/controller/main_controller.py
# ----------------------------------------------------------------------------------
# Purpose:
# This file is used to start the HDF5 Converter application.
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

import time

import wx

from hdf5_converter.view import MainView
from hdf5_converter.model import MainModel, WorkerModel
from hdf5_converter.controller.converter_controller import ConverterController


class MainController:
    """This class is responsible for controlling the main application."""

    def __init__(self) -> None:
        self._app = wx.App()
        self._view = MainView()
        self._model = MainModel()

        # Initialize the converter controller
        self._converter_controller = ConverterController(self._view, self._model)

        # Initialize the worker model
        self._worker_model = WorkerModel(self._worker_methods, ())  # Ensure worker runs in a separate thread
        self._worker_model.start()

    def run(self) -> None:
        """Runs the main application."""
        # Display the main view
        self._view.display_window()

        # Start the wx app event loop
        self._app.MainLoop()

    def _worker_methods(self) -> None:
        """This method is responsible for running the worker methods."""

        # Run the conversion process
        while not self._view.terminated:

            if self._converter_controller._converting:
                if not self._converter_controller.processing:
                    wx.CallAfter(self._converter_controller._prepare_for_convertion)
                    self._converter_controller.convert_files()

                self._converter_controller.restore_after_convertion()

            time.sleep(0.1)

        # Set as finished so the GUI can exit
        self._view.worker_finished = True
