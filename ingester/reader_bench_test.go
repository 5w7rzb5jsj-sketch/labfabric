package main

import (
	"bufio"
	"io"
	"strings"
	"testing"
)

func BenchmarkBufferedReader(b *testing.B) {
	const lines = 100000

	input := strings.Repeat("event test data\n", lines)

	b.SetBytes(int64(len(input)))
	b.ReportAllocs()
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		reader := bufio.NewReader(strings.NewReader(input))

		for {
			_, err := reader.ReadBytes('\n')
			if err == io.EOF {
				break
			}
			if err != nil {
				b.Fatal(err)
			}
		}
	}
}
