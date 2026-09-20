import json
import subprocess
import sys


def test_malformed_input_does_not_break_pipeline():
    input_data = (
        '{"level":"INFO","message":"before malformed"}\n'
        'THIS IS NOT VALID JSON OR SYSLOG\n'
        '{"level":"ERROR","message":"after malformed"}\n'
    )

    go_process = subprocess.Popen(
        ["go", "run", "."],
        cwd="ingester",
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    ingester_output, ingester_error = go_process.communicate(input_data)

    if go_process.returncode != 0:
        raise AssertionError(
            f"Go ingester failed: {ingester_error}"
        )

    detector = subprocess.run(
        [sys.executable, "detector/detector.py"],
        input=ingester_output,
        text=True,
        capture_output=True,
        check=True,
    )

    output = [
        json.loads(line)
        for line in detector.stdout.splitlines()
        if line.strip()
    ]

    assert len(output) == 1
    assert output[0]["anomaly"] is True
    assert output[0]["event"]["level"] == "ERROR"
    assert output[0]["event"]["message"] == "after malformed"

    print("malformed input pipeline passed")


if __name__ == "__main__":
    test_malformed_input_does_not_break_pipeline()
