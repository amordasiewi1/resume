from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from resume import Resume

"""
Custom escape characters for latex exporter so it doesnt get confused
"""
def latex_escape(text: str | None) -> str:
    if text is None:
        return ""

    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }

    result = ""

    for char in text:
        result += replacements.get(char, char)

    return result

"""
Latex exporter class, needs jinja template
"""
class LatexExporter:
    def __init__(self, template_dir: str | Path = "templates"):
        self.template_dir = Path(template_dir)

        self.environment = Environment(
            loader=FileSystemLoader(self.template_dir),

            block_start_string="((*",
            block_end_string="*))",

            variable_start_string="(((",
            variable_end_string=")))",

            comment_start_string="((#",
            comment_end_string="#))",

            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )

        self.environment.filters["latex"] = latex_escape

    def render(
            self,
        resume: Resume,
        template_name: str = "resume.tex.j2",
    ) -> str:
        template = self.environment.get_template(template_name)

        return template.render(resume=resume)

    def save(
        self,
        resume: Resume,
        path: str | Path,
        template_name: str = "resume.tex.j2",
    ) -> None:
        path = Path(path)

        latex = self.render(
            resume=resume,
            template_name=template_name,
        )

        path.write_text(
            latex,
            encoding="utf-8",
        )