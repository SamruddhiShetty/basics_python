#given a number and rerturn the roman format of the same

def intToRoman(num) -> str:
        r1=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        r2=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value, i= "", 0
        
        while num!=0:
            if r1[i]<=num:
                num-=r1[i]
                value=value+r2[i]
            else:
                i+=1
                
                
        return(value)
