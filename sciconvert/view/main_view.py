# SPDX-License-Identifier: MIT

import wx
from wxutils import FlatConfirmDialog, FlatPanel

from sciconvert.view.converter_view import ConverterView
from sciconvert.view.status_view import StatusView


class MainView(wx.Frame):
    """Implements the main application view."""

    def __init__(self, version: str, with_inspect: bool = False) -> None:
        super(MainView, self).__init__(parent=None, id=wx.ID_ANY, title=f"SciConvert {version}")


        # Helper variables
        self._with_inspect = with_inspect
        self._terminated = False
        self._worker_finished = False

        # Panels
        self.main_panel = FlatPanel(self)
        self.converter_view = ConverterView(self.main_panel)
        self.status_view = StatusView(self.main_panel)

        # Run the configuration methods
        self._layout()
        self.Bind(wx.EVT_CLOSE, self._close_event_handler)

    def _create_menu(self) -> None:
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()

        # Quit
        quit_id = wx.NewIdRef()
        file_menu.Append(quit_id, "Quit]tCtrl+Q")
        self.Bind(wx.EVT_MENU, lambda event: self.Close(), id=quit_id)

        # wx inspection tool
        if self._with_inspect:
            inspect_item = file_menu.Append(wx.ID_ANY, "Show wxPython Inspection Tool\tCtrl+I", "Debug wxPythonApp")
            self.Bind(wx.EVT_MENU, self._show_inspection_tool, ispect_item)

        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)    

    @staticmethod
    def _show_inspection_tool(event=None) -> None:
        """Shows the wx inspection tool."""
        wx.GetApp().ShowInspectionTool().Show()

    def _layout(self) -> None:
        """Sets the layout of the main view."""
        # Set the layout of the main panel
        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        panel_sizer.Add(self.converter_view, 0, wx.EXPAND)
        panel_sizer.Add(self.status_view, 1, wx.EXPAND)
        self.main_panel.SetSizer(panel_sizer)

        frame_sizer = wx.BoxSizer(wx.VERTICAL)
        frame_sizer.Add(self.main_panel, 1, wx.EXPAND)
        self.SetSizer(frame_sizer)

    def display_window(self) -> None:
        """Sets the title and displays the main window."""
        # Set the window title
        self.SetTitle("HDF5 Converter")

        # Display the main window
        self.Show()

    def _close_event_handler(self, event: wx.CloseEvent) -> None:
        """Runs when trying to close the application."""
        result = FlatConfirmDialog(self, "Are you sure you want to close the appliation?", "Close Application").ShowModal()
        if result == wx.ID_YES:
            self._terminated = True
            while not self._worker_finished:
                wx.SafeYield()
            event.Skip()
        else:
            event.Veto()

    @property
    def terminated(self) -> bool:
        return self._terminated

    @property
    def worker_finished(self) -> bool:
        return self._worker_finished

    @worker_finished.setter
    def worker_finished(self, value: bool) -> None:
        self._worker_finished = value
