def partition(liste, start, end):
    pivot = liste[start]
    low = start + 1
    high = end
    while True:
        while low <= high and liste[high] >= pivot:
            high = high - 1
        while low <= high and liste[low] <= pivot:
            low = low + 1
        if low <= high:
            liste[low], liste[high] = liste[high], liste[low]
        else:
            break

    liste[start], liste[high] = liste[high], liste[start]
    return high
def quick_sort(liste, start, end):
    if start >= end:
        return
    p = partition(liste, start, end)
    quick_sort(liste, start, p-1)
    quick_sort(liste, p+1, end)
liste=[29,13,22,37,52,49,46,71,56]
quick_sort(liste, 0, len(liste) - 1)
print(liste)
