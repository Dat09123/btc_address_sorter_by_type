# Bitcoin Address Sorter by Type 🪙

![Version](https://img.shields.io/badge/version-1.0.0-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![Release](https://img.shields.io/badge/release-latest-orange)

Welcome to the **Bitcoin Address Sorter by Type** repository! This tool provides an ultra-fast solution for sorting Bitcoin addresses based on their types. With real-time multiprocessing, it detects address formats while keeping RAM usage low. This makes it ideal for forensic research, data analytics, and blockchain intelligence.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Address Types](#address-types)
- [Contributing](#contributing)
- [License](#license)
- [Release Information](#release-information)
- [Acknowledgments](#acknowledgments)

## Features

- **Ultra-Fast Sorting**: Sort Bitcoin addresses quickly using efficient algorithms.
- **Real-Time Multiprocessing**: Leverage multiple CPU cores for faster processing.
- **Address Format Detection**: Automatically identify address formats, including P2PKH, P2SH, and Bech32.
- **Low RAM Usage**: Designed to run efficiently on systems with limited memory.
- **User-Friendly Interface**: Simple command-line interface for ease of use.
- **Supports Multiple Address Types**: Handles various Bitcoin address formats seamlessly.

## Installation

To get started, you need to clone this repository and install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Dat09123/btc_address_sorter_by_type.git
   cd btc_address_sorter_by_type
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.8 or higher installed. You can install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installation, you can run the Bitcoin Address Sorter. The basic command structure is as follows:

```bash
python sorter.py [options] [address_file]
```

### Options

- `-h`, `--help`: Show help message and exit.
- `-o`, `--output`: Specify the output file for sorted addresses.
- `-t`, `--type`: Filter addresses by type (P2PKH, P2SH, Bech32).

### Example

To sort a file containing Bitcoin addresses, use:

```bash
python sorter.py -o sorted_addresses.txt addresses.txt
```

## Address Types

The Bitcoin Address Sorter supports the following address types:

- **P2PKH (Pay-to-Public-Key-Hash)**: Traditional addresses starting with '1'.
- **P2SH (Pay-to-Script-Hash)**: Addresses starting with '3'.
- **Bech32 (Segregated Witness)**: Native SegWit addresses starting with 'bc1'.

## Contributing

We welcome contributions to enhance the functionality and performance of the Bitcoin Address Sorter. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Release Information

You can download the latest release of the Bitcoin Address Sorter from the [Releases](https://github.com/Dat09123/btc_address_sorter_by_type/releases) section. Make sure to execute the downloaded file as per the instructions provided in the documentation.

For detailed release notes and updates, visit the [Releases](https://github.com/Dat09123/btc_address_sorter_by_type/releases) section.

## Acknowledgments

- **Bitcoin Developers**: For creating the Bitcoin protocol and inspiring projects like this.
- **Open Source Community**: For providing valuable resources and libraries.
- **Contributors**: Thank you for your efforts in improving this project.

## Contact

For any questions or suggestions, feel free to open an issue in this repository or contact the maintainer directly.

---

This README provides a comprehensive overview of the Bitcoin Address Sorter by Type, its features, installation steps, usage instructions, and contribution guidelines. The project aims to support researchers and developers working in the blockchain and cryptocurrency space.