import sys
import copy
import importlib
from pathlib import Path


def discover_problems():
    problems = {}
    problems_dir = Path(__file__).parent / "problems"

    for category_dir in sorted(problems_dir.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith("_"):
            continue
        category = category_dir.name
        for filepath in sorted(category_dir.glob("p[0-9]*.py")):
            stem = filepath.stem
            num = int(stem.split("_", 1)[0][1:])
            mod_path = f"leetcode_tasks.problems.{category}.{stem}"
            mod = importlib.import_module(mod_path)

            problems[num] = {
                "module": mod,
                "category": category,
                "title": getattr(mod, "title", stem),
                "phase": getattr(mod, "phase", None),
                "difficulty": getattr(mod, "difficulty", None),
            }
    return problems


def run_tests(problem_info):
    mod = problem_info["module"]
    tests_def = getattr(mod, "tests", None)
    if tests_def is None:
        print("  No tests defined")
        return None

    solution = mod.Solution()
    method_name = tests_def["method"]
    method = getattr(solution, method_name)
    compare_fn = getattr(mod, "compare", lambda result, expected: result == expected)

    passed = 0
    total = len(tests_def["cases"])

    for case in tests_def["cases"]:
        args = copy.deepcopy(case["args"])
        expected = case["expected"]
        args_repr = ", ".join(repr(a) for a in case["args"])

        try:
            result = method(*args)
            if compare_fn(result, expected):
                passed += 1
                print(f"  \033[32mPASS\033[0m {method_name}({args_repr})")
            else:
                print(f"  \033[31mFAIL\033[0m {method_name}({args_repr})")
                print(f"       got:      {result!r}")
                print(f"       expected: {expected!r}")
        except Exception as exc:
            print(f"  \033[31mERROR\033[0m {method_name}({args_repr})")
            print(f"        {type(exc).__name__}: {exc}")

    return passed, total


def main():
    raw_args = sys.argv[1:]
    problems = discover_problems()

    nums = set()
    category_filter = None
    phase_filter = None
    list_mode = False
    i = 0
    while i < len(raw_args):
        if raw_args[i] == "--category":
            category_filter = raw_args[i + 1]
            i += 2
        elif raw_args[i] == "--phase":
            phase_filter = int(raw_args[i + 1])
            i += 2
        elif raw_args[i] == "--list":
            list_mode = True
            i += 1
        else:
            nums.add(int(raw_args[i]))
            i += 1

    selected = {
        num: info
        for num, info in sorted(problems.items())
        if (not nums or num in nums)
        and (not category_filter or info["category"] == category_filter)
        and (not phase_filter or info.get("phase") == phase_filter)
    }

    if not selected:
        print("No matching problems found.")
        return

    if list_mode:
        for num, info in selected.items():
            phase_str = f"P{info['phase']}" if info.get("phase") else "  "
            diff = info.get("difficulty", "")
            print(f"  #{num:<5} {info['title']:<40} [{info['category']}] {phase_str} {diff}")
        return

    total_passed = 0
    total_cases = 0
    for num, info in selected.items():
        diff = info.get("difficulty", "")
        print(f"\n{'=' * 50}")
        print(f"#{num} {info['title']}  [{info['category']}]  {diff}")
        print(f"{'=' * 50}")
        result = run_tests(info)
        if result:
            p, t = result
            total_passed += p
            total_cases += t

    print(f"\n{'─' * 50}")
    if total_cases > 0:
        color = "\033[32m" if total_passed == total_cases else "\033[33m"
        print(f"Total: {color}{total_passed}/{total_cases} passed\033[0m")
    else:
        print("No test cases found.")
