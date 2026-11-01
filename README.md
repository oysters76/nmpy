# NumPy 100 Exercises

Working through the [100 numpy exercises](https://github.com/rougier/numpy-100) to learn and practice numpy.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Run

```bash
uv run tasks
```

## Structure

- `src/nmpy_tasks/tasks.py` — all 100 task functions
- `src/nmpy_tasks/decorators.py` — `@task()` for auto-registration, `@task_skipper()` to skip completed tasks
- `src/nmpy_tasks/main.py` — runs all registered tasks

## How it works

Each exercise is a function decorated with `@task("description")` and `@task_skipper(skip=False)`.

Write your solution inside the function body, replacing `pass`. Once done, flip `skip=True` to skip it on future runs.
