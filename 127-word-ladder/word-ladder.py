class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # adj = defaultdict(set)

        # def isNei(w1,w2):
        #     l = len(w1)
        #     ct = 0
        #     for i in range(l):
        #         if w1[i]==w2[i]:
        #             ct+=1
        #     return True if ct+1==l else False

        # for word1 in wordList + [beginWord]:
        #     for word2 in wordList+ [beginWord]:
        #         if word1!=word2 and isNei(word1, word2):
        #             adj[word1].add(word2)
        #             adj[word2].add(word1)

        # visited = set()
        # q = deque([endWord])

        # res = 1
        # while(q):
        #     n = len(q)
        #     res +=1
        #     for _ in range(n):
        #         node = q.popleft()
        #         visited.add(node)
        #         for nei in adj[node]:
        #             if nei==beginWord:
        #                 return res
        #             if nei not in visited:
        #                 q.append(nei)

        # return 0

        if endWord not in wordList:
            return 0

        wlen = len(beginWord)
        nei = defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for j in range(wlen):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            n = len(q)
            for _ in range(n):
                word = q.popleft()
                if word==endWord:
                    return res
                for j in range(wlen):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            q.append(neiWord)
                            visit.add(neiWord)

                
                
            res +=1
        return 0