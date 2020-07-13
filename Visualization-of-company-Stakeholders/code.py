# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1 
#Reading the file
data=pd.read_csv(path)

#Creating a new variable to store the value counts
loan_status=data["Loan_Status"].value_counts()
#Plotting bar plot
loan_status.plot.bar()


# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(["Property_Area","Loan_Status"])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind="bar",stacked=False)
#Changing the x-axis label
plt.xlabel("Property Area")
#Changing the y-axis label
plt.ylabel("Loan Status")
#Rotating the ticks of X-axis
plt.xticks(rotation=45)
# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(["Education","Loan_Status"]).size().unstack()
education_and_loan.plot.bar(stacked=True)
#Changing the x-axis label
plt.xlabel("Education Status")

#Changing the y-axis label
plt.ylabel("Loan Status")

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data["Education"]=="Graduate"]

#Subsetting the dataframe based on 'Education' column
not_graduate=data[data["Education"]=="Not Graduate"]

#Plotting density plot for 'Graduate'
graduate.plot(kind="density",label="Graduate")

#Plotting density plot for 'not Graduate'
not_graduate.plot(kind="density",label="Not Graduate")
# Step 5
#Setting up the subplots
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1)

#Plotting scatter plot
ax_1.scatter(x=data["ApplicantIncome"],y=data["LoanAmount"])
ax_1.set_title("Applicant Income")
ax_2.scatter(x=data['CoapplicantIncome'],y=data["LoanAmount"])
ax_2.set_title("Coapplicant Income")
data["TotalIncome"]=data["ApplicantIncome"]+data["CoapplicantIncome"]
ax_3.scatter(x=data["TotalIncome"],y=data["LoanAmount"])
ax_3.set_title("Total Income")



