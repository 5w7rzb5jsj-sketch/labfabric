package main

import (
	"bufio"
	"io"
	"strings"
	"testing"
)

func BenchmarkInputLineProcessing(b *testing.B) {
	input := strings.Repeat("event test data\n", 1000)

	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		scanner := bufio.NewScanner(strings.NewReader(input))

		for scanner.Scan() {
			_, _ = io.Discard.Write([]byte(scanner.Text()))
		}

		if err := scanner.Err(); err != nil {
			b.Fatal(err)
		}
	}
}
