# installing the libraries to processing and analyses

import pandas as pd ## library00 to read files
import numpy as np ## library to process datas

## Import files to analyses

# CurrentAccount
# The location of the file which is to be retrieved using this function.
# I'll use the file path of github, because is better to other devs make the same. 
currenteAccount_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/balanca%20comercial.csv"
# It stands for separator
sep_ca = ';'
df_ca = pd.read_csv(currenteAccount_url, sep=sep_ca)

# print the data to verify if the data was correct
print("currentAccount df")
print("shape and df")
print(df_ca.shape)

#rename columns
df_ca =  df_ca.rename(columns={'data': 'date', 'valor': 'currentAccount'})
print(df_ca.head())


# PrimaryIncome
# The location of the file which is to be retrieved using this function.
primaryIncome_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/rendaPrimaria.csv"
# It stands for separator
sep_pi = ';'
df_pi = pd.read_csv(primaryIncome_url, sep=sep_pi)

# print the data to verify if the data was correct
print("primaryIncome df")
print("shape and df")
print(df_pi.shape)

#rename columns
df_pi = df_pi.rename(columns={"data":"date", "valor":"primaryIncome"})
print(df_pi.head())

# SecondIncome
# The location of the file which is to be retrieved using this function.
secondIncome_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/rendaSecundaria.csv"
# It stands for separator
sep_si = ';'
df_si = pd.read_csv(secondIncome_url, sep=sep_si)

# print the data to verify if the data was correct
print("secondIncome df")
print("shape and df")
print(df_si.shape)

#rename columns
df_si = df_si.rename(columns={"data":"date", "valor": "secondIncome"})
print(df_si.head())

# Services
# The location of the file which is to be retrieved using this function.
services_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/servicos.csv"
# It stands for separator
sep_s = ';'
df_s = pd.read_csv(services_url, sep=sep_s)

# print the data to verify if the data was correct 
print("service df")
print("shape and df")
print(df_s.shape)

#rename columns
df_s = df_s.rename(columns={"data":"date", "valor":"services"})
print(df_s.head())


# merge dataframes to a only df
# merge primaryIncome
df = pd.merge(df_ca, df_pi, how="left", on=["date"])
print(df.head())

# merge secondIncome
df = pd.merge(df_ca, df_si, how="left", on=["date"])
print(df.head())

# merge service
df = pd.merge(df_ca, df_s, how="left", on=["date"])
print(df.head())

