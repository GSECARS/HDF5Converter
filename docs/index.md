# SciConvert

A scientific data file format converter.

## Installation

```bash
pip install sciconvert
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv tool install sciconvert
```

## Running the application

```bash
sciconvert
```

Pass `--inspect` to open the wxPython inspection tool for debugging the UI:

```bash
sciconvert --inspect
```

## Modules

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Converter
:link: converter
:link-type: doc

Handles loading HDF5 files, traversing datasets by search term, and writing frames to TIF or CBF format. Includes safe overwrite protection and parallel file processing.
:::

:::{grid-item-card} API Reference
:link: autoapi/index
:link-type: doc

Auto-generated reference for all public classes and functions.
:::

::::

```{toctree}
:maxdepth: 2
:hidden:

converter
API Reference <autoapi/index>
```
