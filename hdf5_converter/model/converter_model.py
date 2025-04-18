#!/usr/bin/python3
# ----------------------------------------------------------------------------------
# Project: HDF5 Converter
# File: hdf5_converter/model/converter_model.py
# ----------------------------------------------------------------------------------
# Purpose:
# This is the converter model of the HDF5 Converter GUI. It is responsible for
# handling the conversion process.
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

from pathlib import Path

import fabio
import h5py
from qtpy.QtCore import Signal, QObject


class ConverterModel(QObject):
    """This class is responsible for handling the conversion process."""

    new_status = Signal()

    def __init__(self) -> None:
        """Initialises the converter model."""
        super(ConverterModel, self).__init__()

        self._status_message = ""

    def set_status_message(self, message: str) -> None:
        """Sets the status message."""
        self._status_message = message
        self.new_status.emit()

    def save_data(self, data: list, output_file: str, is_single_frame: bool = False, digits: int = 4, format: str = "tiff") -> None:
        """Saves the data in the specified format."""

        digits = int(digits)

        # The available formats
        format_mapping = {
            "tiff": fabio.tifimage.tifimage,
            "cbf": fabio.cbfimage.cbfimage
        }

        if format not in format_mapping:
            raise ValueError(f"Unsupported format: {format}")

        image_class = format_mapping[format]

        output_path = Path(output_file)

        if output_path.exists():
            self.set_status_message(f"Error: The file or directory '{output_file}' already exists. Conversion stopped to prevent data loss.")
            return

        if is_single_frame or data.ndim == 2:
            # Single image
            image = image_class(data if data.ndim == 2 else data[0])
            image.write(output_file)
        else:
            # Stack of images
            for i in range(data.shape[0]):
                image = image_class(data[i])
                # Append frame number to the file name with leading zeros
                frame_number = str(i + 1).zfill(digits) if digits > 1 else str(i + 1)
                output_file_with_frame = f"{output_file}_{frame_number}.{format}"
                output_frame_path = Path(output_file_with_frame)

                if output_frame_path.exists():
                    self.set_status_message(f"Error: The file '{output_file_with_frame}' already exists. Conversion stopped to prevent data loss.")
                    return

                image.write(output_file_with_frame)

    def process(self, file_name: str, search_term: str, output_type: str, digits: int) -> None:
        """Processes the HDF5 file and converts the datasets to the specified format."""
        
        image_count = 0
        frame_count = 0

        # Get the base name and parent directory of the file
        parent_dir = Path(file_name).parent
        base_name = Path(file_name).stem

        def visit_func(name: str, node: h5py.Dataset) -> None:
            nonlocal image_count, frame_count
            if isinstance(node, h5py.Dataset) and search_term in name:
                image_count += 1
                if len(node.shape) == 2:
                    frame_count += 1
                elif len(node.shape) > 2:
                    frame_count += node.shape[0]
                try:
                    # Read the dataset using h5py
                    with h5py.File(file_name, "r") as f:
                        dataset = f[name]
                        data = dataset[:]

                    if data.ndim == 2 or (data.ndim == 3 and data.shape[0] == 1):
                        # Single frame case
                        output_file = parent_dir / f"{base_name}.{output_type}"
                        if output_file.exists():
                            ConverterModel.set_status_message(f"Error: The file '{output_file}' already exists. Conversion stopped to prevent data loss.")
                            return
                        ConverterModel.save_data(data, str(output_file), is_single_frame=True, digits=digits, format=output_type)
                    else:
                        # Multiple frames case
                        output_dir = parent_dir / f"{base_name}_{output_type}"
                        if output_dir.exists():
                            ConverterModel.set_status_message(f"Error: The directory '{output_dir}' already exists. Conversion stopped to prevent data loss.")
                            return
                        output_dir.mkdir(parents=True, exist_ok=True)
                        output_file = output_dir / f"{base_name}"
                        ConverterModel.save_data(data, str(output_file), digits=digits, format=output_type)
                except Exception as e:
                    print(f"Error processing dataset {name}: {e}")
        
        if not Path(file_name).is_file():
            self.set_status_message(f"File {file_name} does not exist or cannot be accessed.")
            return
        
        with h5py.File(file_name, "r") as file:
            file.visititems(visit_func)

    @property
    def status_message(self) -> str:
        """Returns the status message."""
        return self._status_message
