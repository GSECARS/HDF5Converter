# HDF5Converter

![Licence](https://img.shields.io/badge/License-GPL--3.0-teal.svg) ![Python](https://img.shields.io/badge/Python-3.13-22558a.svg?logo=python&color=22558a)

This application is designed to convert HDF5 files into various formats. It currently supports conversion to .tiff and .cbf, with additional formats planned for future updates.

------------
## Table of Contents

- [Installation](#installation)
- [Contribution](#contributing)
- [License](#license)

------------
## Installation
To install the .atest build of the application you can find the installers [here](https://github.com/GSECARS/HDF5Converter/releases/).

If you prefer to build it from source run the following:
```bash
git clone https://github.com/GSECARS/HDF5Converter.git && cd HDF5Converter && python HDF5Converter.py
```

### Development
To set up the project for development, just clone the repository and install in development mode. Pre-commit hooks need to be installed as well.

```bash
git clone -b development https://github.com/GSECARS/HDF5Converter.git && cd HDF5Converter && pip install -e ".[development]" && pre-commit install
```

------------
## Contributing

All contributions to the HDF5Converter project are welcome! Here are some ways you can help:
- Report a bug by opening an [issue](https://github.com/GSECARS/HDF5Converter/issues).
- Add new features, fix bugs or improve documentation by submitting a [pull request](https://github.com/GSECARS/HDF5Converter/pulls).

Please adhere to the [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow) model when making your contributions! This means creating a new branch for each feature of bug fix, and submitting your changes as a pull request against the main branch. If you're not sure how to contribute, please open an issue and we'll be happy to help you out.

By contributing to the HDF5Converter project, you agree that your contributions will be licensed under the  GNU General Public License version 3.

------------
## License

HDF5Converter is distributed under the GNU General Public License version 3. You should have received a [copy](LICENSE) of the GNU General Public License along with this program.  If not, see 
https://www.gnu.org/licenses/ for additional details.