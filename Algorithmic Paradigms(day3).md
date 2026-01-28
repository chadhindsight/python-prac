# Algorithmic Paradigms - Simple Guide

## 1. Divide and Conquer
**What it is:** Break problem into smaller pieces, solve each piece, combine results.

### Merge Sort
**Time:** O(n log n), **Space:** O(n)
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
**LeetCode:** #148 Sort List

### Quick Sort
**Time:** O(n log n) average, **Space:** O(log n)
```python
def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
    
    return arr

def partition(arr, start, end):
    pivot = arr[start]
    swap_idx = start
    # range() is exclusive of the end value so we need +1 to include the end value
    for i in range(start + 1, end + 1):
        if pivot > arr[i]:
            swap_idx += 1
            arr[swap_idx], arr[i] = arr[i], arr[swap_idx]
    
    arr[start], arr[swap_idx] = arr[swap_idx], arr[start]
    return swap_idx
```
**LeetCode:** #215 Kth Largest Element

## 2. Greedy
**What it is:** Pick what looks best right now.

### Coin Change (US coins only)
**Time:** O(1)
```python
def lemonadeChange(bills):
    five = ten = 0  # counts of $5 and $10 bills

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # when bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True

```
**LeetCode:** #860 Lemonade Change

### Activity Selection
**Time:** O(n log n)
```python
def max_activities(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    count = 1
    last_end = activities[0][1]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= last_end:
            count += 1
            last_end = activities[i][1]
    
    return count
```
**LeetCode:** #435 Non-overlapping Intervals

## 3. Sliding Window
**What it is:** Move a window through array/string.

**Time:** O(n), **Space:** O(1)
```python
# Fixed size window
def max_sum_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Variable size window
def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```
**LeetCode:** #3 Longest Substring Without Repeating Characters

## 4. Two Pointers
**What it is:** Use two pointers moving through data.

**Time:** O(n), **Space:** O(1)
```python
# Opposite ends
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

# Same direction
def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1
```
**LeetCode:** #167 Two Sum II