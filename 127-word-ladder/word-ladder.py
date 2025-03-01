class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord not in wordList:
        #     return 0

        # wlen = len(beginWord)
        # nei = defaultdict(list)

        # wordList.append(beginWord)
        # for word in wordList:
        #     for j in range(wlen):
        #         pattern = word[:j] + "*" + word[j+1:]
        #         nei[pattern].append(word)

        # visit = set([beginWord])
        # q = deque([beginWord])
        # res = 1

        # while q:
        #     n = len(q)
        #     for _ in range(n):
        #         word = q.popleft()
        #         if word==endWord:
        #             return res
        #         for j in range(wlen):
        #             pattern = word[:j] + "*" + word[j+1:]
        #             for neiWord in nei[pattern]:
        #                 if neiWord not in visit:
        #                     q.append(neiWord)
        #                     visit.add(neiWord)

                
                
        #     res +=1
        # return 0

        if endWord not in wordList:
            return 0

        wl = len(beginWord)
        nei = defaultdict(list)

        wordList.append(beginWord)
        for wrd in wordList:
            for i in range(wl):
                pattern = wrd[:i]+"*"+wrd[i+1:]
                nei[pattern].append(wrd)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            ql = len(q)
            for _ in range(ql):
                wrd = q.popleft()
                if wrd==endWord:
                    return res
                for i in range(wl):
                    pattern = wrd[:i]+'*'+wrd[i+1:]
                    for neiWrd in nei[pattern]:
                        if neiWrd not in visit:
                            q.append(neiWrd)
                            visit.add(neiWrd)
            res+=1

        return 0