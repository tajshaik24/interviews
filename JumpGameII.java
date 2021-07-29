/*
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
*/
class Solution {
    public int jump(int[] nums) {
        if (nums.length == 1) { //no jumps required because small array
            return 0;
        }
        int count = 0; //initialize some count
        int i = 0; //initialize an index i
        while (i + nums[i] < nums.length - 1) { //want to check to see if we reach the end of the array
            int maxVal = 0; //checking the maxVal 
            int maxValIndex = 0; //generating the index of the maxVal
            for (int j = 1; j <= nums[i]; j++) { //going through all the values
                if (nums[j + i] + j > maxVal) {
                    maxVal = nums[j + i] + j; //setting that to the maxVal
                    maxValIndex = i + j; //setting a new Index
                }
            }
            i = maxValIndex; //setting a new value for I
            count++; //adding a count
        }
        return count + 1; //adding 1 to account for last index 
    }
}