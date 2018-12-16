'''
    pip install ipython 
    pip3 install ipython 
    python3 -m pip install ipython 
'''

import pandas
df1=pandas.DataFrame([[2,4,6],[10,20,30]])
df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"], index=["First","Second"])

df2 = pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])
df2 = pandas.DataFrame([{"Name":"John", "SurName":"Os"},{"Name":"Jack", "SurName":"Ask"}])

type(df1) # pandas.core.frame.DataFrame

dir(df1)

df1.mean()
'''
    Price     6.0
    Age      12.0
    Value    18.0
    dtype: float64
'''

df1.mean().mean()
'''
    12.0
'''
type(df1.mean()) # pandas.core.series.Series

df1.Price
'''
    First      2
    Second    10
    Name: Price, dtype: int64
'''
df1.Price.mean()
'''
    6.0
'''

