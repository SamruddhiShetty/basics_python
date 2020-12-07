class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pbook={'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        ans=[]
        if not digits:
            return ans
        ans=[""]
        for c in digits:
            ans=[i+j for i in ans for j in pbook[c]]
            
        return ans
        
        
  #input:- digits=[2,3]
  #output:- ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
