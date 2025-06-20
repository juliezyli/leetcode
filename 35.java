public class problem35 {
    public int searchInsert(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        for (int i = 0; i < nums.length - 1; i++) {
           if (target > nums[i]) {
                if (target < nums[i + 1]) {
                    return i + 1;
                }
            }
        }
        if (target < nums[0]) {
            return 0;
        }
        return nums.length; 
    }
}
