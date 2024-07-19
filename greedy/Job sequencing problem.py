# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

# example - here deadline of 4 days means that task can be completed in 
# any of the 1st 4 days either1 or 2 or 3 or 4th day.
#single job can be completed in single day 

# Delay the jobs to end days
# Better to perform maximum profit tasks

#Sort on the basis of profit
#Since we have to delay the jobs to the end days so find the maximum day
# and make an array of maximum_day+1 with all -1 and update with id
#if that day does not have -1 then check if the previous index have -1
#then update it 

#tc=nlogn+n*maxdeadline

def job_seq(jobs, N):
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True) #reverse because we want in ascending order

    # Find the maximum deadline to create the jobs_done array
    max_deadline = max(job[1] for job in jobs)

    # Initialize the jobs_done array with -1
    jobs_done = [-1] * (max_deadline + 1)
    total_profit = 0

    # Iterate through each job
    for job in jobs:
        # Find a slot for the job, starting from its deadline and moving backwards
        for i in range(job[1], 0, -1):
            if jobs_done[i] == -1:
                jobs_done[i] = job[0]
                total_profit += job[2]
                break

    return jobs_done, total_profit

# Example usage
jobs = [(1, 4, 20), (2, 1, 10), (3, 2, 40), (4, 2, 30)]
N = len(jobs)
jobs_done, total_profit = job_seq(jobs, N)
print(f"Jobs done: {jobs_done}")  # Jobs done: [-1, 2, 4, 3, 1]
print(f"Total profit: {total_profit}")  # Total profit: 100








