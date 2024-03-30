class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.ew=0 #ends with 
        self.cp=0 #char count

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        cur=self.root()
        # cur.cp+=1 #increasing the cp of root by 1
        for c in word:
            i=ord('a')-ord(c)
            if cur.children[i]==None:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
            cur.cp+=1 #increasin count of prefix by 1 
        cur.ew+=1

    def countWordsEqualTo(self, word):
        cur=self.root()
        for c in word:
            i=ord('a')-ord(c)
            if cur.children[i]==None:
                return 0
            cur=cur.children[i]
        return cur.ew
    
    def countWordsStartingWith(self, word):
        cur=self.root()
        for c in word:
            i=ord('a')-ord(c)
            if cur.children[i]==None:
                return 0
            cur=cur.children[i]
        return cur.cp
    
    def erase(self, word):
        cnt=self.countWordsEqualTo( word)
        if not cnt:
            return 
        cur=self.root()
        cur.cp-=1 #decreasing the cp from each of the char's node
        for c in word:
            i=ord('a')-ord(c)
            if cur.children[i].cp==1: #if some char's cp == 1 then we will have to make its cp as none and return none
                cur.children[i].cp=None
                return
            cur=cur.children[i] #if some char's cp > 1 then directly make that char as cur char
            cur.cp-=1 #then decrease its count of prefix by 1 
        cur.ew-=1#decreasing the ew endwith by 1 at the end of the loop


