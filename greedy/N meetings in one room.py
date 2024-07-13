# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

#Here we need to maximize the number of meetings so we can go in any order
#that satisfies the condition of max meetings
# we might need to return the order of the maximum number of meetings

#So we need to find those meetings that are ending faster
#On the basis of sorted ending value so make a data structure to store 
#start,ending,position 

#To make the meeting possible:- Ending of the initial meeting should be 
# smaller than the start of the current meeting

from typing import List, Tuple

class Solution:
    def maxMeetings(self, start: List[int], end: List[int]) -> List[int]:
        # Create a list of tuples where each tuple contains (start, end, position)
        meetings = [(start[i], end[i], i + 1) for i in range(len(start))]
        
        # Sort the meetings based on the end time
        meetings.sort(key=lambda x: x[1])
        
        # List to store the order of the maximum number of meetings
        selected_meetings = []
        
        # The end time of the last selected meeting
        last_end_time = 0
        
        for meeting in meetings:
            if meeting[0] > last_end_time:  # If the current meeting starts after the last meeting ends
                selected_meetings.append(meeting[2])  # Add the meeting's position to the result
                last_end_time = meeting[1]  # Update the end time of the last selected meeting
        
        return selected_meetings

# Example usage:
solution = Solution()
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
print(solution.maxMeetings(start_times, end_times))  # Output should be [1, 2, 4, 5]

