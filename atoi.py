# basics_python
#module to use regx functions
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        match=re.match('[ ]*([+-]?\d+)', str)
        if match:
				#group returns the wanted part of the match
            num=int(match.group(1))
						#using the compresion
            return min(num, (2**31)-1) if num>=0 else max(num, -2**31)
        else:
            return 0
