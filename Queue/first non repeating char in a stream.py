# Input: A = "aabc"
# Output: "a#bb"
# Explanation: For every character first non
# repeating character is as follow-
# "a" - first non-repeating character is 'a'
# "aa" - no non-repeating character so '#'
# "aab" - first non-repeating character is 'b'
# "aabc" - first non-repeating character is 'b'

#push the element from the input string into queue and increase the value of its char count accordingly
#then in the while loop we will check the char count of front element if its greater than 1 
#then pop the front element else print the front element
# #tc=n

from queue import Queue

def first_non_repeat(str):
    q = Queue()
    charCount = [0] * 26

    for i in range(len(str)):
        q.put(str[i]) #appending the element into queue from rear end
        charCount[ord(str[i])-ord('a')]+=1 #increasing the count of str[i] in charcount by 1

        while (q):
            if charCount[ord(q.queue[0])-ord('a')]>1: #if front(top)element of queue is greater than 1 then 
                q.get() #then pop that element from queue
            else: #if the count ==1
                print(q.queue[0],end=" ")
                break
        if (q.empty()):
            print(-1, end = " ")
    print()

Str = "aabc"
first_non_repeat(Str) 