# SPDX-License-Identifier: MIT

import time
from contextlib import suppress
from pathlib import Path

from sciconvert.view import MainView
from sciconvert.model import MainModel, WorkerModel
from sciconvert.controller.converter_controller import ConverterController


class MainController:
    """This class is responsible for controlling the main application."""

    def __init__(self, model: MainModel, view: MainView) -> None:
        self._model = model
        self._view = view

        # Initialize the converter controller
        self._converter_controller = ConverterController(model=self._model, view=self._view)

        # Initialize the worker model
        self._worker_model = WorkerModel(self._worker_methods, ())
        self._worker_model.start()

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

