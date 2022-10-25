# %%
import pandas as pd
import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import yfinance as yf

# %%
df=pd.DataFrame()
df=yf.download("PETR4.SA CSNA3.SA ITUB4.SA JBSS3.SA TAEE11.SA",start='2017-01-01',end='2022-01-01')
df.head(5)

# %%
fig=plt.figure(figsize=(20,20))
fig.patch.set_facecolor("white")
ax1=fig.add_subplot(211,ylabel="Adj Close")
df["Adj Close"].div(df["Adj Close"].iloc[0]).plot(ax=ax1,lw=1.)
fig.show()

# %%
df2=yf.download("PETR4.SA CSNA3.SA ITUB4.SA JBSS3.SA TAEE11.SA",start='2017-01-01',end='2022-01-01')["Adj Close"]

df2["ShorterPETR"]=df2["PETR4.SA"].rolling(5,1).mean()
df2["ShorterITUB"]=df2["ITUB4.SA"].rolling(5,1).mean()
df2["ShorterCSNA"]=df2["CSNA3.SA"].rolling(5,1).mean()
df2["ShorterJBSS"]=df2["JBSS3.SA"].rolling(5,1).mean()
df2["ShorterTAEE"]=df2["TAEE11.SA"].rolling(5,1).mean()
df2["LongerPETR"]=df2["PETR4.SA"].rolling(20,1).mean()
df2["LongerITUB"]=df2["ITUB4.SA"].rolling(20,1).mean()
df2["LongerCSNA"]=df2["CSNA3.SA"].rolling(20,1).mean()
df2["LongerJBSS"]=df2["JBSS3.SA"].rolling(20,1).mean()
df2["LongerTAEE"]=df2["TAEE11.SA"].rolling(20,1).mean()
#df2[['ShorterPETR',"ShorterITUB","ShorterCSNA","ShorterJBSS","ShorterTAEE","LongerPETR","LongerITUB","LongerCSNA","LongerJBSS","LongerTAEE"]].plot(ax=ax1,lw=1.)
#fig.show()
df2.tail(10)

# %%
fig=plt.figure(figsize=(20,20))
fig.patch.set_facecolor("white")
ax1=fig.add_subplot(211,ylabel="Adj Close")
df["Adj Close"].div(df["Adj Close"].iloc[0]).plot(ax=ax1,lw=1.)
df2[['ShorterPETR',"ShorterITUB","ShorterCSNA","ShorterJBSS","ShorterTAEE","LongerPETR","LongerITUB","LongerCSNA","LongerJBSS","LongerTAEE"]].div(df2.iloc[0]).plot(ax=ax1,lw=1.)
fig.show()

# %%
df_ret=pd.DataFrame()

df_ret["RetornosPetr"]=(df2["PETR4.SA"]/df2['PETR4.SA'].shift(1)-1).dropna()
df_ret["LogRetornosPetr"]=np.log(df2["PETR4.SA"]/df2['PETR4.SA'].shift(1))
df_ret["RetornosCsna"]=df2["CSNA3.SA"]/df2['CSNA3.SA'].shift(1)-1
df_ret["LogRetornosCsna"]=np.log(df2["CSNA3.SA"]/df2['CSNA3.SA'].shift(1))
df_ret["RetornosItub"]=df2["ITUB4.SA"]/df2['ITUB4.SA'].shift(1)-1
df_ret["LogRetornosItub"]=np.log(df2["ITUB4.SA"]/df2['ITUB4.SA'].shift(1))
df_ret["RetornosJbss"]=df2["JBSS3.SA"]/df2['JBSS3.SA'].shift(1)-1
df_ret["LogRetornosJbss"]=np.log(df2["JBSS3.SA"]/df2['JBSS3.SA'].shift(1))
df_ret["RetornosTaee"]=df2["TAEE11.SA"]/df2['TAEE11.SA'].shift(1)-1
df_ret["LogRetornosTaee"]=np.log(df2["TAEE11.SA"]/df2['TAEE11.SA'].shift(1))

retTotalAnPetr=(df2["PETR4.SA"].iloc[-1]/df2["PETR4.SA"].iloc[0]-1)**(1/5)
logretTotalAnPetr=df_ret['LogRetornosPetr'].sum()
retTotalAnCsna=(df2["CSNA3.SA"].iloc[-1]/df2["CSNA3.SA"].iloc[0]-1)**(1/5)
logretTotalAnCsna=df_ret["LogRetornosCsna"].sum()
retTotalAnItub=(df2["ITUB4.SA"].iloc[-1]/df2["ITUB4.SA"].iloc[0]-1)**(1/5)
logretTotalAnItub=df_ret["LogRetornosItub"].sum()
retTotalAnJbss=(df2["JBSS3.SA"].iloc[-1]/df2["JBSS3.SA"].iloc[0]-1)**(1/5)
logretTotalAnJbss=df_ret['LogRetornosJbss'].sum()
retTotalAnTaee=(df2["TAEE11.SA"].iloc[-1]/df2["TAEE11.SA"].iloc[0]-1)**(1/5)
logretTotalAnTaee=df_ret["LogRetornosTaee"].sum()

print(df_ret.tail(5))
print(retTotalAnPetr,logretTotalAnPetr,retTotalAnCsna,logretTotalAnCsna,retTotalAnItub,logretTotalAnItub,retTotalAnJbss,logretTotalAnJbss,retTotalAnTaee,logretTotalAnTaee)

# %%
df_ret.hist(column=["LogRetornosPetr","LogRetornosCsna","LogRetornosItub","LogRetornosJbss","LogRetornosTaee"])

# %%
SharpePetr=df_ret["LogRetornosPetr"].mean()/df_ret["LogRetornosPetr"].std()
SharpeCsna=df_ret["LogRetornosCsna"].mean()/df_ret["LogRetornosCsna"].std()
SharpeItub=df_ret["LogRetornosItub"].mean()/df_ret["LogRetornosItub"].std()
SharpeJbss=df_ret["LogRetornosJbss"].mean()/df_ret["LogRetornosJbss"].std()
SharpeTaee=df_ret["LogRetornosTaee"].mean()/df_ret["LogRetornosTaee"].std()
print(SharpePetr,SharpeCsna,SharpeItub,SharpeJbss,SharpeTaee)
print(max(SharpePetr,SharpeCsna,SharpeItub,SharpeJbss,SharpeTaee))

# %%
peso=0.2
df3=pd.DataFrame()
df3['retPort']=(peso*df_ret["LogRetornosPetr"]+peso*df_ret['LogRetornosCsna']+peso*df_ret['LogRetornosItub']+peso*df_ret['LogRetornosJbss']+peso*df_ret['LogRetornosTaee'])
print(df3['retPort'].mean(),df3['retPort'].std())

# %%
df3['retPortAcum']=df3['retPort'].cumsum()
print(df3['retPortAcum'])

# %%
fig=plt.figure(figsize=(20,20))
fig.patch.set_facecolor("white")
ax1=fig.add_subplot(211,ylabel="Adj Close")
df["Adj Close"].div(df["Adj Close"].iloc[0]).plot(ax=ax1,lw=1.)
df3['retPortAcum'].div(df3['retPortAcum'].iloc[0]).plot(ax=ax1,lw=1.)


