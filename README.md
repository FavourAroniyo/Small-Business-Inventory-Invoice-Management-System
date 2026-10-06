# Small Business Inventory and Invoice Management System

Python/Tkinter desktop application implementing the supplied proposal.

## Included
Products, stock movements, TXT/PDF/DOCX supplier import, regex parsing, optional Gemini extraction,
review-before-save, customers, invoices, payments, automatic stock deduction, invoice DOCX files,
low-stock dashboard, reports, CSV export, backups, duplicate-file fingerprints, validation,
custom exceptions, logging-ready modular services, and tests.

## Run
Python 3.11+:
1. `python -m venv .venv`
2. activate it
3. `pip install -r requirements.txt`
4. optionally copy `.env.example` to `.env` and set `GEMINI_API_KEY`
5. `python demo_seed.py`
6. `python main.py`

The application works without Gemini. AI is an enhancement, never the source of invoice totals or stock counts.

## Architecture
GUI -> Services -> Repositories/Readers/Exporters/AI -> SQLite/files/API.

Suggested Git branches from the proposal:
`feature/inventory` then `feature/invoicing`.
