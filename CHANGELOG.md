# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.2] - 2026-11-25

### Added

- New `sciconvert` package
- `sciconvert` CLI entry point (`sciconvert = "sciconvert:main"`) for launching the application from the command line
- Application icons for all platforms: `.icns` (macOS), `.ico` (Windows), `.png` (Linux/generic)
- `WorkerModel` backed by `threading.Thread` to run the conversion loop in the background without blocking the UI
- Concurrent multi-file conversion
- Callback-based status reporting in `ConverterModel` (`status_callback`) so the model can push messages to the UI
- Three GitHub Actions CI/CD workflows:
  - `tests.yml` — runs `pytest` on Ubuntu, macOS, and Windows against Python 3.14 on every push/PR to `main`
  - `publish.yml` — builds and publishes to PyPI via trusted publishing on version tags, then auto-creates a GitHub Release populated with the matching CHANGELOG section
  - `docs.yml` — builds Sphinx documentation and deploys it to GitHub Pages on every push to `main`
- `CONTRIBUTING.md` with contribution guidelines and links to GitHub/GitLab issue trackers
- `docs` dependency group
- `dev` dependency group
- `uv.lock` lockfile for fully reproducible dependency resolution
- `.python-version` file pinning the project to Python 3.14
- Dynamic versioning from VCS tags via `hatch-vcs`
- Sphinx documentation under `docs/` with `conf.py`, `index.md`, `converter.md`, and a footer template
- `index.md` landing page with installation instructions, CLI flags, and module grid cards
- `converter.md` covering supported formats, UI walkthrough, output layout, library usage examples, parameter tables

### Changed

- **Project renamed** from `HDF5Converter` to `SciConvert` and main package name changed from `hdf5_converter` to `sciconvert`
- **License changed** from GPL-3.0 to MIT and `LICENSE` replaced by `LICENSE.txt`
- Changed python version from `>=3.13` to `==3.14.*`
- Switched build system from `setuptools` / `setuptools_scm` to `hatchling` / `hatch-vcs`
- Migrated to `uv` with optional dependencies replaced by `[dependency-groups]`
- Migrated from PyQt to wxPython with `wxutils`

### Removed

- Entire `hdf5_converter` package (old Qt-based `main_controller`, `main_model`, `qt_worker_model`, `main_view`, `status_view`)
- `HDF5Converter.py` top-level application entry point
- `HDF5Converter.spec` PyInstaller build specification
- `create_apps.sh` and `create_exe.bat` platform-specific build scripts
- `pyinstaller` as a development dependency
- `black` and `flake8` linting tools and their `pyproject.toml` configuration sections
