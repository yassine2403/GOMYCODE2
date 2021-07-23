def binary_search(arr,  x):
 
    
 
    mid = len(arr) // 2
    if arr[0]!=arr[-1]:
        if arr[mid] == x:
            print(True)
        elif arr[mid] > x:
            binary_search(arr[0:mid], x)
        else:
            binary_search(arr[mid+1:len(arr)], x)
    else:
        print(False)
sequence_a=[4,5,6,7,8,9,10,11,12]
binary_search(sequence_a,11)
