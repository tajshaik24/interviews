'''
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''
from collections import defaultdict
class WordDistance:
    def __init__(self, words: List[str]):
        self.wordIndex = defaultdict(list)
        for index,word in enumerate(words):
             self.wordIndex[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        indexWord1 = self.wordIndex[word1]
        indexWord2 = self.wordIndex[word2]
        minDistance = float("inf")
        for index in indexWord1:
            for index2 in indexWord2:
                distance = abs(index2 - index)
                if distance < minDistance:
                    minDistance = distance
        return minDistance



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
