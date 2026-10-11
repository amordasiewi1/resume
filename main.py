from pathlib import Path

from resume_data import resume
from exporters.latex import LatexExporter
from exporters.pdf import PDFCompiler
from exporters.html import HTMLExporter


def main():
    Path("data").mkdir(parents=True, exist_ok=True)
    resume.save_json("data/resume.json")
    resume.save_yaml("data/resume.yaml")
    HTMLExporter().save(resume, "data/resume.html")
    LatexExporter().save(resume, "data/resume.tex")
    PDFCompiler().compile("data/resume.tex")

if __name__ == "__main__":
    main()
