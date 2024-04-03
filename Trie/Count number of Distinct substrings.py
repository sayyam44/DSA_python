#eg-abab=a,ab,aba,abab,b,ba,bab=7+1=8 distinct substrings (1 is added as given in the ques that we need to add an empty subrting at last)
#brute force method

#TC= n*3logn
# sc=n
def distinct_sub(word):
    st=set()
    for i in (len(word)+1): #-------------> tc=n
        for j in range(i+1,len(word)+1):#-------------> tc=n
            st.add(str[i:j]) #-------------> tc=log m where m is the number of the elements in set
    print(len(st))

if __name__ == '__main__':
    str = "aaaa"
    print(distinct_sub(str));
 #TC in above case=n2*logm
 #SC in above case=n3


#Optimized method USING TRIE
#TC=N2

class TrieNode:
    def __init__(self):
        self.children=[None]*26

class Trie:
    def __init__(self):
        self.root=TrieNode()
    def solve(self,word):
        cnt=0 #it will count the number of substrings
        
        for i in range(len(word)):
            cur=self.root #cur is always pointing towards the root whenever the new word begins
            for j in range(i,len(word)):
                if word[j] not in cur.children: #if the new char is not in cur's children 
                    cur.children[word[i]]=TrieNode() #then add that char and its trienode
                    cnt+=1 #and increase the cnt of distinct words by one
                cur=cur.children[word[j]] #if the char is present in the cur.children 
                                          #then cur will move directly to the node where that char is present 
                                          #basically it will happen at the root node everytime

def count_distinct(word):
    trie=Trie()
    return trie.solve(word)


        