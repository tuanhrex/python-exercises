def twosum(arr,val):
    array = []
    for i in arr:
        
        for j in arr:
            if i + j == val and i != j:
                array.append(arr.index(i))
    return array
    

    

print(twosum([11, 2, 7, 15], 9))