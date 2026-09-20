import json
import re
import sys


SYSLOG_PATTERN = re.compile(
    r"^<(?P<priority>\d+)>(?P<timestamp>\w{3}\s+\d+\s+\d+:\d+:\d+)\s+"
    r"(?P<host>\S+)\s+(?P<message>.*)$"
)


def parse_event(line):
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        pass

    match = SYSLOG_PATTERN.match(line)
    if not match:
        return None

    priority = int(match.group("priority"))

    return {
        "format": "syslog",
        "priority": priority,
        "timestamp": match.group("timestamp"),
        "host": match.group("host"),
        "message": match.group("message"),
    }


def detect(event):
    if event.get("level") == "ERROR":
        return True

    if event.get("format") == "syslog" and event.get("priority", 0) <= 11:
        return True

    return False


def main():
    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue

        event = parse_event(line)

        if event is None:
            continue

        if detect(event):
            print(json.dumps({
                "anomaly": True,
                "event": event
            }))


if __name__ == "__main__":
    main()
