# basics_python

import string

size=5
result=[]
s=""
for i in range(size):
    s="-".join(string.ascii_lowercase[i:size])
    result.append((s[::-1]+s[1:]).center((4*size)-3, "-"))
[print(i) for i in result[:0:-1]]
[print(i) for i in result]

o/p:-
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
