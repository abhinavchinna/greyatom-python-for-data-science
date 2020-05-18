# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((new_record,data))
print(census)
print(census.shape)
age=census[:,0]
max_age=int(age.max())
print(" ",max_age)
min_age=int(age.min())
print(min_age)
age_mean=round(age.mean(),2)
print(age_mean)
age_std=round(age.std(),2)
print(age_std)
mask0=census[:,2]==0
race_0=census[mask0]
mask1=census[:,2]==1
race_1=census[mask1]
mask2=census[:,2]==2
race_2=census[mask2]
mask3=census[:,2]==3
race_3=census[mask3]
mask=census[:,2]==4
race_4=census[mask]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)
a=[len_0,len_1,len_2,len_3,len_4]
for i in range(len(a)):
    if a[i]==min(a):
        minority_race=i
        break
    else:
        continue
print(minority_race)
senior_citizens=census[census[:,0]>60]
working_hours_sum=int(np.sum(senior_citizens[:,6]))
print(working_hours_sum)
avg_working_hours=working_hours_sum/len(senior_citizens)
print(avg_working_hours)
high,low=census[census[:,1]>10],census[census[:,1]<=10]
avg_pay_high=round(np.mean(high[:,7]),2)
avg_pay_low = round(np.mean(low[:,7]),2)
print(avg_pay_high,avg_pay_low)





