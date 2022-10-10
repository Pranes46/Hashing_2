class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        hashmap = {0:-1}  #creating a hasmap with a key 0 and value -1 to handle the case
        maxlength = 0    #initializing maxlength var
        rsum = 0        #to calculate the rsum
        
        for i in range(len(nums)):
            
                if nums[i] == 0:   #if the num is 0 we are subtracting the rsum by -1
                    rsum-=1
                else:             #if the num is 1we are subtracting the rsum by 1
                    rsum+=1
                
                if  rsum not in hashmap:  #if the rsum is not in the hasmap we are adding the num with its index as value
                    hashmap[rsum] = i
                    
                else:
                    maxlength = max (maxlength,i-hashmap[rsum])  #if the rsum is in hashmap we are finding the maxlength between previous maxlength and current index subracted by the previous value of the index
                    
        return maxlength  #returning the max length
            
        