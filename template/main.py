import tasks  # triggers @task() registration
from decorators import TASKS


def main():
    for (desc, task) in TASKS:
        print(f"------Task {desc}------")
        task()


if __name__ == "__main__":
    main()
