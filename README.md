# Cookiecutter DS Mini

This is a Cookiecutter template that can be used to initiate a minimal Python data science project with a minimal set of tools for development
and testing. It supports the following features:

- [uv](https://docs.astral.sh/uv/) for dependency management
- Linting and formatting with [ruff](https://docs.astral.sh/ruff/)
- Testing with [pytest](https://docs.pytest.org/)
- Ready to run [Jupyter](https://jupyter.org/) notebooks
- The canonical set of Python data science packages: [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/), [scikit-learn](https://scikit-learn.org/)

## Quickstart

First you need to [install uv](https://docs.astral.sh/uv/getting-started/installation/), e.g.

    $ curl -LsSf https://astral.sh/uv/install.sh | sh

or on Mac OS X with Homebrew

    $ brew install uv

Then navigate to the directory in which you want to create a project directory, and run

    $ uvx cookiecutter gh:asmaier/cookiecutter-ds-mini

`uvx` runs cookiecutter without installing it permanently.

Afterwards your project directory is ready. For a project named `My Analysis` it will have the following structure
```
my-analysis/
├── .gitignore
├── README.md
├── data
│   └── iris.csv
├── notebooks
│   └── example.ipynb
├── pyproject.toml
├── src
│   └── my_analysis
│       ├── resources
│       │   └── .gitkeep
│       ├── __init__.py
│       └── utils.py
└── tests
    ├── resources
    │   └── .gitkeep
    └── test_utils.py
```
The project directory and distribution name (`my-analysis`) are derived from the project name with hyphens,
the importable package name (`my_analysis`) with underscores.

The `data` directory is meant for all kinds of data which you might analyse or explore
with jupyter notebooks in the `notebooks` directory. The code for your python package goes
into the `src/my_analysis` directory.
The tests for your code go into the `tests` directory. Your package and test directory
hold a `resources` directory which is meant for static resources like images, test files, ...
which your package or tests might need.

Just change into the newly created directory and install the dependencies

    $ cd my-analysis
    $ uv sync

You are now ready to start developing. To create your first jupyter notebooks
just do

    $ uv run jupyter lab

That's all Folks! For more information also have a look at the `README.md` created for your project.

## Developing this template

The tests in `tests/` generate projects from the template and run ruff, pytest and the example notebook in them:

    $ uv run pytest

## Acknowledgements

This project is inspired by 

- https://github.com/fpgmaas/cookiecutter-poetry
- https://github.com/drivendata/cookiecutter-data-science
- https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
- https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html
