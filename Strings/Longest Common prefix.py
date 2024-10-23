# https://leetcode.com/problems/longest-common-prefix/
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
def lng(strs):
    # min(strs)->gives lexicographical min among all strs
    #max(strs)->gives lexicographical max among all strs
    # strs = ["abc", "a", "df"]
    # (min(strs))  # Output: "a"
    # (max(strs))  # Output: "df"
    m,M=min(strs),max(strs)
    for i,ch in enumerate(m):
        if ch!=M[i]:
            return m[:i]
    return m #if all the chars of m and M matches then m will be the maximum they will match