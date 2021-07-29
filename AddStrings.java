/**
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
 */
class Solution {
    public static String addStrings(String num1, String num2) {
        int len = Math.max(num1.length(), num2.length());
        char[] val = new char[len];
        boolean carry = false;
        for(int i = 0; i < len; i++) {
            int temp = carry ? 1: 0;
            if(num1.length() > i) {
                temp += num1.charAt(num1.length() - 1 - i) - '0';
            }
            if(num2.length() > i) {
                temp +=  num2.charAt(num2.length() - 1 - i) - '0';
            }
            if(temp >= 10) {
                carry = true;
                temp = temp % 10;
            } else {
                carry = false;
            }

            val[len - 1 - i] = (char)(temp + '0');
        }
        return carry ? ("1" + new String(val)) : new String(val);
    }
}