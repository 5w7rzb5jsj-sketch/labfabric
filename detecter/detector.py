import json
import sys


def detect(event):
    if event.get("level") == "ERROR":
        return True

    return False


def main():
    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue

        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        if detect(event):
            print(json.dumps({
                "anomaly": True,
                "event": event
            }))


if __name__ == "__main__":
    main()
