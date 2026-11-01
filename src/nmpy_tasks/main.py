import nmpy_tasks.tasks  # noqa: F401 — triggers @task() registration
from nmpy_tasks.decorators import TASKS


def main():
    for (desc, task) in TASKS:
        print(f"------Task {desc}------")
        task()


if __name__ == "__main__":
    main()
