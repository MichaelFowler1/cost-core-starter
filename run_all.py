"""Run every example in this folder through cost-core, one after another.

    python run_all.py              # all of them
    python run_all.py cost-risk    # just one

Each writes its results to results/<name>/: report.xlsx, brief.pptx, the
charts and CSVs. Every number in examples/ is invented.
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EX = HERE / "examples"

RUNS = {
    "cost-risk": ["cost-risk", "--data", EX / "estimate.xlsx"],
    "evm": ["evm", "--data", EX / "evm.xlsx", "--units", "thousands"],
    "schedule": ["schedule-check", "--mspdi", EX / "schedule.xml"],
    "jcl": ["jcl", "--spec", EX / "jcl.xlsx"],
    "aoa": ["aoa", "--spec", EX / "aoa.xlsx"],
    "portfolio": ["portfolio", "--spec", EX / "portfolio.xlsx"],
}


def main(names):
    unknown = [n for n in names if n not in RUNS]
    if unknown:
        sys.exit(f"Unknown example {', '.join(unknown)}; choose from {', '.join(RUNS)}.")
    failed = []
    for name in names or RUNS:
        out = HERE / "results" / name
        args = [sys.executable, "-m", "cost_core", *map(str, RUNS[name]), "--out", str(out)]
        print(f"\n=== {name} " + "=" * (60 - len(name)))
        if subprocess.run(args).returncode:
            failed.append(name)
    print("\nResults are in the results folder: open report.xlsx in each one.")
    if failed:
        sys.exit(f"These didn't finish: {', '.join(failed)}")


if __name__ == "__main__":
    main(sys.argv[1:])
