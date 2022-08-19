package main

import "fmt"

func main() {
	s := []int{2,3,5,7,11,13}

	fmt.Println(s[1:4])

	fmt.Println(s[:2])

	fmt.Println(s[1:])
}