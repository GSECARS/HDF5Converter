#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: HDF5 Converter
# File: hdf5_converter/controller/__init__.py
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

from hdf5_converter.controller.main_controller import MainController


__all__ = ["MainController"]
