# SPDX-License-Identifier: MIT

from sciconvert.model.converter_model import ConverterModel


class MainModel:
    """This class is responsible for setting up the main model of the HDF5 Converter GUI."""

    def __init__(self) -> None:
        """Initialises the main model."""
        self.converter = ConverterModel()

