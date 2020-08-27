package trappingrainwater

import "testing"

func TestEmpty(t *testing.T) {
	assert(t, 0, trap([]int{}))
}

func TestHill(t *testing.T) {
	assert(t, 0, trap([]int{0, 1, 2, 1, 0}))
}

func TestBowl(t *testing.T) {
	assert(t, 4, trap([]int{2, 1, 0, 1, 2}))
}

func TestNormal(t *testing.T) {
	assert(t, 6, trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}))
}

// Helper
func assert(t *testing.T, expected int, actual int) {
	if actual != expected {
		t.Errorf("Expected %d; Actual %d", expected, actual)
	}
}
