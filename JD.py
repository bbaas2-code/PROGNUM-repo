#!/usr/bin/env python
# coding: utf-8

# In[ ]:


d =float(input("days begin:"))
m =float(input("months begin:"))
y =float(input("years begin:"))

D =float(input("days end:"))
M =float(input("months end:"))
Y =float(input("years end"))

jd=  367*y -7*(y+(m+9)/12)/4 - 3*((y+(m-9)/7)/100 + 1)/4 + (275*m)/9 + d + 1721029-0.5
JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5

p = JD-jd
print (f"number of days between two dates{p}")


# In[ ]:




