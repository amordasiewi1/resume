from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from resume import Resume


class HTMLExporter:
    def __init__(self, template_dir: str | Path = "templates"):
        self.environment = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(
                enabled_extensions=("html","htm","xml"),
                default=True,
            ),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render(
        self,
        resume: Resume,
        template_name: str = "resume.html.j2",
    ) -> str:
        template = self.environment.get_template(template_name)
        return template.render(resume=resume)

    def save(
        self,
        resume: Resume,
        path: str | Path,
        template_name: str = "resume.html.j2",
    ) -> None:
        Path(path).write_text(
            self.render(resume, template_name),
            encoding="utf-8",
        )