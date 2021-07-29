/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
*/
class Solution {
    public int search(int[] nums, int target) {
        return searchHelper(nums, 0, nums.length-1, target);
    }
    int searchHelper(int[] nums, int startIndex, int endIndex, int target){
        if(nums == null || nums.length == 0 || startIndex > endIndex){
            return -1;
        }
        int indexVal = (startIndex + endIndex)/2;
        if(nums[indexVal] == target){
            return indexVal;
        }
        if(nums[startIndex] == target){
            return startIndex;
        }
        if(nums[endIndex] == target){
            return endIndex;
        }
        if(nums[indexVal] == nums[startIndex]){
            return searchHelper(nums, startIndex + 1, endIndex, target);
        } 
        else if(nums[startIndex] > nums[indexVal]){
            if(target > nums[endIndex] && target < nums[startIndex]){
                return -1;
            } 
            if(target > nums[indexVal] && target <= nums[endIndex]){
                return searchHelper(nums, indexVal + 1, endIndex, target);
            } 
            else {
                return searchHelper(nums, startIndex, indexVal - 1, target);
            } 
        } else {
            if(target < nums[startIndex] && target > nums[endIndex]){
                return -1;
            }     
            if(target >= nums[startIndex] && target < nums[indexVal]){
                return searchHelper(nums, startIndex, indexVal - 1, target);
            } 
            else {
                return searchHelper(nums, indexVal + 1, endIndex, target);
            } 
        }
    }
}

