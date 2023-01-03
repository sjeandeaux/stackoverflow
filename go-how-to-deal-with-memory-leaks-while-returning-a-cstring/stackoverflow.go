package main

/*
#include <stdlib.h>
*/
import "C"
import (
	"log"
	"unsafe"
)

//export GetData
func GetData(symbol, day, month, year *C.char) *C.char {
	combine := "combine"
	log.Println(string(combine))
	return C.CString(string(combine))
}

//export FreeMe
func FreeMe(data *C.char) {
	C.free(unsafe.Pointer(data))
}

func main() {}
