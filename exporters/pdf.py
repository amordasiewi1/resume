from pathlib import Path
import shutil
import subprocess

"""
Latex PDF Compiler class
"""
class PDFCompiler:
    def __init__(self):
        if shutil.which("latexmk") is None:
            raise RuntimeError(
                "latexmk is not installed or not available on PATH."
            )

    def compile(self, tex_path: str | Path) -> Path:
        tex_path = Path(tex_path).resolve()

        if not tex_path.exists():
            raise FileNotFoundError(
                f"Could not find TeX file: {tex_path}"
            )

        subprocess.run(
            [
                "latexmk",
                "-pdf",
                "-interaction=nonstopmode",
                "-halt-on-error",
                tex_path.name,
            ],
            cwd=tex_path.parent,
            check=True,
        )

        return tex_path.with_suffix(".pdf")