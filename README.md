# Practice Repo

NumPy exercises and LeetCode solutions with a built-in test runner.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## NumPy Exercises

Working through the [100 numpy exercises](https://github.com/rougier/numpy-100).

```bash
uv run tasks          # run all tasks
uv run tasks 33       # run only task 33
uv run tasks 5 6 7    # run multiple tasks
```

Each exercise is a function decorated with `@task("description")` and `@task_skipper(skip=False)`. Write your solution inside the function body, replacing `pass`. Flip `skip=True` to skip it on future runs.

## LeetCode Solutions

Solutions organized by category with test cases and reflective notes.

```bash
uv run leetcode                         # run all problems
uv run leetcode 1 49                    # run specific problems by number
uv run leetcode --category two_pointer  # run all in a category
uv run leetcode --phase 1              # run all phase 1 problems
uv run leetcode --list                 # list all problems
```

### Adding a new problem

1. Create `src/leetcode_tasks/problems/{category}/p{NNNN}_{name}.py`
2. Add metadata, Solution class, and test cases following the existing file format
3. Run `uv run leetcode {NNNN}` to verify

The runner auto-discovers new files — no registration needed.

### Phases

- Phase 1: Foundations (arrays/hashing, two pointer)
- Phase 2: Core data structures
- Phase 3: Intermediate patterns
- Phase 4: Advanced and mock practice

## Structure

```
src/
  nmpy_tasks/          # NumPy exercises
    tasks.py           # all 100 task functions
    decorators.py      # @task() and @task_skipper() decorators
    main.py            # CLI runner
  leetcode_tasks/      # LeetCode solutions
    runner.py          # CLI runner with test engine
    problems/
      arrays_and_hashing/
      two_pointer/
```
