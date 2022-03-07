# DnDMan

DndMan is a website for managing DnD characters, and games.

# Developing

To set up a development environment, follow the instructions below.

## Dependencies

You will need to have Python 3.9 or greater to run this.
You will also need to have the [Poetry](https://python-poetry.org/) package manager for python.

## Setup

```bash
git clone https://github.com/W1nter-isHere/DnDMan.git
cd DnDMan
poetry config virtualenvs.in-project true
poetry install
poetry shell
```

## Running

Running the development server:
Note: Every time you open a new terminal you must run `poetry shell` again. Or else `invoke` will not work.

```bash
invoke debug
```

Running the production server (Not implemented):

```bash
invoke start
```