'''
LeetCode 332. Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"]. All airports are represented by three capital letters (IATA code). You may assume all tickets form at least one valid itinerary.
'''
class Solution(object):
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for x,y in tickets:
            graph[x].append(y)

        L = len(tickets)
        res = ["JFK"]
        def dfs(port):
            if len(res) == L + 1:
                return True
            for nex in sorted(graph[port]):
                graph[port].remove(nex)
                res.append(nex)
                if dfs(nex):
                    return True
                else:
                    graph[port].append(nex)
                    res.pop()
            return False

        dfs("JFK")
        return res
