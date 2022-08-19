package main

import (
	"fmt"
)

// fibonacci is a function that returns
// a function that returns an int
func fibonacci() func(int) int {
	return func(x int) int {
		sum := 0
		if x == 0 {
			sum = 0
		} else if x < 3 {
			sum = 1
		} else if x == 3 {
			sum = 2
		} else {
			add_a := 1
			add_b := 2
			for j:=4; j <=x; j++ {
				sum = add_a + add_b
				add_a = add_b
				add_b = sum
			}
		}
		return sum
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 50; i++ {
		fmt.Println(f(i))
	}
}