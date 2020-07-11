# basics_python
#takes 160ms
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                c.append(nums1[i])
                i +=1
            else:
                c.append(nums2[j])
                j+=1
        while j<len(nums2) and i==len(nums1):
            c.append(nums2[j])
            j +=1
            
        while i<len(nums1) and j==len(nums2):
            c.append(nums1[i])
            i+=1
            
        if len(c)%2!=0:
            return c[len(c)//2]
        else:
            return (c[len(c)//2] + c[(len(c)//2)-1]) /2
            
 #takes 100ms
 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2=nums2, nums1
        m=len(nums1)
        n=len(nums2)
        if n==0:
            raise ValueError
        start=0
        finish=m
        while(start<=finish):
            i=(start+finish)//2
            j=((n+m+1)//2)-i
            if i>0 and nums1[i-1]>nums2[j]:
                finish=i-1
            elif i<m and nums2[j-1]>nums1[i]:
                start=i+1
            else:
                if i==0: max_of_left=nums2[j-1]
                elif j==0: max_of_left=nums1[i-1]
                else:
                    max_of_left=max(nums1[i-1], nums2[j-1])
                if (m+n)%2!=0:
                    return (max_of_left)
                if i==m: min_of_right=nums2[j]
                elif j==n: min_of_right=nums1[i]
                else:
                    min_of_right=min(nums1[i], nums2[j])
                return (max_of_left + min_of_right)/2.0
                        

