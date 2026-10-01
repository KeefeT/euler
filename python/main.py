#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent / "problems"
    problems = {}
    for folder in root.iterdir():
        prefix, separator, title = folder.name.partition("_")
        number = prefix.removeprefix("p")
        if folder.is_dir() and separator and prefix.startswith("p") and number.isdigit():
            scripts = sorted(folder.glob("solution*.py"))
            if scripts:
                problems[int(number)] = (title.replace("_", " "), scripts)

    if not problems:
        print("No solutions found.")
        return 0

    print("Available problems:")
    for number, (title, _) in sorted(problems.items()):
        print(f"  {number}: {title}")

    while True:
        answer = input("\nProblem number (q to quit): ").strip()
        if answer.lower() == "q":
            return 0
        if not answer.isdecimal() or int(answer) not in problems:
            print("Please enter one of the available problem numbers.")
            continue

        _, scripts = problems[int(answer)]
        script = scripts[0]
        if len(scripts) > 1:
            for index, candidate in enumerate(scripts, start=1):
                print(f"  {index}: {candidate.name}")
            while True:
                choice = input("Which solution? (q to quit): ").strip()
                if choice.lower() == "q":
                    return 0
                if choice.isdecimal() and 1 <= int(choice) <= len(scripts):
                    script = scripts[int(choice) - 1]
                    break
                print("Please enter a solution number from the list.")

        print(f"\nRunning {script.parent.name}/{script.name}\n", flush=True)
        return subprocess.run([sys.executable, str(script)], cwd=script.parent).returncode


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye.")
