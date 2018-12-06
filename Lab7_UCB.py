
# coding: utf-8

# In[8]:


from slots import playSlots
import matplotlib.pyplot as plt
import random

N = 2000
d = 20
machine_record = []
award_record = []
balance = 1000.0
for n in range(0,N):
    machine_choice = random.randrange(1, d+1)
    machine_record.append(machine_choice)
    cash_reward = playSlots(machine = machine_choice)
    award_record.append(cash_reward)
    balance = (balance - 1.0) + cash_reward

plt.hist(machine_record, bins = 20)
plt.title("Machine Selection (End Balance: "+str(round(balance,2)) + ")")
plt.xlabel("Slot Machine")
plt.ylabel("Number of Times Used")
plt.show()


# In[9]:


from slots import playSlots
import matplotlib.pyplot as plt
import random

N = 2000
d = 20
machine_record = []
award_record = []
balance = 1000.0

number_of_selections = [0] * d
sum_of_rewards = [0] * d

for n in range(0,N):
    machine_choice = 1
    max_upper_bound = 0
    
    for i in range(1,d):
        if(number_of_selections[i] > 0):
            average_reward = sum_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n+1) / number_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e200

        if(upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            machine_choice = i
            
    machine_record.append(machine_choice)
    number_of_selections[machine_choice] = number_of_selections[machine_choice] + 1
    award = playSlots(machine = machine_choice)
    sum_of_rewards[machine_choice] = sum_of_rewards[machine_choice] + award
    balance = balance - 1 + award
    
plt.hist(machine_record, bins = 20)
plt.title("Machine Selection (End Balance: "+str(round(balance,2)) + ")")
plt.xlabel("Slot Machine")
plt.ylabel("Number of Times Used")
plt.show()
        

