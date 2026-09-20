package main

import (
	"encoding/json"
	"testing"
)

func TestJSONEventIsValid(t *testing.T) {
	input := `{"level":"ERROR","message":"disk failure"}`

	var event map[string]interface{}

	if err := json.Unmarshal([]byte(input), &event); err != nil {
		t.Fatalf("invalid JSON: %v", err)
	}

	if event["level"] != "ERROR" {
		t.Fatalf("got level %v, want ERROR", event["level"])
	}

	if event["message"] != "disk failure" {
		t.Fatalf("got message %v, want disk failure", event["message"])
	}
}
