# https://www.codingninjas.com/codestudio/problem-details/ninja-s-training_3621003
#updated
#Recursive Solution 
def f(day,last,points): #(tc=n*n)
    if day==0:
        maxi=0
        for task in range(3):
            if task!= last:
                maxi=max(maxi,points[0][task])
        return maxi 
    maxi=0
    for task in range(3):
        if task!=last:
            # points[day][task] means points of that current day according to
            # previous task 
            point=points[day][task]+f(day-1,task,points)
            maxi=max(maxi,point)
    return maxi

def ninjaTraining(n,points):
    return f(n-1,3,points)

#Memoization (tc=(n*4)*3) 3 because for loop is running for range(3) in code , sc= n(recursion stack space)+(n*4)

def f(day,last,points,dp):
    if day==0:
        maxi=0
        for task in range(3):
            if task!= last:
                maxi=max(maxi,points[0][task])
        return maxi 
    if dp[day][last]!=-1: #step3
        return dp[day][last]
    maxi=0
    for task in range(3):
        if task!=last:
            point=points[day][task]+f(day-1,task,points,dp)
            maxi=max(maxi,point)
    return dp[day][last]==maxi #step2

def ninjaTraining(n,points):
    dp = [[-1 for i in range(4)] for j in range(4)] #declaring the dp array of n*4 
    return f(n-1,3,points,dp)


#Tabulation (tc=(n*4)*3) (same as memoization), sc=n*4(just recursion stack space is not used))

def ninjaTraining(n,points):
    dp = [[-1 for i in range(4)] for j in range(4)] #declaring the dp array of n*4 
    dp[0] = max(points[0][1], points[0][2])
    dp[1] = max(points[0][0], points[0][2])
    dp[2] = max(points[0][0], points[0][1])
    dp[3] = max(points[0][0], max(points[0][1], points[0][2]))

    for day in range(1,n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3): 
                if (task != last):
                    point=points[day][task]+dp[day-1][task]
                    dp[day][last] = max(dp[day][last], points)
    
    return dp[n-1][3]

