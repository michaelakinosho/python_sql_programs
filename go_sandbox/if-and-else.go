package main

import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) (v float64, w float64) {
	if v := math.Pow(x, n); v < lim {
		return v, lim
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
		return v, lim
	}
	// can't use v here, though
	// return lim
}

func main() {
	fmt.Printf("First pass:")
	fmt.Println(pow(3, 2, 10))
	fmt.Println("Second pas:")
	fmt.Println(pow(3, 3, 20))
	
}
