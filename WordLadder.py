'''
LeetCode 127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
* Only one letter can be changed at a time.
* Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
* Return 0 if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume beginWord and endWord are non-empty and are not the same.
'''
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        baseDict = defaultdict(list)
        for word in wordList:
            for index in range(len(word)):
                randWord = word[:index] + "*" + word[index+1:]
                baseDict[randWord].append(word)
        queue = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)
        while(len(queue) != 0):
            word, length = queue.pop(0)
            for index in range(len(word)):
                randWord = word[:index] + "*" + word[index+1:]
                listWords = baseDict[randWord]
                for listWord in listWords:
                    if listWord == endWord:
                        return length + 1
                    if listWord not in visited:
                        visited.add(listWord)
                        queue.append((listWord, length + 1))
                del baseDict[randWord]
        return 0
