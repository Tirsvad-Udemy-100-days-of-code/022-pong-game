**English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

# Getting Started

## Requirements

Python 3.13 or newer and `pytest` for the tests. The game itself uses only the standard library, and the turtle window needs Tk (`tkinter`). To run the tests, install the development tool (`pytest`) with `python -m pip install -e ".[dev]"`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

```bash
python src/main.py
```

## Tests

```bash
python -m pytest
```

## Licence

The code is licensed under the GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). See the `LICENSE` file.
