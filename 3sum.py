# basics_python
#find the value of a, b, c in the given array such that they add up to give value equal to the given target(here 0) return the list of lists wherein each list 
#contains the value of set a, b, c .


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        
        for i,value in enumerate(nums):
            if i>0 and  value == nums[i-1]:     #this is used to prevent the appearance of two similar lists due to the presence of duplicate values 
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if value+nums[l]+nums[r] > 0:
                    r -=1
                elif value+nums[l]+nums[r] < 0: 
                    l +=1
                else:
                    result.append([value, nums[l], nums[r]])
                    l +=1
                    while l<r and nums[l]==nums[l-1]:      #this is also used top prevent duplicate values , each of these eliminates the one escaped from each other
                        l +=1
                        
        return(result)
        
