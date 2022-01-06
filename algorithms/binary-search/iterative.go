func search(nums []int, target int) int {
    var pivot int
    left := 0
    right := len(nums) - 1
    
    for left <= right {
        pivot = left + (right - left)/2
        
        if target == nums[pivot] {
            return pivot
        }
        if target < nums[pivot] {
            right = pivot - 1
        } else {
            left = pivot + 1
        }
    }
    
    return -1
}