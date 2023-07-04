import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="GeCCo",
    version="v1.0",
    author="Tim Verschuren",
    author_email="t.verschuren@wi.knaw.nl",
    description="GeCCo (Gene Content Counter) is a Python package that allows for the visualisation of normalised gene counts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TimVerschuren/GeCCo",
    project_urls={
        "Bug Tracker": "https://github.com/TimVerschuren/GeCCo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "Bio", "scipy", "plotly"],
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "gecco = GeCCo_src.cli:main",
        ]
    }
)
