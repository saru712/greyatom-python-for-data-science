# --------------
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv(path)
plt.figure(figsize=[14,8])
plt.xlabel("Loan Approvals ")
plt.ylabel("No of loans")
plt.title("visualizing the company's record with respect to loan approvals")
loan_status =data['Loan_Status'].value_counts(ascending=False)

loan_status.plot(kind="bar")

plt.show()




# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

# Plot stacked bar chart
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
# Display plot
plt.show()


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))

# Plot stacked bar chart
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
# Display plot
plt.show()#Code starts here


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

graduate=data[(data['Education']=='Graduate')]

not_graduate=data[(data['Education']=='Not Graduate')]

graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
# Initialize figure and axes
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(20,10))

# ts

data.plot.scatter(x='ApplicantIncome', y='LoanAmount')
ax_1.set_title('Applicant Income')
data.plot.scatter(x='CoapplicantIncome', y='LoanAmount')
ax_2.set_title('Coapplicant Income')
data['TotalIncome']=data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome', y='LoanAmount')
ax_3.set_title('Total Income')





