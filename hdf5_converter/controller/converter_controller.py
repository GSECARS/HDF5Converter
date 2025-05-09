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

import time
from concurrent.futures import ThreadPoolExecutor

from qtpy.QtCore import Signal, QObject

from hdf5_converter.view import MainView
from hdf5_converter.model import MainModel


class ConverterController(QObject):
    """This class is responsible for handling the conversion process."""

    convertion_signal = Signal()

    def __init__(self, view: MainView, model: MainModel) -> None:
        """Initialize the converter controller with the view and model."""
        super(ConverterController, self).__init__()
        self._view = view
        self._model = model
        self._converting = False
        self._processing = False

        # Connect signals to slots
        self._connect_signals()

    def _connect_signals(self) -> None:
        """Connect signals from the view to the model."""
        # Connect the convert button signal to the model's convert method
        self._view.converter_view.btn_convert.clicked.connect(self._trigger_conversion)
        self._model.converter.new_status.connect(self._update_status_message)
        self.convertion_signal.connect(self._prepare_for_convertion)

    def convert_files(self) -> None:
        """Handle the conversion process."""

        format = self._view.converter_view.cmb_output_type.currentText()
        search_term = self._view.converter_view.input_search_term.text()
        digits = self._view.converter_view.spin_digits.value()
        input_files = self._view.converter_view.btn_input.file_path

        self._processing = True
        start_time = time.time()

        # Convert the files using a thread pool
        with ThreadPoolExecutor() as executor:
            futures = []
            for file in input_files:
                future = executor.submit(self._model.converter.process, file, search_term, format, digits)
                futures.append(future)

            for future in futures:
                try:
                    # Wait for the future to complete and handle any exceptions
                    future.result()
                except Exception as e:
                    self._view.status_view.update_status.emit(f"Error processing file: {e}")

        # Print the total time taken to convert the files in minutes or seconds based on the time taken
        end_time = time.time()
        total_time = end_time - start_time
        if total_time < 60:
            self._view.status_view.update_status.emit(f"Conversion completed in {total_time:.2f} seconds.")
        else:
            self._view.status_view.update_status.emit(f"Conversion completed in {int(total_time // 60)} minutes and {total_time % 60:.2f} seconds.")

    def _prepare_for_convertion(self) -> None:
        """Prepare the view for conversion by disabling the widgets and updating the status message."""
        # Disable the conversion widgets
        self._view.converter_view.togge_widget_status(False)

        # Clear the status view
        self._view.status_view.clear()

        # Provide the initial message for the conversion starting and on what files
        self._view.status_view.update_status.emit("Files to be converted:")
        self._view.status_view.update_status.emit("--------------------------------------------------")
        # Get the input files from the view
        input_files = self._view.converter_view.btn_input.file_path
        for file in input_files:
            self._view.status_view.update_status.emit(file)
        self._view.status_view.update_status.emit("--------------------------------------------------")
        # Provide the message for the conversion starting
        self._view.status_view.update_status.emit("Conversion in progress...")

    def restore_after_convertion(self) -> None:
        """Restore the view after conversion is complete."""
        # Restore the conversion widgets
        self._view.converter_view.togge_widget_status(True)
        # Restore the helpers
        self._converting = False
        self._processing = False

    def _update_status_message(self) -> None:
        """Update the status message in the view."""
        self._view.status_view.update_status.emit(self._model.converter.status_message)

    def _trigger_conversion(self) -> None:
        """Trigger the conversion process."""
        self._converting = True

    @property
    def converting(self) -> bool:
        """Check if the conversion process is currently running."""
        return self._converting

    @property
    def processing(self) -> bool:
        """Check if the conversion process is currently running."""
        return self._processing
