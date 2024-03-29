/* Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome. */

//Follow up:
//Could you solve it without converting the integer to a string?

class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0 || x >= Math.pow(2,31) - 1){
            return false;
        }
        Stack<Integer> stack = new Stack<Integer>();
        int initialValue = x;
        int endValue = 0;
        while(x > 0){
            stack.push(x%10);
            x = x/10;
        }
        int counter = 0;
        while(!stack.isEmpty()){
            endValue += stack.pop() * Math.pow(10, counter);
            counter++;
        }
        return initialValue == endValue;
    }
}