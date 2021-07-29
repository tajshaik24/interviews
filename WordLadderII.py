'''
LeetCode 126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
1) Only one letter can be changed at a time
2) Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
'''
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordSet = set(wordList)
        # Each queue is a level in the tree
        queue = set()
        queue.add(beginWord)
        # A dictionary that acts like a graph
        graphDict = defaultdict(list)
        graphDict[beginWord] = [[beginWord]]
        # A dictionary that hold different combinations of word
        baseDict = defaultdict(list)
        for word in wordList:
            for index in range(len(word)):
                randWord = word[:index] + "*" + word[index+1:]
                baseDict[randWord].append(word)
        # Go through each level of the tree
        while(queue):
            newQueue = set()
            newGraphDict = defaultdict(list)
            for word in queue:
                wordSet.discard(word)
                for index in range(len(word)):
                    randWord = word[:index] + "*" + word[index+1:]
                    listWords = baseDict[randWord]
                    for listWord in listWords:
                      # Make sure no duplicates or no repeated elements
                        if word != listWord and listWord in wordSet:
                            newQueue.add(listWord)
                            for path in graphDict[word]:
                                newGraphDict[listWord].append(path + [listWord])
            # Contains all the possible paths to endWord
            if endWord in newGraphDict:
                return newGraphDict[endWord]
            queue = newQueue
            graphDict = newGraphDict
        return []
