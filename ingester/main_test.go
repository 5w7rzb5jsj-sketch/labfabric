package main

import (
	"bufio"
	"strings"
	"testing"
)

func TestInputLinesArePreserved(t *testing.T) {
	input := "event one\nevent two\nevent three\n"

	scanner := bufio.NewScanner(strings.NewReader(input))

	var got []string
	for scanner.Scan() {
		got = append(got, scanner.Text())
	}

	want := []string{"event one", "event two", "event three"}

	if len(got) != len(want) {
		t.Fatalf("got %d lines, want %d", len(got), len(want))
	}

	for i := range want {
		if got[i] != want[i] {
			t.Errorf("line %d: got %q, want %q", i, got[i], want[i])
		}
	}
}
