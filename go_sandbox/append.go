package main

import (
	"fmt"
)

func main() {
	var s []int
	printSlice("s", s)

	// append works on nil slices.
	s = append(s, 0)
	printSlice("s", s)

	// The slice grows as needed.
	s = append(s, 1)
	printSlice("s", s)

	// We can add more than one element at a time.
	t := []int{1,2,3}
	printSlice("t", t)

	s = append(s, 4,5,6)
	printSlice("s", s)
}

func printSlice(n string, s []int) {
	fmt.Printf("%v len=%d cap=%d %v\n", n, len(s), cap(s), s)
}