import json
import subprocess
import sys


def test_detector_pipeline():
    events = [
        {"level": "INFO", "message": "normal event"},
        {"level": "ERROR", "message": "failure event"},
    ]

    input_data = "\n".join(json.dumps(event) for event in events) + "\n"

    result = subprocess.run(
        [sys.executable, "detector/detector.py"],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )

    output = [json.loads(line) for line in result.stdout.splitlines()]

    assert len(output) == 1
    assert output[0]["anomaly"] is True
    assert output[0]["event"]["level"] == "ERROR"

    print("pipeline test passed")


if __name__ == "__main__":
    test_detector_pipeline()
