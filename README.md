# Shortest Subarray to be Removed to Make Array Sorted Using Two Pointers

- ### Problem Intuition
    Given an array, we are asked to remove the shortest subarray so that the remaining array becomes sorted in non-decreasing order. The main challenge is finding the shortest subarray efficiently, without having to check every possible subarray.

- ### Key Observations:
    1. **Non-decreasing Subarrays**: 
        - The array is already sorted in non-decreasing order in the beginning or at the end.
        - We need to identify the longest non-decreasing prefix and suffix of the array. 
    2. **Two Main Scenarios**:
        - The entire array is already non-decreasing: no subarray needs to be removed.
        - A subarray in the middle needs to be removed to make the array sorted.

- ### Intuition:
    To solve this efficiently:
    1. **Identify the longest non-decreasing prefix**: Traverse from the left and find the largest segment that is already sorted.
    2. **Identify the longest non-decreasing suffix**: Traverse from the right and find the largest segment that is already sorted.
    3. **Try to merge the prefix and suffix**: If there's any overlap where the last element of the prefix is less than or equal to the first element of the suffix, then you can remove a subarray between them. This minimizes the number of elements to remove.
    4. **Optimal subarray removal**: The result is the shortest subarray that can be removed, either from the beginning, the end, or the middle.

- ### Approach
    1. **Find the longest non-decreasing prefix**:
        - Traverse the array from the left to right until we find an element that is smaller than the previous one. This gives us the longest non-decreasing prefix.   
    2. **Find the longest non-decreasing suffix**:
        - Traverse the array from the right to left until we find an element that is larger than the next one. This gives us the longest non-decreasing suffix.
    3. **Merge the prefix and suffix**:
        - Now that we have the longest non-decreasing prefix (`left`) and suffix (`right`), try to find the shortest subarray that can be removed. We can try merging the two segments, checking whether the prefix’s end can be followed by the suffix’s start.
    4. **Final Answer**:
        - If the entire array is non-decreasing from the start, return `0`.
        - Otherwise, compute the minimum length of subarrays to be removed.

- ### Code
    - **Python Solution**

        ```python3 []
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
        ```
    
    - **C++ Solution**

        ```cpp []
        class Solution {
        public:
            int findLengthOfShortestSubarray(vector<int>& arr) {
                // Initialize the length of the array
                int n = arr.size();

                // Two pointers: 'left' will point to the first position where the array stops being non-decreasing
                // 'right' will point to the last position where the array stops being non-decreasing
                int left = 0, right = n-1;

                // Move the 'left' pointer to the right as long as arr[left] is less than or equal to arr[left + 1]
                // This will find the longest non-decreasing prefix of the array
                while(left < n-1 && arr[left] <= arr[left+1])
                    ++left;
                
                // If 'left' has reached the end of the array, the array is already sorted
                if(left == n-1) 
                    return 0;

                // Move the 'right' pointer to the left as long as arr[right] is greater than or equal to arr[right - 1]
                // This will find the longest non-decreasing suffix of the array
                while(right > 0 && arr[right] >= arr[right-1])
                    --right;
                
                // The result is the minimum length of subarrays that need to be removed to make the array non-decreasing
                // The first candidate is the subarray from arr[left+1] to arr[n-1] (length n - left - 1)
                // The second candidate is the subarray from arr[0] to arr[right-1] (length right)
                int result = min(n-left-1, right);
                
                // Two pointers approach: trying to merge the non-decreasing prefix (arr[0] to arr[left]) with the non-decreasing suffix (arr[right] to arr[n-1])
                int ptr1 = 0, ptr2 = right;

                // Traverse both the prefix and suffix and try to find a valid non-decreasing array by removing a subarray
                while(ptr1 <= left && ptr2 < n) {
                    // If arr[ptr1] <= arr[ptr2], then the subarray from ptr1 to ptr2 can be removed
                    // and the remaining array will be non-decreasing
                    if(arr[ptr1] <= arr[ptr2]) {
                        result = min(result, ptr2-ptr1-1);
                        ++ptr1; // Move 'ptr1' forward to explore the next element in the prefix
                    }
                    else {
                        ++ptr2; // Move 'ptr2' forward to explore the next element in the suffix
                    }
                }
                
                // Return the minimum length of the subarray to remove to make the array sorted
                return result;
            }
        };
        ```

- ### Time Complexity
    - **Prefix and suffix computation**: 
        - Finding the longest non-decreasing prefix takes `O(n)`, as we traverse the array once from the left.
        - Finding the longest non-decreasing suffix also takes `O(n)`, as we traverse the array once from the right.
    
    - **Merging the two segments**:
        - We use two pointers to merge the non-decreasing prefix and suffix, which also takes `O(n)`.

    Thus, the overall time complexity is **O(n)**, where `n` is the length of the array.

- ### Space Complexity
    - The algorithm uses a constant amount of extra space, as we only need a few pointers and variables to keep track of the result.
    - No additional data structures (like arrays or hashmaps) are used.

    Thus, the space complexity is **O(1)**.