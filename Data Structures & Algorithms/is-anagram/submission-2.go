import (
	"maps"
)

func stringCharMap(s string) map[rune]int {
	charMap := make(map[rune]int)
	for _, v := range s {
		_, ok := charMap[v]
		if ok {
			charMap[v] += 1
		} else {
			charMap[v] = 1
		}
	}
	return charMap
}

func isAnagram(s string, t string) bool {
	if maps.Equal(stringCharMap(s), stringCharMap(t)){
		return true
	} else {
		return false
	}
}
