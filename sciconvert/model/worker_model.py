# SPDX-License-Identifier: MIT

import threading
from typing import Callable, Any


class WorkerModel(threading.Thread):
    """This class is responsible for creating a worker thread that handles the conversion processes."""

    def __init__(self, method: Callable, args: Any) -> None:
        """Initialises the worker model."""
        super(WorkerModel, self).__init__(daemon=True)
        self._method = method
        self._args = args

    def run(self) -> None:
        """Runs the worker thread."""
        self._method(*self._args)

