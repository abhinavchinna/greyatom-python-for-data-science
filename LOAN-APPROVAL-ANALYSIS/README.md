Visualization for Company Stakeholders
Instructions :

Step 1

Let's start with the simple task of visualizing the company's record with respect to loan approvals.

    Save the value counts of Loan_Status in a variable called loan_status using value_counts()

    Plot a bar graph of loan_status
Step 2
Everyone needs money

The company provides financial assistance across the different regions of the country. One interesting statistic that stakeholders want to see is the loan approval distribution across the regions.
Instructions :

    Group the 'data' dataframe by Property_Area and Loan_Status and store it in a variable called 'property_and_loan'

    Use the .size() method on 'property_and_loan' and then use .unstack() and save it back to 'property_and_loan'

    Plot an unstacked bar plot of property_and_loan (It is similar to creating a stacked bar plot except change the parameter 'stacked' to False)

    Name the x-axis as Property Area

    Name the y-axis as Loan Status

    Rotate the labels of x-axis by 45o
Step 3
Expensive Education

Higher education has always been an expensive endeavour for people but it results in better career opportunities and stability in life. But does higher education result in a better guarantee in issuing loans?
Instructions :

    Group the 'data' dataframe by Education and Loan_Status and store it in a variable called 'education_and_loan'

    Use the .size() method on 'education_and_loan' and then use .unstack() and save it back to 'education_and_loan'

    Plot an stacked bar plot of education_and_loan

    Name the x-axis as Education Status

    Name the y-axis as Loan Status

    Rotate the labels of x-axis by 45o
Smarter and Richer?

After seeing the loan status distribution, let's check whether being graduate or not also leads to different loan amount distribution by plotting an overlapping density plot of two values
Instructions :

    Create a dataframe called 'graduate' which is a subset of 'data' dataframe with the condition "data['Education'] == 'Graduate'"

    Create a dataframe called 'not_graduate' which is a subset of 'data' dataframe with the condition "data['Education'] == 'Not Graduate'"

    Plot a density plot LoanAmount of 'graduate' dataframe using "Series.plot()" and pass the parameter kind='density' and label='Graduate'

    Do the same for LoanAmount of 'not_graduate' dataframe but with label='Not Graduate'
Income vs Loan

For any financial institution to be successful in its loan lending system, there has to be a correlation between the borrower's income and loan amount he is lent. Let's see how our company fares in that respect:
Instructions :

    Create three subplots with (nrows = 3 , ncols = 1) and store it in variable's fig ,(ax_1,ax_2,ax_3)

    Since both are continuous variables, plot scatter plot between 'ApplicantIncome' and LoanAmount using ax_1. Set axis title as Applicant Income

    Plot scatter plot between 'CoapplicantIncome' and LoanAmount using ax_2. Set axis title as Coapplicant Income

    Create a new column in the dataframe called 'TotalIncome' which is a sum of the values of columns ApplicantIncome and CoapplicantIncome

    Plot scatter plot between 'TotalIncome' and LoanAmount using ax_3. Set axis title as Total Income
