# Cookiecutter DS Mini

This is a Cookiecutter template that can be used to initiate a minimal Python data science project with a minimal set of tools for development
and testing. It supports the following features:

- [Poetry](https://python-poetry.org/) for dependency management
- Code quality with [ruff](https://github.com/charliermarsh/ruff)
- Testing with [pytest](https://docs.pytest.org/)
- Ready to run [Jupyter](https://jupyter.org/) notebooks
- The canonical set of Python data science packages: [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/), [scikit-learn](https://scikit-learn.org/)

## Quickstart

First you need to install cookiecutter:

### Linux, Windows

    $ pip install pipx
    $ pipx install cookiecutter


### Homebrew on Mac OS X

    $ brew install cookiecutter


Then navigate to the directory in which you want to
create a project directory, and run the following commands

    $ cookiecutter https://github.com/asmaier/cookiecutter-ds-mini.git


Afterwards your project directory is ready. It will have the following structure
```
└── {{ cookiecutter.project_name }}
    ├── README.md
    ├── data
    │   └── iris.csv
    ├── notebooks
    │   └── example.ipynb
    ├── pyproject.toml
    ├── src
    │   └── {{ cookiecutter.project_slug }}
    │       ├── __init__.py
    │       └── utils.py
    └── tests
        ├── resources
        │   └── .gitkeep
        └── test_utils.py
```
Just change into the newly
created directory and install the dependencies

    $ cd <project_name>
    $ poetry install

You are now ready to start developing. To create your first jupyter notebooks
just do

    $ poetry run jupyter lab

That's all Folks! For more information also have a look at the `README.md` created for your project.

## Acknowledgements

This project is inspired by 

- https://github.com/fpgmaas/cookiecutter-poetry
- https://github.com/drivendata/cookiecutter-data-science
