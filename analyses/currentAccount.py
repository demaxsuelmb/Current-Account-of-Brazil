# installing the libraries to processing and analyses

import pandas as pd ## library to read files
import numpy as np ## library to process datas

## Import files to analyses

# CurrentAccount
# The location of the file which is to be retrieved using this function.
currenteAccount_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/balanca%20comercial.csv"
# It stands for separator
sep_ca = ';'
df_ca = pd.read_csv(currenteAccount_url, sep=sep_ca)


# PrimaryIncome
# The location of the file which is to be retrieved using this function.
primaryIncome_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/rendaPrimaria.csv"
# It stands for separator
sep_pi = ';'
df_pi = pd.read_csv(primaryIncome_url, sep=sep_pi)

# SecondIncome
# The location of the file which is to be retrieved using this function.
secondIncome_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/rendaSecundaria.csv"
# It stands for separator
sep_si = ';'
df_si = pd.read_csv(secondIncome_url, sep=sep_si)


# Services
# The location of the file which is to be retrieved using this function.
services_url = "https://raw.githubusercontent.com/demaxsuelmb/Current-Account-of-Brazil/main/bases/servicos.csv"
# It stands for separator
sep_s = ';'
df_s = pd.read_csv(services_url, sep=sep_s)





