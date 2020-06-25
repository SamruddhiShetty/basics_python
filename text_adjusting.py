# basics_python
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print(' '.rjust((thickness-1)//2)+(c*thickness).ljust(thickness*3)+(c*thickness).rjust(thickness*2))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print(' '.rjust((thickness-1)//2)+(c*thickness).ljust(thickness*2)+(c*thickness).rjust(thickness*3))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    
    
    
    i/p :-- 7
    
      H      
     HHH     
    HHHHH    
   HHHHHHH   
  HHHHHHHHH  
 HHHHHHHHHHH 
HHHHHHHHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
   HHHHHHH                     HHHHHHH
                            HHHHHHHHHHHHH 
                             HHHHHHHHHHH  
                              HHHHHHHHH   
                               HHHHHHH    
                                HHHHH     
                                 HHH      
                                  H       
​
    
    
    
