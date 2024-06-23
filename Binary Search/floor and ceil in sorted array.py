# Floor of X is the largest element which is smaller than or equal to X. 
# Ceil of X is the smallest element which is greater than or equal to X

def findFloorAndCeiling(a, n, x):
    low = 0
    high = n - 1
    floor_value = -1
    ceiling_value = -1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == x:
            return (a[mid], a[mid])  # If x is found, it's both the floor and ceiling
        elif a[mid] < x:
            floor_value = a[mid]
            low = mid + 1
        else:
            ceiling_value = a[mid]
            high = mid - 1

    return (floor_value if floor_value != -1 else -1, ceiling_value if ceiling_value != -1 else -1)

n = 6
x = 5
a = [3, 4, 4, 7, 8, 10]

floor_value, ceiling_value = findFloorAndCeiling(a, n, x)

print(f"Floor of {x} is: {floor_value}")
print(f"Ceiling of {x} is: {ceiling_value}")
