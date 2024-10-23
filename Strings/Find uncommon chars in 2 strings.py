# https://www.geeksforgeeks.org/find-uncommon-characters-two-strings/

def find_uncommon_chars(str1: str, str2: str) -> list:
    # Create a dictionary to store the frequency of each character
    char_count = {}
    
    # Count characters in the first string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Count characters in the second string
    for char in str2:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find characters that appear only once (uncommon)
    uncommon_chars = [char for char, count in char_count.items() if count == 1]
    
    return uncommon_chars

# Example usage:
str1 = "abcde"
str2 = "bcfgh"
result = find_uncommon_chars(str1, str2)
print(result)  # Output: ['a', 'd', 'e', 'f', 'g', 'h']


# Use a hash table of size 26 for all the lowercase characters.
# Initially, mark presence of each character as ‘0’ (denoting that the character is not present in both 
#the strings).
# Traverse the 1st string and mark presence of each character of 1st string as ‘1’ (denoting 1st string) 
#in the hash table.
# Now, traverse the 2nd string. For each character of 2nd string, check whether its presence in the hash
#  table is ‘1’ or not. If it is ‘1’, then mark its presence as ‘-1’ (denoting that the character is 
# common to both the strings), else mark its presence as ‘2’ (denoting 2nd string).
s=''
max_char=26
def find_uncommon(s1,s2):
    present=[0]*max_char
    for i in range(0,max_char):
        present[i]=0
    
    for i in range(len(s1)):
        present[ord(s1[i])-ord('a')]=1 #making the l1's all chars value==1 in present 
    
    for i in range(len(s2)):
        if present[ord(s2[i])-ord('a')]==1 or present[ord(s2[i])-ord('a')]==-1 :
            present[ord(s2[i])-ord('a')]=-1
        else:
            present[ord(s2[i])-ord('a')]=2
    
    for i in range(max_char):
        if present[i]==1 or present[i]==2:
            s.add(i)
    return s

    

