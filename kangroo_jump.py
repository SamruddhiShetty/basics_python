# basics_python

#they should land at the same position at the same time , they should have same number of jumps
#always x2>x1 that is the position of the second kangroo is always greater than the first one

def kangaroo(x1, v1, x2, v2):
    if v2>=v1:
        return "NO"
    else:
        if (x2-x1)%(v1-v2)==0:
            return "YES"
        else:
            return "NO"
        


if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)
