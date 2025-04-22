# ----------------------------------------------------------------------------------
# Project: HDF5Converter
# File: HDF5Converter.spec
# ----------------------------------------------------------------------------------
# Purpose:
# This file is used to create a standalone executable for the HDF5 Converter GUI
# using PyInstaller. It includes the necessary imports, analysis, and configuration
# for the executable. The executable is created based on the platform (Windows, Mac,
# or Linux) and includes the required dependencies and resources.
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

import os
from sys import platform
from PyInstaller.utils.hooks import collect_submodules

version = "0.0.1"

a = Analysis(
    ['HDF5Converter.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=[],
    hiddenimports=collect_submodules("fabio"),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Set the application name and OS based on the platform
if platform == "win32" or platform == "cygwin":
    os = "Win"
    app_name = "HDF5Converter.exe"
elif platform == "darwin":
    os = "Mac"
    app_name = "HDF5Converter"
elif platform == "linux" or platform == "linux2":
    os = "Linux"
    app_name = "HDF5Converter"

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=f"{app_name}_{os}_{version}",
)

# Create the MacOS app bundle
if os == "Mac":
    app = BUNDLE(
        coll,
        name="HDF5Converter.app",
    )
