package main

import (
	"fmt"
	"strings"
	"strconv"
)

func main() {
	// Create a tic-tac-toe board.
	board := [][]string{
		[]string{" ","1","2","3"},
		[]string{"1","_", "_", "_"},
		[]string{"2","_", "_", "_"},
		[]string{"3","_", "_", "_"},
	}

	// The players take turns.
	moves := [][]string{
		[]string{"1","1","X"},
		[]string{"3","3","O"},
		[]string{"2","3","X"},
		[]string{"2","1","O"},
		[]string{"1","3","X"},
	}
	
	for j := 0; j < len(moves); j++ { 
		r, _ := strconv.Atoi(moves[j][0])
		c, _ := strconv.Atoi(moves[j][1])
		//if err != nil {
			//fmt.Println("Not nil")
		//}
		P := moves[j][2]
		board[r][c] = P
		fmt.Printf("Board layout after player: %v\n", P)
		for i := 0; i < len(board); i++ {
			fmt.Printf("%s\n", strings.Join(board[i], " "))
		}
		fmt.Println("\n")
	}
}