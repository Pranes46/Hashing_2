class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        hashset = set()  # we are initializing the hashset to store the str
        
        count = 0 #to store the occurences
        
        for ch in s:  #we are iterating all the str
            if ch not in hashset:  #if the str is not present in the hashset we are adding it to the hashset
                hashset.add(ch)
            else:      # if the str is present in the hashset the above if condition will fail and we are removing the str from hashset and we are adding 2 with the counter 
                hashset.remove(ch)
                count+=2
        if len(hashset)!=0:  #after the loop is completed we are checking whether the hashset is empty or not, if it is not empty there is some odd num string is present in the hashset i.e 1. so we are adding 1 with the counter
                count+=1
                
        return count
        