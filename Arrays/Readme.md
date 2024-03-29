# ARRAY - LINEAR DATA STRUCTURE

- Array is a data structure used to store homogeneous elements at contiguous locations.
- Size of an array must be provided before storing data.

## Let size of array be n.

```
Accessing Time: O(1) [This is possible because elements
                      are stored at contiguous locations]

Search Time:   O(n) for Sequential Search
               O(log n) for Binary Search [If Array is sorted]

Insertion Time: O(n) [The worst case occurs when insertion
                     happens at the Beginning of an array and
                     requires shifting all of the elements]

Deletion Time: O(n) [The worst case occurs when deletion
                     happens at the Beginning of an array and
                     requires shifting all of the elements]
```

## Reverse Array

```
while start < end:
    swap(arr[start], arr[end])
    start += 1
    end -= 1
```

## Binary Search

```
left = 0
right =  len(arr) - 1

while (right >= left):

    ...

    mid =  left + (right-left)//2

    if arr[mid] ...

    ...

```
