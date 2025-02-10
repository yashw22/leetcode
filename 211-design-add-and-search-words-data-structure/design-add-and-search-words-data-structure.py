class Node():
    def __init__(self):
        self.child = {}
        self.end = False
        self.prev = None

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        # curr = self.root
        # for c in word:
        #     if c not in curr.child:
        #         curr.child[c] = Node()
        #         curr.child[c].prev = curr
        #     curr = curr.child[c]
        
        # curr.end = True
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = Node()
                curr.child[ch].prev = curr
            curr = curr.child[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        
        # def rec(i, curr):
        #     if i==len(word):
        #         return curr.end

        #     c = word[i]
        #     if c!=".":
        #         if c not in curr.child:
        #             return False
        #         else:
        #             curr = curr.child[c]
        #             return rec(i+1, curr)
        #             curr = curr.prev
        #     else:
        #         for v in curr.child.values():
        #             curr = v
        #             if rec(i+1, curr):
        #                 return True
        #             curr = curr.prev
        #         return False

        # return rec(0, self.root)

        def rec(i, curr):
            if i==len(word):
                return curr.end

            ch = word[i]
            if ch!=".":
                if ch not in curr.child:
                    return False
                else:
                    return rec(i+1, curr.child[ch])
            else:
                for child in curr.child.values():
                    # curr = child
                    if rec(i+1, child):
                        return True
                    # curr = curr.prev
                return False


        return rec(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)