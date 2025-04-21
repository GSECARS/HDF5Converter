#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: HDF5 Converter
# File: hdf5_converter/view/converter_view.py
# ----------------------------------------------------------------------------------
# Purpose:
# This is the converter view of the HDF5 Converter GUI. It is responsible for
# displaying the converter view, which includes the file selection, conversion
# options, and the conversion button.
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

from gsewidgets import Label, SimpleButton, MultiFileBrowserButton, NumericSpinBox, FullComboBox, InputBox
from qtpy.QtCore import QSize
from qtpy.QtWidgets import QFrame, QGridLayout, QHBoxLayout


class ConverterView(QFrame):
    """Creates the converter view of the HDF5 Converter GUI."""

    def __init__(self) -> None:
        """Initialises the converter view."""
        super(ConverterView, self).__init__()

        # Create the widgets
        self.btn_input = MultiFileBrowserButton(text="Load File(s)", file_extensions=["h5", "hdf5", "mh5", "ph5"])
        self.lbl_digits = Label("Number of Digits")
        self.spin_digits = NumericSpinBox(min_value=1, max_value=10, default_value=3, incremental_step=1, size=QSize(32, 32))
        self.btn_convert = SimpleButton("Convert", size=QSize(250, 100))
        self.lbl_output_type = Label("Output Type")
        self.cmb_output_type = FullComboBox()
        self.lbl_search_term = Label("Dataset Search Term")
        self.input_search_term = InputBox(placeholder="Enter search term", size=QSize(200, 32))

        # Configure the widgets
        self._configure_widgets()

        # Set the layout of the converter view
        self._layout()

    def _configure_widgets(self) -> None:
        """Configures the widgets of the converter view."""
        # Set the default output type
        self.cmb_output_type.addItem("tiff")
        self.cmb_output_type.addItem("cbf")
        self.cmb_output_type.setCurrentIndex(0)

        self.btn_input.clicked.connect(self._update_load_file_button)

        # Set the default search term value
        self.input_search_term.setText("data")

    def _update_load_file_button(self) -> None:
        """Updates the load file button with the selected file paths."""
        if self.btn_input.file_path:
            self.btn_input.setText(f"Loaded {len(self.btn_input.file_path)} File(s)")
        else:
            self.btn_input.setText("Load File(s)")

    def _layout(self) -> None:
        """Sets the layout of the converter view."""

        layout_digits = QHBoxLayout()
        layout_digits.setContentsMargins(0, 0, 0, 0)
        layout_digits.setSpacing(0)
        layout_digits.addWidget(self.lbl_digits)
        layout_digits.addWidget(self.spin_digits)

        layout_output_type = QHBoxLayout()
        layout_output_type.setContentsMargins(0, 0, 0, 0)
        layout_output_type.setSpacing(0)
        layout_output_type.addWidget(self.lbl_output_type)
        layout_output_type.addWidget(self.cmb_output_type)

        layout_search_term = QHBoxLayout()
        layout_search_term.setContentsMargins(0, 0, 0, 0)
        layout_search_term.setSpacing(0)
        layout_search_term.addWidget(self.lbl_search_term)
        layout_search_term.addWidget(self.input_search_term)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.btn_input, 0, 0, 1, 3)
        layout.addLayout(layout_search_term, 1, 0, 1, 1)
        layout.addLayout(layout_digits, 1, 1, 1, 1)
        layout.addLayout(layout_output_type, 1, 2, 1, 1)
        layout.setColumnStretch(3, 1)
        layout.addWidget(self.btn_convert, 0, 3, 2, 2)

        
        # Set the layout to the converter view
        self.setLayout(layout)

    def togge_widget_status(self, status: bool) -> None:
        """Toggles the status of the widgets in the converter view."""
        self.btn_input.setEnabled(status)
        self.spin_digits.setEnabled(status)
        self.cmb_output_type.setEnabled(status)
        self.btn_convert.setEnabled(status)
