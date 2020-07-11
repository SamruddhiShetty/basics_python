# basics_python

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        final=len(nums)-1
        while start<=final:
            mid=(start+final)//2
            if nums[mid]==target:
                return (mid)
            elif nums[mid]<nums[final]:
                if nums[mid]<=target<=nums[final]:
                    start=mid+1
                else:
                    final=mid-1
            else:
                if nums[start]<=target<=nums[mid]:
                    final=mid-1
                else:
                    start=mid+1
        return -1
            
            
        
