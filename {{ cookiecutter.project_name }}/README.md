# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup project

    $ uv sync

## Start jupyter notebooks

    $ uv run jupyter lab

## Run linter and tests

    $ uv run ruff check
    $ uv run pytest -s

## Teardown project

    $ rm -r .venv uv.lock