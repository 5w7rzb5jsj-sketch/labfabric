import json


def test_fixture_is_valid_jsonl():
    with open("fixtures/events.jsonl", "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    assert len(lines) == 5

    events = [json.loads(line) for line in lines]

    assert events[0]["level"] == "INFO"
    assert events[2]["level"] == "ERROR"
    assert events[4]["level"] == "ERROR"


if __name__ == "__main__":
    test_fixture_is_valid_jsonl()
    print("fixture test passed")
