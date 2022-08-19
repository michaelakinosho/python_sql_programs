package main

import "fmt"

func main() {
	sum := 0.0
	for i := 0; i < 10; i++ {
		sum += float64(i)/2
	}
	fmt.Printf("sum is type %T, sum is value %v", sum, sum)
}