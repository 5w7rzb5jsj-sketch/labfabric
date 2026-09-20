import detector


def test_error_event_is_anomaly():
    event = {"level": "ERROR", "message": "failure"}

    assert detector.detect(event) is True


def test_info_event_is_not_anomaly():
    event = {"level": "INFO", "message": "normal"}

    assert detector.detect(event) is False


def test_syslog_is_parsed():
    line = (
        "<11>Sep 20 12:00:09 server1 "
        "kernel: Disk error detected"
    )

    event = detector.parse_event(line)

    assert event is not None
    assert event["format"] == "syslog"
    assert event["priority"] == 11
    assert event["host"] == "server1"


def test_high_priority_syslog_is_anomaly():
    line = (
        "<11>Sep 20 12:00:09 server1 "
        "kernel: Disk error detected"
    )

    event = detector.parse_event(line)

    assert detector.detect(event) is True


def test_normal_syslog_is_not_anomaly():
    line = (
        "<13>Sep 20 12:00:05 server1 "
        "systemd[1]: Started service"
    )

    event = detector.parse_event(line)

    assert detector.detect(event) is False
