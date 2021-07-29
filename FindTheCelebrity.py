'''
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.


Example 1:
Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.
'''
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        to_check = set(range(n))
        self.rFindCel(0, n, to_check)
        if len(to_check) != 1:
            return -1
        celebrity = list(to_check)[0]
        for i in range(n):
            if i != celebrity:
                if not knows(i, celebrity) or knows(celebrity, i):
                    return -1
        return int(celebrity)

    def rFindCel(self, idx, stop, the_set):
        set_list = list(the_set)
        i = set_list[0]
        for j in range(1, len(set_list)):
            if knows(i, set_list[j]):
                the_set.remove(i)
                break
            the_set.remove(set_list[j])
        if idx + 1 < stop: self.rFindCel(idx + 1, stop, the_set)
