def bubbleSort(liste):
    for j in range(len(liste)-1,0,-1):
        for i in range(j):
            if liste[i]>liste[i+1]:
                a = liste[i]
                liste[i] = liste[i+1]
                liste[i+1] = a
    return liste
print(bubbleSort([29,13,22,37,52,49,46,71,56]))
