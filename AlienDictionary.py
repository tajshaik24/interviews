'''
LeetCode 269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''
from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edges = defaultdict(set)
        degrees = defaultdict(int)
        for two_words in zip(words, words[1:]):
            for ch1, ch2 in zip(*two_words):
                if ch1 != ch2:
                    edges[ch1].add(ch2)
                    break
        for ch in edges.keys():
            for ch2 in edges[ch]:
                degrees[ch2] += 1

        charset = set(''.join(words))
        q = [ch for ch in charset if ch not in degrees]
        res = []
        while q:
            ch = q.pop(0)
            res.append(ch)
            for ch2 in edges[ch]:
                degrees[ch2] -= 1
                if degrees[ch2] == 0:
                    q.append(ch2)
        if all(map(lambda d: d==0, degrees.values())):
            return ''.join(res)
        return ''
