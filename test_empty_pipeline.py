import subprocess
import sys


def test_empty_input_pipeline():
    go_process = subprocess.Popen(
        ["go", "run", "."],
        cwd="ingester",
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    ingester_output, ingester_error = go_process.communicate("")

    if go_process.returncode != 0:
        raise AssertionError(
            f"Go ingester failed: {ingester_error}"
        )

    assert ingester_output == ""

    detector = subprocess.run(
        [sys.executable, "detector/detector.py"],
        input=ingester_output,
        text=True,
        capture_output=True,
        check=True,
    )

    assert detector.stdout == ""

    print("empty input pipeline passed")


if __name__ == "__main__":
    test_empty_input_pipeline()
