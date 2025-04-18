#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: HDF5 Converter
# File: hdf5_converter/controller/converter_controller.py
# ----------------------------------------------------------------------------------
# Purpose:
# This file is the converter controller of the HDF5 Converter GUI. It is responsible
# for handling the conversion process and connecting the view and model.
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

from hdf5_converter.view import MainView
from hdf5_converter.model import MainModel



class ConverterController:
    
    def __init__(self, view: MainView, model: MainModel) -> None:
        """Initialize the converter controller with the view and model."""
        self._view = view
        self._model = model

        # Connect signals to slots
        self._connect_signals()

    def _connect_signals(self) -> None:
        """Connect signals from the view to the model."""
        # Connect the convert button signal to the model's convert method
        self._view.converter_view.btn_convert.clicked.connect(self._on_convert_button_clicked)

    def _on_convert_button_clicked(self) -> None:
        """Handle the convert button click event."""
        
        format = self._view.converter_view.cmb_output_type.currentText()
        digits = self._view.converter_view.spin_digits.value()
        input_files = self._view.converter_view.btn_input.file_path

        print(f"Input files: {input_files}")
        print(f"Output format: {format}")
        print(f"Number of digits: {digits}")

        # Call the model's save_data method to perform the conversion
        for file_name in input_files:
            self._model.converter.process(file_name=file_name, digits=digits, output_type=format, search_term="data")
        
        