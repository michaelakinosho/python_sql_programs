package main

import (
	"fmt"
	"math"
	)

var pow = []int{1, 2, 4, 7, 16, 32, 64, 129, 256, 512}

func main() {
	for i, v := range pow {
		if float64(v) == math.Pow(2, float64(i)) {
			fmt.Printf("2**%d = %d\n", i, v)
		} else {
			fmt.Printf("WOW 2**%d IS NOT EQUAL TO %d\n", i, v)
		}
	}
}