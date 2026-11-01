import sys
import nmpy_tasks.tasks  # noqa: F401 — triggers @task() registration
from nmpy_tasks.decorators import TASKS


def main():
    args = sys.argv[1:]

    if args:
        nums = {int(a) for a in args}
        selected = [(desc, t) for desc, t in TASKS if _task_num(t) in nums]
        if not selected:
            print(f"No tasks found for: {', '.join(args)}")
            return
    else:
        selected = TASKS

    for desc, task in selected:
        print(f"------Task {_task_num(task)}: {desc}------")
        task()


def _task_num(func):
    return int(func.__name__.removeprefix("task"))


if __name__ == "__main__":
    main()
