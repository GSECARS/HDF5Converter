# SPDX-License-Identifier: MIT

import wx
from wxutils import FlatButton, FlatLabel, FlatCombo, FlatTextCtrl, FlatPanel
from wxutils.dialogs import FileOpen
from wxutils.themes import get_theme


class _LoadFilesButton(FlatButton):
    """Flat button that opens a multi-file dialog and stores the selected paths."""

    def __init__(self, parent: wx.Window, label: str, file_extensions: list) -> None:
        super().__init__(parent, label)
        self._file_extensions = file_extensions
        self.file_path: list = []
        self.Bind(wx.EVT_BUTTON, self._open_files)

    def _open_files(self, event: wx.CommandEvent) -> None:
        """Opens a file dialog and stores the selected paths."""
        parts = [f"*.{ext}" for ext in self._file_extensions]
        wildcard = f"HDF5 files ({';'.join(parts)})|{';'.join(parts)}"
        paths = FileOpen(self.GetTopLevelParent(), "Select HDF5 File(s)", multiple=True, wildcard=wildcard)
        if paths:
            self.file_path = paths if isinstance(paths, list) else [paths]
            self.SetLabel(f"Loaded {len(self.file_path)} File(s)")


class ConverterView(FlatPanel):
    """Creates the converter view of the HDF5 Converter GUI."""

    def __init__(self, parent: wx.Window) -> None:
        """Initialises the converter view."""
        super(ConverterView, self).__init__(parent)

        theme = get_theme()
        self.SetBackgroundColour(theme.background)

        # Create the widgets
        self.btn_input = _LoadFilesButton(self, "Load File(s)", ["h5", "hdf5", "mh5", "ph5"])
        self.lbl_digits = FlatLabel(self, label="Number of Digits")
        self.spin_digits = wx.SpinCtrl(self, value="3", min=1, max=10)
        self.btn_convert = FlatButton(self, "Convert")
        self.lbl_output_type = FlatLabel(self, label="Output Type")
        self.cmb_output_type = FlatCombo(self, choices=["tif", "cbf"])
        self.lbl_search_term = FlatLabel(self, label="Dataset Search Term")
        self.input_search_term = FlatTextCtrl(self, value="data", placeholder="Enter search term", size=wx.Size(200, 32))

        # Set the default output type
        self.cmb_output_type.SetSelection(0)

        # Set the layout of the converter view
        self._layout()

    def _layout(self) -> None:
        """Sets the layout of the converter view."""
        digits_sizer = wx.BoxSizer(wx.HORIZONTAL)
        digits_sizer.Add(self.lbl_digits, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)
        digits_sizer.Add(self.spin_digits, 0, wx.ALIGN_CENTER_VERTICAL)

        output_type_sizer = wx.BoxSizer(wx.HORIZONTAL)
        output_type_sizer.Add(self.lbl_output_type, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)
        output_type_sizer.Add(self.cmb_output_type, 0, wx.ALIGN_CENTER_VERTICAL)

        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        search_sizer.Add(self.lbl_search_term, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)
        search_sizer.Add(self.input_search_term, 1, wx.EXPAND)

        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        row_sizer.Add(search_sizer, 1, wx.EXPAND)
        row_sizer.Add(digits_sizer, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 4)
        row_sizer.Add(output_type_sizer, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 4)

        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.Add(self.btn_input, 0, wx.EXPAND)
        left_sizer.Add(row_sizer, 0, wx.EXPAND | wx.TOP, 2)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(left_sizer, 1, wx.EXPAND)
        sizer.Add(self.btn_convert, 0, wx.EXPAND | wx.LEFT, 2)

        self.SetSizer(sizer)

    def togge_widget_status(self, status: bool) -> None:
        """Toggles the status of the widgets in the converter view."""
        self.btn_input.Enable(status)
        self.spin_digits.Enable(status)
        self.cmb_output_type.Enable(status)
        self.btn_convert.Enable(status)
        self.input_search_term.Enable(status)

