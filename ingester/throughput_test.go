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

func BenchmarkLinesPerSecond(b *testing.B) {
	const lines = 1000000

	input := strings.Repeat("event test data\n", lines)

	b.ReportAllocs()
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		scanner := bufio.NewScanner(strings.NewReader(input))

		count := 0

		for scanner.Scan() {
			_, _ = io.Discard.Write(scanner.Bytes())
			count++
		}

		if err := scanner.Err(); err != nil {
			b.Fatal(err)
		}

		if count != lines {
			b.Fatalf("processed %d lines, want %d", count, lines)
		}
	}

	b.ReportMetric(float64(lines)*float64(b.N)/b.Elapsed().Seconds(), "lines/sec")
}
