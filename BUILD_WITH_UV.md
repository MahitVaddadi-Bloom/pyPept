# Building and Installing pyPept with UV

This guide explains how to build and install pyPept using the modern `uv` package manager.

## Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) installed

### Installing UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

## Quick Start

### Development Installation

```bash
# Clone the repository
cd pyPept

# Create virtual environment and install in editable mode
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install with development dependencies
uv pip install -e ".[dev]"
```

### User Installation

```bash
# Install from local directory
uv pip install .

# Or install in editable mode
uv pip install -e .
```

### Using UV Directly (No Virtual Environment Activation Required)

```bash
# Install dependencies
uv pip install -e .

# Run scripts with uv
uv run python examples/capped_peptide.py

# Run the CLI
uv run run_pyPept --help
```

## NumPy Compatibility

pyPept is compatible with both NumPy 1.x and 2.x:

- **NumPy 1.x**: Versions >= 1.22.2
- **NumPy 2.x**: All 2.x versions

The package automatically detects the NumPy version and uses appropriate APIs.

### Force Specific NumPy Version

```bash
# Install with NumPy 1.x
uv pip install -e . "numpy>=1.22.2,<2.0.0"

# Install with NumPy 2.x
uv pip install -e . "numpy>=2.0.0,<3.0.0"
```

## SciPy Compatibility

pyPept requires SciPy >= 1.9.0, which is compatible with both NumPy 1.x and 2.x.

## Building Distribution Packages

### Build Wheel and Source Distribution

```bash
# Install build tools
uv pip install build

# Build packages
python -m build

# Output will be in dist/
# - pyPept-1.0.0-py3-none-any.whl
# - pyPept-1.0.0.tar.gz
```

### Using Hatch (Recommended)

```bash
# Install hatch
uv pip install hatch

# Build with hatch
hatch build

# Clean build artifacts
hatch clean
```

## Development Workflow

### Install Development Dependencies

```bash
uv pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=pyPept --cov-report=html

# Run specific test file
uv run pytest tests/sequence_Test.py
```

### Code Formatting

```bash
# Format code with black
uv run black src tests

# Sort imports with isort
uv run isort src tests

# Check style with flake8
uv run flake8 src tests
```

### Type Checking

```bash
# Run mypy
uv run mypy src/pyPept
```

### Building Documentation

```bash
# Install docs dependencies
cd docs

# Build HTML documentation
uv run make html

# View documentation
open _build/html/index.html  # macOS
# or
xdg-open _build/html/index.html  # Linux
```

## Using the CLI

```bash
# After installation, use the CLI
run_pyPept --help

# Or with uv
uv run run_pyPept --help
```

## Troubleshooting

### RDKit Installation Issues

If RDKit installation fails:

```bash
# Use conda for RDKit
conda install -c conda-forge rdkit

# Then install pyPept without RDKit
uv pip install -e . --no-deps
uv pip install numpy pandas requests igraph biopython packaging scipy
```

### NumPy 2.0 Compatibility Issues

If you encounter issues with NumPy 2.0:

```bash
# Force NumPy 1.x
uv pip install "numpy>=1.22.2,<2.0.0" --force-reinstall

# Reinstall pyPept
uv pip install -e . --force-reinstall --no-deps
```

### Permission Issues

```bash
# Use user install
uv pip install --user -e .
```

## Version Management

### Bump Version

```bash
# Install bumpver
uv pip install bumpver

# Bump patch version (1.0.0 -> 1.0.1)
bumpver update --patch

# Bump minor version (1.0.0 -> 1.1.0)
bumpver update --minor

# Bump major version (1.0.0 -> 2.0.0)
bumpver update --major
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']
        numpy-version: ['1.x', '2.x']
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Install uv
      run: curl -LsSf https://astral.sh/uv/install.sh | sh
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        if [ "${{ matrix.numpy-version }}" == "1.x" ]; then
          uv pip install -e ".[dev]" "numpy>=1.22.2,<2.0.0"
        else
          uv pip install -e ".[dev]" "numpy>=2.0.0,<3.0.0"
        fi
    
    - name: Run tests
      run: uv run pytest
```

## Migration from setuptools

The package has been migrated from `setuptools` to `hatchling`:

### Key Changes

1. **Build backend**: Now uses `hatchling` instead of `setuptools`
2. **Dependencies**: Declared directly in `pyproject.toml`
3. **No setup.py**: All configuration in `pyproject.toml`
4. **Data files**: Automatically included via `tool.hatch.build`

### Old Way (setuptools)

```bash
pip install -e .
python setup.py install
```

### New Way (hatchling + uv)

```bash
uv pip install -e .
# or
hatch build
```

## Additional Resources

- [UV Documentation](https://github.com/astral-sh/uv)
- [Hatch Documentation](https://hatch.pypa.io/)
- [NumPy 2.0 Migration Guide](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
- [PEP 621](https://peps.python.org/pep-0621/) - Storing project metadata in pyproject.toml

## Support

For issues or questions:
- GitHub Issues: [pyPept Issues](https://github.com/yourusername/pyPept/issues)
- Documentation: [pyPept Docs](https://pypept.readthedocs.io)
