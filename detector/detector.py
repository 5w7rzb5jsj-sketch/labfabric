import json
import re
import sys
SYSLOG_PATTERN = re.compile(
    r"^<(?P<priority>\d+)>(?P<timestamp>\w{3}\s+\d+\s+\d+:\d+:\d+)\s+"
    r"(?P<host>\S+)\s+(?P<message>.*)$"
)
def parse_event(line):
    stripped = line.strip()
    if not stripped:
        return None
    if stripped[0] in "{[":
        try:
            return json.loads(stripped)
        except json.JSONDecodeError:
            return None
    match = SYSLOG_PATTERN.match(stripped)
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
    write = sys.stdout.write
    for line in sys.stdin:
        event = parse_event(line)
        if event is None:
            continue
        if detect(event):
            write(json.dumps({
                "anomaly": True,
                "event": event
            }))
            write("\n")
if __name__ == "__main__":
    main()
