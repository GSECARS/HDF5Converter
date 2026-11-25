# SPDX-License-Identifier: MIT

import time
from concurrent.futures import ThreadPoolExecutor

import wx

from sciconvert.view import MainView
from sciconvert.model import MainModel


class ConverterController:
    """This class is responsible for handling the conversion process."""

    def __init__(self, model: MainModel, view: MainView) -> None:
        """Initialize the converter controller with the view and model."""
        self._model = model
        self._view = view
        self._converting = False
        self._processing = False

        # Connect signals to slots
        self._connect_signals()

    def _connect_signals(self) -> None:
        """Connect view events and model callbacks."""
        # Connect the convert button event to the trigger method
        self._view.converter_view.btn_convert.Bind(wx.EVT_BUTTON, self._trigger_conversion)
        self._model.converter.status_callback = self._update_status_message

    def convert_files(self) -> None:
        """Handle the conversion process."""
        format = self._view.converter_view.cmb_output_type.GetStringSelection()
        search_term = self._view.converter_view.input_search_term.GetValue()
        digits = self._view.converter_view.spin_digits.GetValue()
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
                    wx.CallAfter(self._view.status_view.add_status_message, f"Error processing file: {e}")

        # Print the total time taken to convert the files in minutes or seconds based on the time taken
        end_time = time.time()
        total_time = end_time - start_time
        if total_time < 60:
            wx.CallAfter(self._view.status_view.add_status_message, f"Conversion completed in {total_time:.2f} seconds.")
        else:
            wx.CallAfter(self._view.status_view.add_status_message, f"Conversion completed in {int(total_time // 60)} minutes and {total_time % 60:.2f} seconds.")

    def _prepare_for_convertion(self) -> None:
        """Prepare the view for conversion by disabling the widgets and updating the status message."""
        # Disable the conversion widgets
        self._view.converter_view.togge_widget_status(False)

        # Clear the status view
        self._view.status_view.clear()

        # Provide the initial message for the conversion starting and on what files
        self._view.status_view.add_status_message("Files to be converted:")
        self._view.status_view.add_status_message("--------------------------------------------------")
        # Get the input files from the view
        for file in self._view.converter_view.btn_input.file_path:
            self._view.status_view.add_status_message(file)
        self._view.status_view.add_status_message("--------------------------------------------------")
        # Provide the message for the conversion starting
        self._view.status_view.add_status_message("Conversion in progress...")

    def restore_after_convertion(self) -> None:
        """Restore the view after conversion is complete."""
        # Restore the helpers
        self._converting = False
        self._processing = False
        # Restore the conversion widgets
        wx.CallAfter(self._view.converter_view.togge_widget_status, True)

    def _update_status_message(self) -> None:
        """Update the status message in the view."""
        wx.CallAfter(self._view.status_view.add_status_message, self._model.converter.status_message)

    def _trigger_conversion(self, event: wx.CommandEvent) -> None:
        """Trigger the conversion process."""
        self._converting = True

    @property
    def converting(self) -> bool:
        return self._converting

    @property
    def processing(self) -> bool:
        return self._processing

