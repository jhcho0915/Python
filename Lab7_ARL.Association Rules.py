
# coding: utf-8

# In[ ]:


import pandas as pd
from apyori import apriori
import pyfim


# In[ ]:


order_data = pd.read_csv("./order_products__train.csv")
product_data = pd.read_csv("./products.csv")
named_orders = pd.merge(order_data, product_data, on = 'product_id')
counts = named_orders['product_name'].value_counts()


selected_orders = named_orders[named_orders['product_name'].isin(counts.index.values.tolist())]
selected_orders['cols'] = selected_orders.groupby('order_id').cumcount()
selected_pivot = selected_orders.pivot(index='order_id', columns='cols')[['product_name']]
selected_pivot.head()

purchases = []
for i in range(0,len(selected_pivot)):
    purchases.append([str(selected_pivot.values[i,j]) for j in range(0,25)])

rules = apriori(purchases, min_support = 0.01, min_confidence = 0.1, min_lift = 3, min_length = 20)
results = list(rules)

rule_counter = 0
for i in range(0, len(results)):
    result = results[i]
    supp = int(result.support*10000)/100
    conf = int(result.ordered_statistics[0].confidence*100)
    hypo = ''.join([x + '' for x in result.ordered_statistics[0].items_base])
    conc = ''.join([x + '' for x in result.ordered_statistics[0].items_add])
    if "nan" not in hypo:
        rule_counter = rule_counter + 1
        print("If "+str(hypo)+ " is purchased, "+str(conf)+ " % of the time "+str(conc)+" is purchased [support = "+str(supp)+"%]")
print("Total rules built, omitting NaN: " + str(rule_counter))


# In[23]:


counts


# In[24]:


rules = pyfim.eclat(purchases, supp=1, zmin = 2, out = [])


# In[14]:


rule_count = 0
for i in range(0, len(rules)):
    supp = round(int(rules[i][1]) / len(purchases)*100,3)
    items = rules[i][0]
    if "nan" not in items:
        rule_count = rule_count + 1
        item_1 = rules[i][0][0]
        item_2 = rules[i][0][1]
        print("If "+str(item_1)+ " is purchased, "+str(supp)+ " % of the time "+str(item_2)+" is purchased [absolute support = "+ str(rules[i][1])+"]")
print("Total rules built, omitting NaN: " + str(rule_count))

