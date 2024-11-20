#updated
class Solution:
    def sorted(self, s):
        # Code here
        stk=[]
        while s :
            tmp=s.pop() 
            
            while stk and stk[-1]>tmp: #we have to push min value into stk
                tmp2=stk.pop()
                s.push(tmp2)
                # stk.pop[-1]
            stk.push(tmp)
        return stk


#recursive method 
#tc=n2,sc=n

def sortedInsert(element,s):
    if len(s)==0 or element > s[-1]: #here also we are doing the same as above just here the stk=s 
        #case 1 - len=0 so s=[9],2nd case element=23 i.e > s[-1] i.e 9 so 
        # new s=[9,23]
        s.append(element)
        return 
    else: # 3rd case will fall here 
        temp=s.pop() # temp=23 #remove topmost element
        sortedInsert(element,s) # this will return s=[9,10] #again call same function after removing 
        s.append(temp) #s=[9,10,23] #now append the removed value


def sortStack(s): #let s=[9,23,10]
    temp=s.pop()  
    sortStack(s) #putting all vals in temp and making s empty 
    sortedInsert(temp,s) #for 1st case s is empty ,temp=9 , 2nd case - temp=23, s=[9],case 3- temp=10,s=[9,23]



