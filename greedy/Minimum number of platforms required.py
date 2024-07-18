# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

#Brute Force Approach (tc=n2)
#go through all the arrival time and departure time pairs and find the total
#number of intersections for each pair and then find the max of all 

#4 cases of intersection for a train
#arrival before and departing after 
#arr before and departing middle
#arrival after and departing after 
#arrival and departing middle

def platforms(arr, dep):
    max_count = 0

    # Iterate through each train's arrival and departure times
    for i in range(len(arr)):
        cnt = 1  # Initialize the count for the current train

        # Check against all other trains
        for j in range(i + 1, len(arr)):
            # Check if there is an intersection based on the conditions provided
            if ((arr[i] > arr[j] and dep[i] < dep[j]) or 
                (arr[i] > arr[j] and arr[i] < dep[j] < dep[i]) or
                (arr[i] < arr[j] < dep[i] and dep[j] > dep[i]) or
                (arr[i] < arr[j] and dep[i] > dep[j])):
                cnt += 1
        
        # Update the maximum count if the current count is greater
        max_count = max(max_count, cnt)

    return max_count

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(platforms(arr, dep))  


#Optimized solution (tc=2n)
# In this ques we dont need which trains are possible we just need the 
# minimum count of the platforms needed to receive all trains
#so we can sort arrival array as well as departure array seperately
#Take 2 pointers and check which pointer time is possible arrival or departure
#If arrival time is possible then increase the count and if departure is
#possible then recude the count

def platforms(arr, dep):
    arr.sort()
    dep.sort()
    
    i, j = 0, 0
    cnt = 0
    max_cnt = 0
    
    while i < len(arr) and j < len(dep):
        if arr[i] < dep[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(platforms(arr, dep)) 
