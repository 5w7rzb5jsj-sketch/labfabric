import json
import subprocess
import sys


def test_go_to_python_syslog_pipeline():
    input_data = (
        "<13>Sep 20 12:00:05 server1 "
        "systemd[1]: Started service\n"
        "<11>Sep 20 12:00:09 server1 "
        "kernel: Disk error detected\n"
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
    assert output[0]["event"]["format"] == "syslog"
    assert output[0]["event"]["priority"] == 11
    assert output[0]["event"]["host"] == "server1"
    assert output[0]["event"]["message"] == "kernel: Disk error detected"

    print("full Go -> Python syslog pipeline passed")


if __name__ == "__main__":
    test_go_to_python_syslog_pipeline()
