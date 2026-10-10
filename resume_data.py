from resume import (
    Resume,
    Contacts,
    ContactLink,
    Section,
    DateRange,
    Degree,
    EducationEntry,
    ExperienceEntry,
    Author,
    PublicationEntry,
    SkillGroup,
    SkillsEntry,
    month,
)


resume = Resume(
    name="Alessandro Mordasiewicz",
    citizenship="U.S. Citizen",

    contacts=Contacts(
        phone="312-608-0070",
        email="amordasiewi1@gmail.com",
        links=[
            ContactLink(
                label="LinkedIn",
                url="https://www.linkedin.com/in/alessandro-mordasiewicz/",
                display="linkedin.com/in/alessandro-mordasiewicz/",
            ),
        ],
    ),

    sections=[
        # education section
        Section(
            title="Education",
            entries=[
                EducationEntry(
                    institution="Purdue University",
                    location="West Lafayette, IN",
                    degrees=[
                        Degree(
                            degree="M.S. Aeronautics and Astronautics",
                            dates=DateRange(
                                start=month(2027, 1),
                                present=True,
                            ),
                            gpa="4.0/4.0",
                            concentrations=["Astrodynamics"],
                            minors=["Autonomy & Control"]
                        ),
                        Degree(
                            degree="B.S. Aeronautical and Astronautical Engineering",
                            dates=DateRange(
                                start=month(2022, 8),
                                end=month(2026, 5),
                            ),
                            gpa="3.4/4.0",
                            concentrations=["Astrodynamics"],
                            minors=["Computer Science"],
                        ),
                    ],
                    coursework=[
                        "Orbit Mechanics",
                        "Space Traffic Management",
                        "Spacecraft Attitude Dynamics",
                        "Applied Control in Astronautics",
                        "Applied Stochastic Processes",
                        "Control System Analysis",
                        "Geometric Control Methods",
                    ],
                    interests=[
                        "Spacecraft & launch vehicle GNC",
                        "astrodynamics",
                        "mission analysis/design",
                        "modeling & simulation",
                        "software engineering",
                    ],
                ),
            ],
        ),
        # professional experience
        Section(
            title="Professional Experience",
            entries=[

                ExperienceEntry(
                    title="GNC Intern, Mission Design",
                    organization="Relativity Space",
                    location="Long Beach, CA",
                    dates=DateRange(
                        start=month(2026, 5),
                        end=month(2026, 11),
                    ),
                    bullets=[
                        (
                            "Supported the Mission Design group in launch vehicle "
                            "trajectory optimization productionization and day-of-launch "
                            "tooling development for the Terran R medium-to-heavy-lift "
                            "partially reusable launch vehicle."
                        ),
                        (
                            "Responsible for the creation of launch window generation "
                            "and evaluation tooling (Python)."
                        ),
                        (
                            "Enhanced robustness of second-stage guidance algorithm "
                            "for inertial orbit targeting (Rust)."
                        ),
                        (
                            "Conducted preliminary launch vehicle collision avoidance "
                            "and payload separation analyses (Python)."
                        ),
                        (
                            "Worked in conjunction with the Simulation team for several "
                            "extensive 6DoF simulation improvements (C++/Python)."
                        ),
                        (
                            "Extensively used Git (via GitLab) for version control."
                        ),
                    ],
                ),

                ExperienceEntry(
                    title="Flight Mechanics Intern",
                    organization="NASA - Marshall Space Flight Center",
                    location="Huntsville, AL",
                    dates=DateRange(
                        start=month(2025, 5),
                        end=month(2025, 8),
                    ),
                    bullets=[
                        (
                            "Supported the NASA HLS guidance, navigation, & mission "
                            "analysis group (EV42) under the ESSCA contract."
                        ),
                        (
                            "Developed Python/MATLAB tools to enhance lunar DEM fidelity "
                            "for hazard injection and lander tip-over analysis."
                        ),
                        (
                            "Integrated enhanced lunar DEMs into a 6DoF landing "
                            "dynamics simulation."
                        ),
                        (
                            "Verified and validated HLS landing dynamics simulations "
                            "by reconstructing the Apollo 11 landing."
                        ),
                        (
                            "Developed a Python landing visualization tool, reducing "
                            "generation time from 2 hours to 2-3 minutes."
                        ),
                        (
                            "Extensively used Git (via GitHub) for version control."
                        ),
                    ],
                ),

                ExperienceEntry(
                    title="Flight Dynamics Intern",
                    organization="Intelsat (now SES Satellites)",
                    location="McLean, VA",
                    dates=DateRange(
                        start=month(2024, 5),
                        end=month(2024, 8),
                    ),
                    bullets=[
                        (
                            "Supported daily Flight Dynamics operations of over "
                            "70 active GEO satellites."
                        ),
                        (
                            "Developed and maintained an interactive web application "
                            "(Python, React) to analyze critical satellite parameters."
                        ),
                        (
                            "Developed Python scripts for data visualization in "
                            "operational flight dynamics software migrating to Linux."
                        ),
                        (
                            "Evaluated a GPS-based position estimation method against "
                            "existing state estimation systems for GEO satellites."
                        ),
                        (
                            "Gained experience with Git for version control, enabling "
                            "efficient collaboration and code management."
                        ),
                    ],
                ),

                ExperienceEntry(
                    title="Aerospace Engineering Intern",
                    organization="Axiom Aerospace LLC",
                    location="Chicago, IL",
                    dates=DateRange(
                        start=month(2023, 5),
                        end=month(2023, 8),
                    ),
                    bullets=[
                        (
                            "Compiled FAA certification packages including comprehensive "
                            "engineering reports, design drawings, and test & computations "
                            "for Parts Manufacturer Approval (PMA) on FAA Part 23, 25, "
                            "27, and 29 category aircraft."
                        ),
                        (
                            "Created and edited engineering drawings using SolidWorks "
                            "and Adobe Acrobat for various aircraft parts."
                        ),
                        (
                            "Submitted final project files to the FAA Chicago Aircraft "
                            "Certification Office for review and approval."
                        ),
                    ],
                ),
            ],
        ),
        # extracurriculars
        Section(
            title="Extracurriculars",
            entries=[
                ExperienceEntry(
                    title="Undergraduate Teaching Assistant",
                    organization=(
                        "Purdue University Department of Physics and Astronomy"
                    ),
                    location="West Lafayette, IN",
                    dates=DateRange(
                        start=month(2023, 8),
                        end=month(2026, 5),
                    ),
                    bullets=[
                        (
                            "TA for PHYS 172: Modern Mechanics, the introductory "
                            "physics course for first-year engineering students."
                        ),
                        (
                            "Facilitated lab sections of up to 54 students, assisting "
                            "students in understanding basic physics concepts and "
                            "programming in Python."
                        ),
                    ],
                ),
            ],
        ),
        # publications
        Section(
            title="Publications",
            entries=[
                PublicationEntry(
                    authors=[
                        Author(
                            name="R. M. Ali",
                        ),
                        Author(
                            name="A. C. Slagle",
                        ),
                        Author(
                            name="A. Mordasiewicz",
                            highlight=True,
                        ),
                        Author(
                            name="J. Orphee",
                        ),
                        Author(
                            name="P. J. McDonough",
                        ),
                    ],

                    title=(
                        "Apollo 11 Lunar Module Touchdown Dynamics Reconstruction "
                        "Verification and Validation for Human Landing Systems"
                    ),

                    venue=(
                        "48th Annual AAS Guidance, Navigation and Control "
                        "(GN&C) Conference"
                    ),

                    location="Breckenridge, CO",
                    year=2026,

                    identifier=(
                        "NASA Technical Reports Server, Doc. ID 20260000331"
                    ),

                    url="https://ntrs.nasa.gov/citations/20260000331",
                ),
            ],
        ),
        # technical skills
        Section(
            title="Technical Skills",
            entries=[
                SkillsEntry(
                    groups=[
                        SkillGroup(
                            name="Programming",
                            skills=[
                                "MATLAB",
                                "Python",
                                "C/C++",
                                "Rust",
                                "Julia",
                                "Java",
                                "JavaScript",
                                "TypeScript (React)",
                                "HTML/CSS",
                                "Bash",
                                "Git",
                                "R",
                            ],
                        ),
                        SkillGroup(
                            name="Other",
                            skills=[
                                "Simulink",
                                "GMAT",
                                "FreeFlyer",
                                "STK",
                                "Azure DevOps",
                                "GitHub",
                                "GitLab",
                                "Microsoft Office",
                                "Jira",
                                "SolidWorks",
                                "Siemens NX",
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)