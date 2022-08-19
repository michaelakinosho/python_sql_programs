package main

import (
	"fmt"
	"math"
)

func compute(fn func(float64, float64) float64) float64 {
	return fn(3,4)
}

func main() {
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	adding := func(a, b float64) float64 {
		return a + b
	}
	fmt.Println(hypot(5, 12))
	fmt.Println(compute(hypot), "\n")

	fmt.Println(adding(2, 3))
	fmt.Println(compute(adding),"\n")

	fmt.Println(compute(math.Pow))
}