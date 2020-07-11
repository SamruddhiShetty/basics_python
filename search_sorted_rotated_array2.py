# basics_python
#when duplicates are present that is the array is arranged in non-decreasing order
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start=0
        final=len(nums)-1
        while start<=final:
            mid=(start+final)//2
            if nums[mid]==target:
                return True
            elif nums[start]==nums[mid]==nums[final]:
                start=start+1
                final=final-1
            elif nums[mid]<=nums[final]:
                if nums[mid]<target and target<=nums[final]:
                    start=mid+1
                else:
                    final=mid-1
            else:
                if nums[start]<=target and target<nums[mid]:
                    final=mid-1
                else:
                    start=mid+1
        return False
        
