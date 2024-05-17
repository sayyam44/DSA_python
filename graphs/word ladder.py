# https://leetcode.com/problems/word-ladder/

#Since we need to find the shortest path bw the start word and the endword that is why 
#we will implement it using BFS approach
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #1st of all find the all possible patterns of a word and then make a list that matches this patterns .
        #eg- hot=*ot,h*t,ho*
        #{*ot:[hot,dot,lot]}
        #{h*t:[hot,hit]} etc
        #therefore for hot we get [dot,lot,hit]
        #by moving chars 1by1 for each element we doing it for n words and then going through each single
        #  char that we removed i.e. m ====n*m(possible number of patterns that we have in total) then 
        # adding each word to the list will take another m time ,tc=n*m2 by adjacency list 
        
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word) #{*ot:{hot,dot,lot}}
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0