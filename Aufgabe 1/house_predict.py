#%%
import pandas as pd

# %%
df = pd.read_csv("ames.csv") # load csv data
df = df.dropna() # check for missing values in dataframe and drop them
# %%

#Split in train und test data
dftrain = df[:2000] 
dftest = df[2001:]
# %%
df
# %%
