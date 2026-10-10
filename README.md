
## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
PDF generation also requires `latexmk` and a LaTeX distribution on your PATH.
For Ubuntu/WSL:

```bash
sudo apt install latexmk texlive-latex-extra texlive-fonts-recommended
```

Clone the repo and install the locked dependencies:

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
`data/resume.tex`, and `data/resume.pdf`.
