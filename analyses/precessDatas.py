
import pandas as pd ## library00 to read files
import numpy as np ## library to process datas

## Import files to analyses

# CurrentAccount
# The location of the file which is to be retrieved using this function.
# I'll use the file path of github, because is better to other devs make the same. 
currenteAccount_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/balanca%20comercial.csv"
# It stands for separator
sep_ca = ';'
df = pd.read_csv(currenteAccount_url, sep=sep_ca)

## type
# print(type(df))

## access elements in df
## top 4
# print('top 4')
# print(df[:3])

# ## lasts 3
# print('last 3')
# print(df[-3:])


## Every other element multple
# print('others elemets multiple')
# print(df[::10])

## check the type of an Array
# print('check the type')
# print(df.dtypes)

## copy and view data
## copy
# cp = df.copy()
# cp = cp[::50]

# print('Original data')
# print(df.head)

# print('Copy data')
# print(cp.head)



## copy and view data
# ## view

# vw = df.view
# print(vw)
# vw = vw[::50]

# print('Original data')
# print(df.head)

# print('View data')
# print(vw.head)


a = np.array([[1,2,3,4],[9,0,2,3],[1,2,3,19]])  
print('array a')
print(a)

print('view')
b = a.view()
b = b[:-1]
print('array b')
print(b)

# print('original')
# print(a)