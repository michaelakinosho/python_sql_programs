package main

import "fmt"

func main() {
	defer fmt.Println("First")

	defer fmt.Println("Second")

	fmt.Println("Third")
}