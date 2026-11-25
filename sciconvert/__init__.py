# SPDX-License-Identifier: MIT

from argparse import ArgumentParser
from importlib.metadata import version
from pathlib import Path

from wxutils import AppConfig, WxApplication, add_application_arguments, handle_shortcut_arguments

from sciconvert.controller import MainController
from sciconvert.view import MainView
from sciconvert.model import MainModel

__version__ = version("sciconvert")
__all__ = ["__version__", "main"]

APP_CONFIG = AppConfig(
    name="SciConvert",
    assets=str(Path(__file__).resolve().parent / "assets"),
    description="Scientific data file format converter",
    application_id="gsecars.sciconvert",
)


def make_parser() -> ArgumentParser:
    """Builds the command line parser."""
    parser = ArgumentParser("sciconvert")
    add_application_arguments(parser)
    return parser


def main() -> None:
    parser = make_parser()
    args = parser.parse_args()

    if handle_shortcut_arguments(parser, args, APP_CONFIG):
        return

    app = WxApplication(APP_CONFIG, False)
    model = MainModel()
    view = MainView(version=__version__, with_inspect=args.inspect)
    _controller = MainController(model=model, view=view)

    app.run(view)

