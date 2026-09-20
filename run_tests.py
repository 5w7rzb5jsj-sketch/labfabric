import subprocess
import sys


def main():
    print("Running detector tests...")
    subprocess.run(
        [sys.executable, "detector/run_tests.py"],
        check=True,
    )

    print("Running end-to-end pipeline test...")
    subprocess.run(
        [sys.executable, "test_pipeline.py"],
        check=True,
    )

    print("ALL TESTS PASSED")


if __name__ == "__main__":
    main()
