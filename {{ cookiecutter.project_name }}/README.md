# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup project

    $ poetry install

## Start jupyter notebooks

    $ poetry run jupyter lab

## Run linter and tests

    $ poetry run ruff check
    $ poetry run pytest -s

## Teardown project

    $ poetry env remove --all