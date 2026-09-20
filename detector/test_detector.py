import detector


def test_error_event_is_anomaly():
    event = {"level": "ERROR", "message": "failure"}

    assert detector.detect(event) is True


def test_info_event_is_not_anomaly():
    event = {"level": "INFO", "message": "normal"}

    assert detector.detect(event) is False
