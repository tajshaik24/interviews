/* 
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
*/

class Solution {
    public boolean search(int[] nums, int target) {
        return searchHelper(nums, 0, nums.length-1, target);
    }
    boolean searchHelper(int[] nums, int startIndex, int endIndex, int target){
        if(nums == null || nums.length == 0 || startIndex > endIndex){
            return false;
        }
        int indexVal = (startIndex + endIndex)/2;
        if(nums[indexVal] == target || nums[startIndex] == target || nums[endIndex] == target){
            return true;
        }
        if(nums[indexVal] == nums[startIndex]){
            return searchHelper(nums, startIndex + 1, endIndex, target);
        } 
        else if(nums[startIndex] > nums[indexVal]){
            if(target > nums[endIndex] && target < nums[startIndex]){
                return false;
            } 
            if(target > nums[indexVal] && target <= nums[endIndex]){
                return searchHelper(nums, indexVal + 1, endIndex, target);
            } 
            else {
                return searchHelper(nums, startIndex, indexVal - 1, target);
            } 
        } else {
            if(target < nums[startIndex] && target > nums[endIndex]){
                return false;
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