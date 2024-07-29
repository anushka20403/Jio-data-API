#!/usr/bin/env python
# coding: utf-8

# In[316]:


import pandas as pd


# In[317]:


df=pd.read_csv('myjio_tdata.csv')


# In[364]:


#5.Total Recharges , Succces and failure reports Pg wise


def PG(df):
        
        total= df[df['TRANSACTIONTYPE'] == 'RECHARGE'].groupby('PG_NAME').size()
        notconfirm= df[(df['TRANSACTIONTYPE'] == 'RECHARGE') & (df['STATUS'] == 'BENEFIT-WIP-NOTCONFIRMED')].groupby('PG_NAME').size()
        success_reports = df[(df['TRANSACTIONTYPE'] == 'RECHARGE') & (df['STATUS'] == 'CLOSED-SUCCESSFUL')].groupby('PG_NAME').size()
        failure_reports = df[(df['TRANSACTIONTYPE'] == 'RECHARGE') & (df['STATUS'] == 'CLOSED-ABORTED')].groupby('PG_NAME').size()
        data={
             'SUCCESS': success_reports,
             'FAILURES': failure_reports,
            'WIP-NOTCONFIRMED': notconfirm,
            'TOTAL RECHARGES': total,}
        df2=pd.DataFrame(data, dtype=int).fillna(0)
        df2['%SUCCESS'] = (df2['SUCCESS'] / df2['TOTAL RECHARGES']) * 100
        df2['%FAILURE'] = (df2['FAILURES'] / df2['TOTAL RECHARGES']) * 100
        df2['%NOT_CONFIRMED'] = (df2['WIP-NOTCONFIRMED'] / df2['TOTAL RECHARGES']) * 100
        df2.reset_index(inplace = True)
        df2.rename(columns={'index': 'PG_NAME'}, inplace=True)
        return df2



# In[246]:


#7.Comparison b/w recharge count , success and failure


def comparison(df):
    df2=PG(df)
    totalrecharges=df2['TOTAL RECHARGES'].sum()
    totalsuccess=df2['SUCCESS'].sum()
    totalfailures=df2['FAILURES'].sum()
    
    success_percentage = (totalsuccess / totalrecharges) * 100
    failure_percentage = (totalfailures / totalrecharges) * 100
        

    s = pd.Series([totalrecharges, totalsuccess, totalfailures, success_percentage, failure_percentage], index=['Total Recharges', 'Total Success', 'Total Failures', '%success', '%failure'], name='Comparison')
    return s



# In[89]:


#no of requests per pg(success or fail or not confirmed)


def RequestsPerPG(df):
    x=df.groupby(['PG_NAME'])['STATUS'].size().rename('TOTAL')
    rpg=x.to_frame()
    return rpg


# In[90]:




# In[91]:


#total requests per pg and which requests 


def RequestSorF(df):
    
    RequestSorF=df.groupby(['PG_NAME','STATUS']).size().unstack(fill_value=0)
    df2=RequestSorF.join(RequestsPerPG(df))
    return df2


# In[92]:




# In[93]:


#1. top 5 most utilized PGS


def max5PG(df):
    rpg = RequestsPerPG(df)
    sorted_df=rpg.sort_values(by= 'TOTAL', ascending=False)
    sorted_df.reset_index(inplace = True)
    return sorted_df.head(5)


# In[94]:




# In[264]:


#2. top 5 most utilized payment mode


def RequestsPerPayMODE(df):
    x=df.groupby(['PAYMENTMODE'])['STATUS'].size().rename('TOTAL')
    paymode=x.to_frame()
    return paymode

def max5PayMode(df):
    pay = RequestsPerPayMODE(df)
    sorted_df=pay.sort_values(by= 'TOTAL', ascending=False)
    sorted_df.reset_index(inplace = True)
    return sorted_df.head(5)



# In[200]:



# In[201]:



# In[365]:


#6.timebased failure and success ratio


def timebased(df):
        df['CREATIONDATE'] = df['CREATIONDATE'].astype(str).str.replace('IST', '', regex=False)
        df['CREATIONDATE_NEW1'] = pd.to_datetime(df['CREATIONDATE'], format='%a %b %d %H:%M:%S %Y', errors='coerce')
        df['TIME']=df['CREATIONDATE_NEW1'].dt.round('60T')
        x=df.groupby(['TIME','STATUS']).size().unstack(fill_value=0)
        y=df.groupby(['TIME'])['STATUS'].size().rename('TOTAL').to_frame()
        z=x.join(y)
        z.reset_index(inplace = True)
        z['%SUCCESS'] = (z['CLOSED-SUCCESSFUL'] / z['TOTAL']) * 100
        z['%FAILURE'] = (z['CLOSED-ABORTED'] / z['TOTAL']) * 100
        z['%NOT_CONFIRMED'] = (z['BENEFIT-WIP-NOTCONFIRMED'] / z['TOTAL']) * 100
        maxx=z['TOTAL'].max()
        z['PEAK_TIME']='NO'
        z.loc[z['TOTAL'] == maxx, 'PEAK_TIME'] = 'YES'
        return z

    
#4. Peak time when most of the recharges happens


def PeakTime(df):
    df2=timebased(df)
    x=df2.loc[df2['PEAK_TIME']=='YES','TIME']
    return x


# In[367]:


#3. pgs wise recharge counts reports.

def PGwise(df):
    result = df[df['TRANSACTIONTYPE'] == 'RECHARGE'].groupby(['PG_NAME']).size().rename('COUNT').to_frame()
    result.reset_index(inplace = True)
    return  result



# In[368]:


#3. payment wise recharge counts reports.


def PayWise(df):
    result = df[df['TRANSACTIONTYPE'] == 'RECHARGE'].groupby(['PAYMENTMODE']).size().rename('COUNT').to_frame()
    result.reset_index(inplace = True)
    return result



# In[263]:


#Number of success/failure/notconfirmed of transaction type and total requests per transaction type


def transactionTypeStatus(df):
        
        z=df.groupby(['TRANSACTIONTYPE'])['STATUS'].size().rename('TOTAL').to_frame()
        y=df.groupby(['TRANSACTIONTYPE','STATUS']).size().unstack(fill_value=0)
        new=y.join(z)
        return new




# In[209]:


#recharge count
df[df['TRANSACTIONTYPE'] == 'RECHARGE'].shape[0]


# In[208]:


#number of failures and succesces of recharges
df[df['TRANSACTIONTYPE'] == 'RECHARGE'].groupby(['STATUS']).size()

