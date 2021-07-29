//Given a 32-bit signed integer, reverse digits of an integer.

//Example 1:
//Input: 123
//Output: 321

//Example 2:
//Input: -123
//Output: -321

//Example 3:
//Input: 120
//Output: 21

//Note:
//Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution {
    public int reverse(int x) {
        if(x > Math.pow(2,31) - 1 || x < -Math.pow(2,31)){
            return 0;
        }
        Stack<Integer> stack_ints = new Stack<Integer>();
        int reverseNumber = 0;
        boolean isNegative = x < 0 ? true : false;
        if(isNegative){
            x = x * -1;
        }
        while(x > 0){
            stack_ints.push(x%10);
            x = x/10;
        }
        int counter = 0;
        while(!stack_ints.empty()){
            reverseNumber += stack_ints.pop() * Math.pow(10, counter);
            counter++;
        } 
        reverseNumber = (isNegative ? -1 * reverseNumber: reverseNumber);
        return reverseNumber >= Math.pow(2,31) - 1 || reverseNumber <= -Math.pow(2,31)+1 ? 0 : reverseNumber;
    }
}