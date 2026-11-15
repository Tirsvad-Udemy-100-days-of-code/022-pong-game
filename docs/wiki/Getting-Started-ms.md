[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

# Bermula

## Keperluan

Python 3.13 atau lebih baharu dan `pytest` untuk ujian. Permainan itu sendiri hanya menggunakan pustaka standard, dan tetingkap turtle memerlukan Tk (`tkinter`). Untuk menjalankan ujian, pasang alat pembangunan (`pytest`) dengan `python -m pip install -e ".[dev]"`.

## Persediaan

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Jalankan

```bash
python src/main.py
```

## Ujian

```bash
python -m pytest
```

## Lesen

Kod ini dilesenkan di bawah the GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). Lihat fail `LICENSE`.
