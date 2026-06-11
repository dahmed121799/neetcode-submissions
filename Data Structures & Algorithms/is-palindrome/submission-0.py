class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for letter in s:
            if letter.isalnum():
                arr.append(letter.lower())
        
        for i in range(len(arr)):
            if arr[i] != arr[len(arr)- 1 - i]:
                return False
        return True

            
        