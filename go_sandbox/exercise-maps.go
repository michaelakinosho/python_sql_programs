package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	words := strings.Fields(s)
	m := make(map[string]int)
	
	for i := 0; i < len(words); i++ {
		if _, ok := m[words[i]]; ok == false {
			m[words[i]] = 1
		} else {
			m[words[i]]++
		}
	}
	return m
}

func main() {
	wc.Test(WordCount)
}
