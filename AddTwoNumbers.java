/*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }
        else if(l2 == null){
            return l1;
        }
        return addTwoNumbersHelper(l1, l2, null, false);
    }
    private ListNode addTwoNumbersHelper(ListNode l1, ListNode l2, ListNode product, boolean carryOne){
        if(l1 == null && l2 == null){
            if(carryOne){
                return new ListNode(1);
            }
            return null;
        }
        if(l1 == null){
            if(carryOne){
                product = new ListNode((l2.val + 1) % 10);
                if((l2.val + 1) > 9){
                    carryOne = true;
                }
                else{
                    carryOne = false;
                }
            }
            else{
                product = new ListNode(l2.val);
            }
            ListNode nextVal = addTwoNumbersHelper(null, l2.next, product.next, carryOne);
            if(nextVal != null){
                product.next = nextVal;
            }
            return product;
        }
        else if(l2 == null){
            if(carryOne){
                product = new ListNode((l1.val + 1) % 10);
                if((l1.val + 1) > 9){
                    carryOne = true;
                }
                else{
                    carryOne = false;
                }
            }
            else{
                product = new ListNode(l1.val);
            }
            ListNode nextVal = addTwoNumbersHelper(l1.next, null, product.next, carryOne);
            if(nextVal != null){
                product.next = nextVal;
            }
            return product;
        }
        if(carryOne){
            product = new ListNode((l1.val + l2.val + 1) % 10);
            if((l1.val + l2.val + 1) > 9){
                carryOne = true;
            }
            else{
                carryOne = false;
            }
        }
        else{
            product = new ListNode((l1.val + l2.val) % 10);
            if((l1.val + l2.val) > 9){
                carryOne = true;
            }
            else{
                carryOne = false;
            }
        }
        ListNode nextVal = addTwoNumbersHelper(l1.next, l2.next, product.next, carryOne);
        if(nextVal != null){
                product.next = nextVal;
        }
        return product;
    }
}