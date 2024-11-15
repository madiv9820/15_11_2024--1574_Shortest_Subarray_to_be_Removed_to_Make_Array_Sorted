#include <iostream>
#include <vector>
using namespace std;

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

int main() {
    int input; vector<int> arr; Solution sol;
    cin >> input;

    while(input != -1) {
        arr.push_back(input);
        cin >> input;
    }

    cout << sol.findLengthOfShortestSubarray(arr) << endl;
}