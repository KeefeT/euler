import contextlib
import importlib
import io
import os
from pathlib import Path
import shlex
import subprocess
import sys
import tempfile
import unittest

from answers import ANSWERS


ROOT = Path(__file__).resolve().parents[2]


class SolutionTests(unittest.TestCase):
    def test_imports_do_not_print_or_run_solutions(self):
        # Fresh processes prevent another test's imports from masking side effects.
        for source in sorted((ROOT / "python/problems").glob("p*/solution*.py")):
            name = ".".join(source.relative_to(ROOT / "python").with_suffix("").parts)
            with self.subTest(module=name):
                result = subprocess.run(
                    [sys.executable, "-c", f"import {name}"],
                    cwd=ROOT, capture_output=True, text=True, check=True,
                )
                self.assertEqual(result.stdout, "")


def answer_test(source, expected):
    def test(self):
        name = ".".join(source.relative_to(ROOT / "python").with_suffix("").parts)
        module = importlib.import_module(name)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            answer = module.solve()
        self.assertIs(type(answer), int)
        self.assertEqual(answer, expected)
        self.assertEqual(output.getvalue(), "", "solve() should return without printing")

    return test


for source in sorted((ROOT / "python/problems").glob("p*/solution*.py")):
    number = int(source.parent.name.split("_", 1)[0][1:])
    # Missing expected answers should fail loudly when adding another solution.
    expected = ANSWERS[number]
    name = f"test_{source.parent.name}_{source.stem}"
    setattr(SolutionTests, name, answer_test(source, expected))


class CSolutionTests(unittest.TestCase):
    def test_problem001_return_value_and_output(self):
        directory = ROOT / "c"
        relative = "problems/p001_multiples_of_3_or_5/solution"
        subprocess.run(["make", f"build/{relative}"], cwd=directory,
                       check=True, capture_output=True, text=True)
        result = subprocess.run([str(directory / "build" / relative)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), str(ANSWERS[1]))

        # Link a tiny test main against solve() to check its actual return value.
        with tempfile.TemporaryDirectory() as temporary:
            temporary = Path(temporary)
            harness = temporary / "test.c"
            harness.write_text(
                f"int solve(void);\nint main(void) {{ return solve() != {ANSWERS[1]}; }}\n"
            )
            executable = temporary / "test"
            command = shlex.split(os.environ.get("CC", "cc"))
            command += ["-std=c11", "-Wall", "-Wextra", "-DEULER_TEST",
                        str(directory / f"{relative}.c"), str(harness), "-o", str(executable)]
            subprocess.run(command, check=True, capture_output=True, text=True)
            result = subprocess.run([str(executable)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
