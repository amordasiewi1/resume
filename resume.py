from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Annotated, Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator


# Base data model from which all classes inherit
class ResumeModel(BaseModel):
    """Base class for all resume data models."""

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )


# Contact link
class ContactLink(ResumeModel):
    """Embedded links for contacts."""

    label: str
    url: str
    display: str | None = None


# Contact information
class Contacts(ResumeModel):
    """Contact information."""

    phone: str | None = None
    email: str | None = None
    links: list[ContactLink] = Field(default_factory=list)


# Date range
class DateRange(ResumeModel):
    """Start/end dates for resume entries."""

    start: dt.datetime | None = None
    end: dt.datetime | None = None
    present: bool = False

    @model_validator(mode="after")
    def validate_dates(self) -> DateRange:
        if self.present and self.end is not None:
            raise ValueError(
                "DateRange cannot have both an end date and present=True."
            )

        if (
            self.start is not None
            and self.end is not None
            and self.end < self.start
        ):
            raise ValueError(
                "End date cannot be before start date."
            )

        return self

    @staticmethod
    def format_date(date: dt.datetime) -> str:
        return date.strftime("%B %Y")

    def display(self) -> str:
        if self.start is None:
            return ""

        start = self.format_date(self.start)

        if self.present:
            return f"{start} - Present"

        if self.end is None:
            return start

        return f"{start} - {self.format_date(self.end)}"


# Convenience helper
def month(year: int, month: int) -> dt.datetime:
    return dt.datetime(year, month, 1)


# Experience
class ExperienceEntry(ResumeModel):
    """Professional, research, teaching, or extracurricular experience."""

    kind: Literal["experience"] = "experience"

    title: str
    organization: str
    location: str | None = None
    dates: DateRange | None = None

    bullets: list[str] = Field(default_factory=list)


# Education

class Degree(ResumeModel):
    """One degree earned or pursued at an institution."""

    degree: str
    dates: DateRange | None = None
    gpa: str | None = None

    concentrations: list[str] = Field(default_factory=list)
    minors: list[str] = Field(default_factory=list)

class EducationEntry(ResumeModel):
    """Education at a single institution."""

    kind: Literal["education"] = "education"

    institution: str
    location: str | None = None

    degrees: list[Degree] = Field(default_factory=list)

    coursework: list[str] = Field(default_factory=list)
    interests: list[str] = Field(default_factory=list)

    bullets: list[str] = Field(default_factory=list)


# Publications
class Author(ResumeModel):
    """Publication author."""

    name: str
    highlight: bool = False


class PublicationEntry(ResumeModel):
    """Publication entry."""

    kind: Literal["publication"] = "publication"

    title: str
    authors: list[Author] = Field(default_factory=list)

    venue: str | None = None
    year: int | None = None
    location: str | None = None

    url: str | None = None
    identifier: str | None = None


# Skills
class SkillGroup(ResumeModel):
    """Group of related skills."""

    name: str
    skills: list[str] = Field(default_factory=list)


class SkillsEntry(ResumeModel):
    """Technical skills entry."""

    kind: Literal["skills"] = "skills"

    groups: list[SkillGroup] = Field(default_factory=list)


# Generic custom entry
class CustomEntry(ResumeModel):
    """Generic entry for user-defined sections."""

    kind: Literal["custom"] = "custom"

    title: str | None = None
    subtitle: str | None = None

    location: str | None = None
    dates: DateRange | None = None

    bullets: list[str] = Field(default_factory=list)
    text: str | None = None

    metadata: dict[str, Any] = Field(default_factory=dict)


# Resume entry type alias
ResumeEntry = Annotated[
    EducationEntry
    | ExperienceEntry
    | PublicationEntry
    | SkillsEntry
    | CustomEntry,
    Field(discriminator="kind"),
]


# Section
class Section(ResumeModel):
    """A resume section."""

    title: str
    entries: list[ResumeEntry] = Field(default_factory=list)

    def add(self, entry: ResumeEntry) -> None:
        self.entries.append(entry)


# yaml dumper for list formatting
class IndentedDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


# Full resume
class Resume(ResumeModel):
    """Complete resume."""

    name: str
    contacts: Contacts = Field(default_factory=Contacts)

    citizenship: str | None = None

    sections: list[Section] = Field(default_factory=list)

    #
    # Section helpers
    #

    def add_section(self, section: Section) -> None:
        self.sections.append(section)

    def get_section(self, title: str) -> Section | None:
        for section in self.sections:
            if section.title.casefold() == title.casefold():
                return section

        return None

    def add_entry(
        self,
        section_title: str,
        entry: ResumeEntry,
    ) -> None:
        section = self.get_section(section_title)

        if section is None:
            section = Section(title=section_title)
            self.sections.append(section)

        section.entries.append(entry)

    def remove_section(self, title: str) -> None:
        sections = []

        for section in self.sections:
            if section.title.casefold() == title.casefold():
                continue

            sections.append(section)

        self.sections = sections

    #
    # Serialization helpers
    #

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump(
            mode="json",
            exclude_none=True,
        )

    def save_json(self, path: str | Path) -> None:
        path = Path(path)

        path.write_text(
            self.model_dump_json(
                indent=4,
                exclude_none=True,
            ),
            encoding="utf-8",
        )

    @classmethod
    def load_json(cls, path: str | Path) -> Resume:
        path = Path(path)

        return cls.model_validate_json(
            path.read_text(encoding="utf-8")
        )

    def save_yaml(self, path: str | Path) -> None:
        path = Path(path)

        with path.open("w", encoding="utf-8") as file:
            yaml.dump(
                self.to_dict(),
                file,
                Dumper=IndentedDumper,
                sort_keys=False,
                allow_unicode=True,
                indent=4
            )

    @classmethod
    def load_yaml(cls, path: str | Path) -> Resume:
        path = Path(path)

        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return cls.model_validate(data)