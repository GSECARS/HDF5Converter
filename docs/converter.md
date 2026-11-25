# Converter

The converter reads one or more HDF5 files, walks their dataset tree, and writes matching datasets to image files on disk.

## Supported formats

| Format | Extension | Notes |
|--------|-----------|-------|
| TIFF | `.tif` | Default output format |
| CBF | `.cbf` | Crystallographic Binary Format |

## UI walkthrough

Launch the application with `sciconvert`. The window has two sections:

**Top bar - conversion controls**

| Widget | Description |
|--------|-------------|
| Load File(s) | Opens a multi-select file dialog filtered to `.h5`, `.hdf5`, `.mh5`, `.ph5` |
| Dataset Search Term | Substring matched against each HDF5 dataset path (default: `data`) |
| Number of Digits | Zero-padding width for frame numbers in multi-frame output (1–10, default: 3) |
| Output Type | Target format: `tif` or `cbf` |
| Convert | Starts the conversion; all controls disable until the run finishes |

**Bottom panel - status log**

Numbered messages stream in as files are processed. The log is cleared at the start of each new conversion run.

## Output layout

Output is written alongside each input file, using the input's stem as the base name.

**Single frame** (2-D dataset or a stack with exactly one frame):

```
input.h5  →  input.tif
```

**Multi-frame stack**:

```
input.h5  →  input_tif/
                 input_001.tif
                 input_002.tif
                 ...
```

The subdirectory name is `<stem>_<format>`. Frames are numbered from 1 with the configured digit width (e.g. `_001`, `_0001`).

SciConvert will **not** overwrite existing files or directories. If a conflict is detected, conversion stops immediately and an error is written to the status log.

## Library usage

The converter can be driven programmatically without the GUI:

```python
from sciconvert.model import ConverterModel

converter = ConverterModel()

# Optional: receive status updates
converter.status_callback = lambda: print(converter.status_message)

# Convert a single file
converter.process(
    file_name="/data/sample.h5",
    search_term="data",
    output_type="tif",
    digits=4,
)
```

### Writing image data directly

```python
import h5py
from sciconvert.model import ConverterModel

converter = ConverterModel()

with h5py.File("/data/sample.h5", "r") as f:
    data = f["entry/data"][:]

# Single frame
converter.save_data(data[0], "/data/frame.tif", is_single_frame=True, format="tif")

# Stack - creates /data/stack_001.tif, /data/stack_002.tif, ...
converter.save_data(data, "/data/stack", digits=3, format="tif")
```

### `ConverterModel.process` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `file_name` | `str` | Path to the HDF5 file |
| `search_term` | `str` | Substring matched against dataset paths |
| `output_type` | `str` | Output format: `"tif"` or `"cbf"` |
| `digits` | `int` | Zero-padding width for frame numbers |

### `ConverterModel.save_data` parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `data` | `ndarray` | | Image data (2-D or 3-D array) |
| `output_file` | `str` | | Output path (no extension for stacks) |
| `is_single_frame` | `bool` | `False` | Force single-frame output even for 3-D arrays |
| `digits` | `int` | `4` | Zero-padding width |
| `format` | `str` | `"tif"` | Output format: `"tif"` or `"cbf"` |

