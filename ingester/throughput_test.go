package main

import (
	"bufio"
	"io"
	"strings"
	"testing"
)

func BenchmarkThroughput(b *testing.B) {
	const lines = 100000

	input := strings.Repeat("event test data\n", lines)

	b.SetBytes(int64(len(input)))
	b.ReportAllocs()
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		scanner := bufio.NewScanner(strings.NewReader(input))

		for scanner.Scan() {
			_, _ = io.Discard.Write(scanner.Bytes())
		}

		if err := scanner.Err(); err != nil {
			b.Fatal(err)
		}
	}
}
