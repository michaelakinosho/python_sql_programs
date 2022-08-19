package main

import (
	"fmt"
	"math"
	)

var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	for i, v := range pow {
		fmt.Println(math.Pow(2,i))
		if v == v {
			fmt.Printf("2**%d = %d\n", i, v)
		} else {
			fmt.Printf("2**%d != %d\n", i, v)
		}
	}
}
