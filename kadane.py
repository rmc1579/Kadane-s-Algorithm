#code
def Kadanes(arr):
    max_current = arr[0]
    max_global = arr[0]
    size =  (len(arr))
    
    
    for i in range(0, size):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global,max_current)
    return max_global

    
    
    
    
a = [-2, -3, 4, -1, -2, 1, 5, -3]
#a = [-2, 3, 2, -1]
print ("Maximum contiguous sum is : ", Kadanes(a))
