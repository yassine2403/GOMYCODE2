def merging(liste):
    if len(liste) > 1:
        mid = len(liste) // 2
        left = liste[:mid]
        right = liste[mid:]

        merging(left)
        merging(right)
        i = 0
        j = 0
        c = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              liste[c] = left[i]
              i += 1
            else:
                liste[c] = right[j]
                j += 1
            c += 1

        while i < len(left):
            liste[c] = left[i]
            i += 1
            c += 1

        while j < len(right):
            liste[c]=right[j]
            j += 1
            c += 1

liste = [29,13,22,37,52,49,46,71,56]
merging(liste)
print(liste)
