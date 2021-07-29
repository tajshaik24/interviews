'''
LeetCode 745. Prefix and Suffix Search

Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.
'''
class WordFilter:
  # Add words to trie as the following: suffix#prefix
    def __init__(self, words: List[str]):
        self.trie = {}
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                cur_node = self.trie
                for char in word[j:] + '#' + word:
                    if not char in cur_node:
                        cur_node[char] = {}
                    cur_node = cur_node[char]
                cur_node["*"] = i

    # Do a search for suffix#prefix and see what words exist
    def f(self, prefix: str, suffix: str) -> int:
        cur_node, max_weight = self.trie, -1
        for char in suffix + '#' + prefix:
            if not char in cur_node:
                return -1
            cur_node = cur_node[char]
        stack = [cur_node]
        while stack:
            cur_node = stack.pop()
            if '*' in cur_node and cur_node['*'] > max_weight:
                max_weight = cur_node['*']
            for child in cur_node:
                if child != '*':
                    stack.append(cur_node[child])
        return max_weight

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
