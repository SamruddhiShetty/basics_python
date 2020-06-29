# basics_python

#problem is to find two numbers 'a' and 'b' in the given array(here-'nums') which adds up to be equal to the target, return the list of the index of a and b.



def two_sum(nums, target):
    find={} #this is a dictionary ,using hash table with one pass
    
    # the value is the key and the index is the value in the dictionary
    
    for index, value in enumerate(nums):
        x=target-value
        if x in find:
            return(index, find[x])
        else:
            find[value]=index
