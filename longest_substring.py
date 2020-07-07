# basics_python

#longest substring in the given string without repeating character

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        count=0
        q=[]
        for i in s:
            if i in q:
                maxi=max(maxi, count)
                x=q.index(i)
                for j in range(x+1):
                    q.pop(0)
                    count -=1
                q.append(i)
                count +=1
                
            else:
                q.append(i)
                count +=1
        maxi=max(maxi,count)
        return maxi
                
# this program takes 92ms and 13.8mb of memory
