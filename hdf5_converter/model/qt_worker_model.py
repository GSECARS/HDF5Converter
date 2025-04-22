#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: HDF5 Converter
# File: hdf5_converter/model/qt_worker_model.py
# ----------------------------------------------------------------------------------
# Purpose:
# This is the qt worker model of the HDF5 Converter GUI. It is responsible for
# creating a worker thread that handles the conversion processes.
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

from qtpy.QtCore import QThread
from typing import Callable, Any


class QtWorkerModel(QThread):
    """This class is responsible for creating a worker thread that handles the conversion processes."""

    def __init__(self, method: Callable, args: Any) -> None:
        """Initialises the qt worker model."""
        super(QtWorkerModel, self).__init__()
        self._method = method
        self._args = args

    def run(self) -> None:
        """Runs the worker thread."""
        self._method(*self._args)
