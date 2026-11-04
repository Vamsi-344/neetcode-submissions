func hasDuplicate(nums []int) bool {
    visited := make(map[int]int)
	for _, v := range nums {
		_, found := visited[v]
		if found {
			return true
		} else {
			visited[v] = 1
			continue
		}
	}
	return false
}
