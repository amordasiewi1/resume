# Resume generator

A Python 3.12+ project managed with uv. Resume data is validated with Pydantic,
exported to JSON and YAML, rendered to LaTeX with Jinja2, and compiled to PDF.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
PDF generation also requires `latexmk` and a LaTeX distribution on your PATH.
For Ubuntu/WSL:

```bash
sudo apt install latexmk texlive-latex-extra texlive-fonts-recommended
```

Clone the repository and install the locked dependencies:

```bash
git clone https://github.com/amordasiewi1/resume.git
cd resume
uv sync --locked
```

## Generate a resume

Edit `resume_data.py`, then run from the repository root:

```bash
uv run main.py
```

Outputs are written to `data/resume.json`, `data/resume.yaml`,
`data/resume.tex`, and `data/resume.pdf`. Generated outputs are ignored by Git.

## Project files

- `resume.py`: resume models and serialization.
- `resume_data.py`: personal resume content.
- `exporters/latex.py`: LaTeX rendering.
- `exporters/pdf.py`: compilation using `latexmk`.
- `templates/resume.tex.j2`: resume layout.
- `pyproject.toml`: project metadata and dependency constraints.
- `uv.lock`: exact resolved dependencies; commit this file.
- `.python-version`: Python version used by uv.

## Dependencies

```bash
uv add package-name
uv remove package-name
uv lock --upgrade-package package-name
uv sync --locked
```

Commit changes to both `pyproject.toml` and `uv.lock` when dependencies change.
The virtual environment is created locally and excluded from Git.
