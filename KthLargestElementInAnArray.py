'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
import random
class Solution:
    def findKthLargest(self, arr, k):
        n = len(arr)
        l, r = 0, n-1
        while l <= r:
            p = partition(arr, l, r)
            if p == n-k:
                return arr[p]
            elif p < n-k:
                l = p+1
            else:
                r = p-1
        return -1
    
def partition(arr, l, r):
        rx = random.randint(l,r)
        arr[l], arr[rx] = arr[rx],arr[l]
        i, j = l + 1, l
        while i <= r:
            if arr[i] < arr[l]:
                arr[j + 1], arr[i] = arr[i], arr[j + 1]
                j += 1
            i += 1
        arr[j],arr[l] = arr[l],arr[j]
        return j