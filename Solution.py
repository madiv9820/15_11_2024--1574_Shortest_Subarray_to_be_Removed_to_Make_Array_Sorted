from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Initialize the length of the array
        n = len(arr)
        
        # Two pointers: 'left' will point to the first position where the array stops being non-decreasing
        # 'right' will point to the last position where the array stops being non-decreasing
        left, right = 0, n - 1

        # Move the 'left' pointer to the right as long as arr[left] is less than or equal to arr[left + 1]
        # This will find the longest non-decreasing prefix of the array
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        
        # If 'left' has reached the end of the array, the array is already sorted
        if left == n - 1: 
            return 0
        
        # Move the 'right' pointer to the left as long as arr[right] is greater than or equal to arr[right - 1]
        # This will find the longest non-decreasing suffix of the array
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        # The result is the minimum length of subarrays that need to be removed to make the array non-decreasing
        # The first candidate is the subarray from arr[left+1] to arr[n-1] (length n - left - 1)
        # The second candidate is the subarray from arr[0] to arr[right-1] (length right)
        result = min(n - left - 1, right)
        
        # Two pointers approach: trying to merge the non-decreasing prefix (arr[0] to arr[left]) with the non-decreasing suffix (arr[right] to arr[n-1])
        ptr1, ptr2 = 0, right

        # Traverse both the prefix and suffix and try to find a valid non-decreasing array by removing a subarray
        while ptr1 <= left and ptr2 < n:
            # If arr[ptr1] <= arr[ptr2], then the subarray from ptr1 to ptr2 can be removed
            # and the remaining array will be non-decreasing
            if arr[ptr1] <= arr[ptr2]:
                result = min(result, ptr2 - ptr1 - 1)
                ptr1 += 1  # Move 'ptr1' forward to explore the next element in the prefix
            else:
                ptr2 += 1  # Move 'ptr2' forward to explore the next element in the suffix
        
        # Return the minimum length of the subarray to remove to make the array sorted
        return result