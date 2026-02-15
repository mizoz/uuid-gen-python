# UUID Generator Python

[![PyPI Version](https://img.shields.io/pypi/v/uuid-gen-python?style=flat-square)](https://pypi.org/project/uuid-gen-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/uuid-gen-python?style=flat-square)](https://pypi.org/project/uuid-gen-python/)
[![License](https://img.shields.io/pypi/l/uuid-gen-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/uuid-gen-python?style=flat-square)](https://pypi.org/project/uuid-gen-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/uuid-gen-python?style=flat-square)](https://github.com/mizoz/uuid-gen-python)

> A Python CLI tool for generating UUIDs (Universally Unique Identifiers).

## Features

- Generate UUID v4 (random)
- Generate UUID v1 (timestamp-based)
- Bulk UUID generation
- Multiple output formats
- Python API for integration

## Installation

### From PyPI

```bash
pip install uuid-gen-python
```

### From Source

```bash
git clone https://github.com/mizoz/uuid-gen-python.git
cd uuid-gen-python
pip install -e .
```

## Usage

### Command Line

```bash
# Generate a single UUID v4
uuid-gen

# Generate UUID v1
uuid-gen --v1

# Generate multiple UUIDs
uuid-gen --count 10

# Generate in specific format
uuid-gen --format upper
```

### Python API

```python
from uuid_gen import UUIDGenerator

gen = UUIDGenerator()

# Generate UUID v4
uuid = gen.generate_v4()
print(uuid)

# Generate UUID v1
uuid = gen.generate_v1()
print(uuid)
```

## CLI Options

| Option | Description |
|--------|-------------|
| `--v1` | Generate UUID v1 (timestamp-based) |
| `--count N` | Generate N UUIDs |
| `--format` | Output format (default, upper, no-dashes) |

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
