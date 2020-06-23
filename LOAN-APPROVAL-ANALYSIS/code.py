# --------------
# Importing header files
import numpy as np
import pandas as pd
import math
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')
bank = pd.read_csv(path)
categorical_var=bank.select_dtypes(include = 'object')
numerical_var=bank.select_dtypes(include = 'number')

banks=bank.drop("Loan_ID",axis=1)
bank_mode=banks.mode()
for col in banks.columns:
    val=banks[col].mode()
    banks[col].fillna(val[0],inplace=True)
bank=banks

# step3
avg_loan_amount=pd.pivot_table(bank,index=['Gender', 'Married', 'Self_Employed'],values="LoanAmount")

# step4
loan_approved_se=sum([(banks['Self_Employed']== 'Yes') & (banks['Loan_Status']== 'Y')][0])
loan_approved_nse=sum([(banks['Self_Employed']== 'No') & (banks['Loan_Status']== 'Y')][0])
percentage_se=round((100/614)*loan_approved_se,2)
percentage_nse=round((100/614)*loan_approved_nse,2)

# step 5
bank["loan_term"]=bank["Loan_Amount_Term"].apply(lambda x : math.ceil(x/12))
big_loan_term= bank[ bank["loan_term"]>=25 ].count()[0]

# step 6
loan_groupby=bank[["Loan_Status",'ApplicantIncome', 'Credit_History']].groupby("Loan_Status")
mean_values=loan_groupby.mean()





