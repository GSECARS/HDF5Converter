:: ----------------------------------------------------------------------------------
:: Project: HDF5 Converter
:: File: create_exe.bat
:: ----------------------------------------------------------------------------------
:: Purpose:
:: This file is used to create an executable for the HDF5 Converter program.
:: ----------------------------------------------------------------------------------
:: Author: Christofanis Skordas
::
:: Copyright (c) 2025 GSECARS, The University of Chicago
:: Copyright (c) 2025 NSF SEES, Synchrotron Earth and Environmental Science
::
:: This program is free software: you can redistribute it and/or modify
:: it under the terms of the GNU General Public License as published by
:: the Free Software Foundation, either version 3 of the License, or
:: (at your option) any later version.
::
:: This program is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
:: GNU General Public License for more details.
::
:: You should have received a copy of the GNU General Public License
:: along with this program.  If not, see <https://www.gnu.org/licenses/>.
:: ----------------------------------------------------------------------------------

:: Delete previous build directories
rmdir /s /q dist
rmdir /s /q build

:: Create the executable using PyInstaller
PyInstaller HDF5Converter.spec